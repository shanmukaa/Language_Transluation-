# 🌏🔁 Language Translator: English ↔️ Hindi 🚀

Welcome to the **English-Hindi Neural Machine Translation** project!  
Easily translate text between English and Hindi using state-of-the-art AI models.  
Whether you want to translate sentences, documents, or try out neural translation in your web browser, this project is for you!

---

## ✨ Features

- 🧠 **Powered by Transformers**: Uses MarianMT models for accurate translations.
- 🏋️‍♂️ **Trained on IIT Bombay Parallel Corpus**: High-quality, large dataset ensures robust results.
- 🔄 **Bidirectional Translation**: Translate English to Hindi **and** Hindi to English!
- 📄 **PDF Support**: Upload a PDF and translate its content in one click.
- 🌐 **Interactive Web App**: Friendly, modern interface for instant translations.
- ⚡ **Fast & Efficient**: Optimized for quick results using PyTorch and batch processing.

---

## 🧑‍💻 Technologies Used

- **Python** 🐍
- **PyTorch** 🔥
- **Transformers (Hugging Face)** 🤗
- **Flask** 🌶️
- **Jupyter Notebook**
- **Bootstrap 5** 🎨
- **HTML/CSS & JavaScript**
- **PyPDF2** 📄

---

## 🚀 Quick Start

### 1️⃣ **Clone the Repository**

```sh
git clone https://github.com/shanmukaa/Language_Transluation-.git
cd Language_Transluation-
```

### 2️⃣ **Install Requirements**

```sh
pip install -r requirements.txt
```

Or install manually:
```sh
pip install flask torch transformers PyPDF2
```

### 3️⃣ **Run the Web App**

```sh
python english_to_hindi_translation_app.py
```

Then open your browser and go to http://localhost:5000

---

## 🖥️ Project Structure

```
.
├── english-to-hindi-translation.ipynb    # Jupyter notebook: Model training & demo
├── english_to_hindi_translation_app.py   # Flask web app for interactive translation
├── templates/
│   └── index.html                       # Modern Bootstrap-based UI
├── uploads/                             # Stores uploaded PDFs temporarily
└── README.md                            # This file
```

---

## 📚 Dataset & Model

- **Dataset**: IIT Bombay English-Hindi Parallel Corpus
- **Model**: MarianMT for English-Hindi and Hindi-English translation
- **Frameworks**: Transformers, PyTorch, Flask

---

## 🛠️ How It Works

1. **Preprocess Data**: Tokenize and pair English & Hindi sentences.
2. **Model Training**: Fine-tune MarianMT (or use pre-trained weights).
3. **Inference**: Input text (or PDF), select translation direction, and get instant results!
4. **Web Interface**: Use the sleek web app to translate anything in real time.

---

## 🧑‍💻 Example

**English ➡️ Hindi**
```
Input: "Machine translation is awesome!"
Output: "मशीन अनुवाद अद्भुत है!"
```

**Hindi ➡️ English**
```
Input: "मुझे हिंदी से अंग्रेज़ी अनुवाद चाहिए।"
Output: "I need translation from Hindi to English."
```

---

## 📦 Dependencies

- flask
- torch
- transformers
- PyPDF2

---

## 💡 Ideas for Improvement

- 🗣️ Add speech-to-text and text-to-speech
- 📱 Make a mobile-friendly version
- 📝 Support for more file formats (Word, TXT)
- 🏃‍♂️ Batch translation for large documents
- ☁️ Deploy on cloud for public access

---

## 📬 Contact

Made with ❤️ by shanmukaa  
Feel free to open issues or suggestions!

---

> "Bridging languages, breaking barriers." 🌏✨
