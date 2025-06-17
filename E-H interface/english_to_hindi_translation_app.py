from flask import Flask, render_template, request, flash
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
import tensorflow as tf
import os
from werkzeug.utils import secure_filename
import PyPDF2

app = Flask(__name__)
app.secret_key = "your_secret_key"

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'pdf'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Pre-load both models and tokenizers
MODELS = {
    "en-hi": {
        "checkpoint": "Helsinki-NLP/opus-mt-en-hi",
        "tokenizer": None,
        "model": None
    },
    "hi-en": {
        "checkpoint": "Helsinki-NLP/opus-mt-hi-en",
        "tokenizer": None,
        "model": None
    }
}

for direction in MODELS:
    MODELS[direction]["tokenizer"] = AutoTokenizer.from_pretrained(MODELS[direction]["checkpoint"])
    MODELS[direction]["model"] = TFAutoModelForSeq2SeqLM.from_pretrained(MODELS[direction]["checkpoint"])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def translate_text(input_text, direction):
    tokenizer = MODELS[direction]["tokenizer"]
    model = MODELS[direction]["model"]
    tokenized = tokenizer([input_text], return_tensors='tf', truncation=True)
    out = model.generate(**tokenized, max_length=256)
    translated = tokenizer.batch_decode(out, skip_special_tokens=True)
    return translated[0] if translated else ""

@app.route('/', methods=['GET', 'POST'])
def translate():
    translation = ""
    input_text = ""
    pdf_text = ""
    direction = request.form.get("direction", "en-hi")
    if request.method == 'POST':
        # Check if user uploaded a PDF
        if 'pdf_file' in request.files and request.files['pdf_file'].filename != "":
            pdf_file = request.files['pdf_file']
            if pdf_file and allowed_file(pdf_file.filename):
                filename = secure_filename(pdf_file.filename)
                pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                pdf_file.save(pdf_path)
                pdf_text = extract_text_from_pdf(pdf_path)
                input_text = pdf_text
                # Limit translation for large PDFs
                if len(pdf_text) > 1500:
                    input_text = pdf_text[:1500]
                    flash("PDF too large, only the first 1500 characters are translated.", "warning")
                translation = translate_text(input_text, direction)
                os.remove(pdf_path)
            else:
                flash("Invalid file type. Please upload a PDF.", "danger")
        else:
            # Handle plain text input
            input_text = request.form.get("english_text", "")
            if input_text.strip():
                translation = translate_text(input_text, direction)
    return render_template('index.html', translation=translation, input_text=input_text, pdf_text=pdf_text, direction=direction)

if __name__ == '__main__':
    app.run(debug=True)