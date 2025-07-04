
# LangChain Mistral Summarizer (Streamlit)

🦜 A Streamlit app that summarizes text content from YouTube videos or website URLs using **LangChain** and the **Mistral 7B Instruct LLM** hosted on Hugging Face.

---

## 💡 Features

✅ Summarize YouTube videos into concise summaries  
✅ Summarize any webpage content  
✅ Works via Hugging Face Inference API  
✅ Customizable prompt template  
✅ Simple, interactive Streamlit UI

---

## 🛠️ Requirements

- Python 3.10+
- Hugging Face account with an API token

---

## 🚀 Installation

Install Python packages:

```bash
pip install -r requirements.txt

---

## ✅ requirements.txt

Here’s the minimal requirements list:

```txt
streamlit
python-dotenv
langchain
langchain-community
langchain-core
langchain-huggingface
validators


🔑 Environment Variables
Create a .env file in the root of your repo:


HF_TOKEN=your_hugging_face_api_token_here


🌐 Running the App
Run your Streamlit app locally:

streamlit run app.py

🎯 Usage
Enter your Hugging Face API token in the sidebar.

Paste a YouTube URL or a webpage URL into the input box.

Click Summarize the Content from YT or Website.

See your summary displayed instantly!


Example URLs:

https://www.youtube.com/watch?v=dQw4w9WgXcQ
or
https://en.wikipedia.org/wiki/Natural_language_processing


👨‍💻 Author
Aryan Patel

🌟 Future Enhancements
Save summaries to PDF

Support chunked summaries for long transcripts

Support multilingual summaries

Add usage analytics dashboard