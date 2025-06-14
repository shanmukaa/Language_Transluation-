import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
import PyPDF2

# Set page configuration
st.set_page_config(page_title="Text & PDF Translator", layout="centered")

# Model mapping for translation directions
MODEL_MAP = {
    "English to Hindi": "Helsinki-NLP/opus-mt-en-hi",
    "Hindi to English": "Helsinki-NLP/opus-mt-hi-en"
}

@st.cache_resource
def load_model_and_tokenizer(model_name):
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def translate_text(text, tokenizer, model):
    inputs = tokenizer.prepare_seq2seq_batch([text], return_tensors="pt", truncation=True, padding=True)
    translated = model.generate(**inputs, max_length=512)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Streamlit UI
st.title("📝 Text & PDF Translator")
st.markdown("Translate between **English ↔ Hindi** using text input or PDF upload.")

# Language direction selection
direction = st.selectbox("Select translation direction:", list(MODEL_MAP.keys()))

# Load appropriate model
tokenizer, model = load_model_and_tokenizer(MODEL_MAP[direction])

# Option to upload PDF or enter text
input_type = st.radio("Choose input method:", ("Text", "PDF File"))

if input_type == "Text":
    user_input = st.text_area("Enter your text below:", height=200)
    if st.button("Translate"):
        if user_input.strip():
            output = translate_text(user_input.strip(), tokenizer, model)
            st.success("**Translated Output:**")
            st.write(output)
        else:
            st.warning("Please enter some text to translate.")

else:  # PDF file input
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file and st.button("Translate PDF"):
        extracted_text = extract_text_from_pdf(uploaded_file)
        if extracted_text.strip():
            output = translate_text(extracted_text.strip(), tokenizer, model)
            st.success("**Translated PDF Content:**")
            st.write(output)
        else:
            st.warning("Could not extract text from PDF. Try a different file.")
