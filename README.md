
# 🌟 Gemini Text Generation with Google Generative AI API

This simple Python program uses Google's **Generative AI (Gemini)** to generate text content via the **`google-generativeai`** Python library.

---

## 📌 Features
- Load Gemini model (e.g., `gemini-1.5-flash-latest`)
- Send a prompt and receive a generated response
- Clean and simple structure

---

## 🔐 1. Get Your API Key

1. Visit: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Log in with your Google account.
3. Click **"Create API Key"**.
4. **Copy your API key.**

---

## 📦 2. Install Requirements

You need Python 3.7+ and the required packages:

```bash
pip install google-generativeai
```

---

## 📁 3. Project Structure

```
gemini_app/
├── simple_ai_agent.py
└── README.md
```

---

## 🧠 4. Usage Example (`simple_ai_agent.py`)

```python
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="YOUR_API_KEY")

# Load the Gemini model (text-only version)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Send a prompt
response = model.generate_content("What is the capital of Japan?")
print(response.text)
```

Replace your api_key you get from step 1 instead of `YOUR_API_KEY`, But **do not commit this version to public repositories**.

```python
genai.configure(api_key="YOUR_API_KEY")
```

---
---

## ⚙️ 5. Run the Program

```bash
python simple_ai_agent.py
```

Expected Output:
```
Tokyo
```

---

## 📎 References

- [Google Generative AI Python SDK](https://github.com/google/generative-ai-python)
- [Gemini API Documentation](https://ai.google.dev/)
- [MakerSuite](https://makersuite.google.com/)

---

## 📄 License
This project is licensed under the Apache 2.0 License.

---

## 🙌 Contributions
PRs are welcome — feel free to fork and improve this template!
