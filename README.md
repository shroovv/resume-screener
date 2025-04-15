# 🤖 AI Resume Screener

AI-powered resume screening tool that analyzes resumes against job descriptions using Mistral-7B via Hugging Face Inference API.

Built with:
- 🔍 LLM-Powered Resume Scoring (Positives & Negatives)
- 🧠 Mistral-7B-Instruct (via Hugging Face API)
- ⚡ Streamlit Frontend
- 📄 PDF Resume Parsing (PyMuPDF)

---

## 🚀 Features

- Upload a resume (PDF)
- Paste any job description
- Receive structured, explainable output:
  - ✅ **Positives**: What matches
  - ⚠️ **Negatives**: What’s missing
- Works fully locally + Hugging Face cloud inference

---

## 🛠️ Tech Stack

- `streamlit` — for UI
- `PyMuPDF` — extract text from PDFs
- `requests` — to call Hugging Face API
- `Mistral-7B-Instruct` — powerful open-source LLM

---

## 🧪 Usage

### 1. Clone this repo
```bash
git clone https://github.com/shroovv/resume-screener.git
cd resume-screener
```

### 2. Set up your virtual environment
```bash
python -m venv venv
.env\Scripts\Activate.ps1   # Or `venv\Scripts\activate` for CMD
pip install -r requirements.txt
```

### 3. Add your Hugging Face API token
Get one from: https://huggingface.co/settings/tokens

Then create a `.env` file:
```
HF_API_TOKEN=your_token_here
```

Or paste it directly into `screener.py` for testing.

### 4. Run the app
```bash
streamlit run app.py
```

---

## 📦 Dependencies

```txt
streamlit
PyMuPDF
requests
```

---

## 📘 License

MIT — feel free to fork, build on, or modify this for your own applications.

---

## 👨‍💻 Built by

**Shravan Srinivasan**
