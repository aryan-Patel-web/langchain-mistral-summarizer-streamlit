import os
import validators
import streamlit as st
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_huggingface import HuggingFaceEndpoint

# Load environment variables from .env
load_dotenv()

# Streamlit page configuration
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize content using Mistral LLM")

# Sidebar input for Hugging Face token
with st.sidebar:
    hf_api_key = st.text_input("🔑 Hugging Face API Token", value="", type="password")

# Main input for content URL
generic_url = st.text_input("Enter YouTube or Website URL")

# Prompt template for summarization
prompt_template = """
Provide a summary of the following content in 300 words:
Content: {text}
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Run on button click
if st.button("Summarize the Content from YT or Website"):
    if not hf_api_key.strip() or not generic_url.strip():
        st.error("Please provide both the Hugging Face token and a valid URL to get started.")
    elif not validators.url(generic_url):
        st.error("Invalid URL. Please enter a proper YouTube or website URL.")
    else:
        try:
            with st.spinner("⏳ Loading and summarizing content..."):
                # Load content from YouTube or web
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0"}
                    )

                docs = loader.load()

                # Initialize HuggingFace LLM endpoint
                repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
                llm = HuggingFaceEndpoint(
                    repo_id=repo_id,
                    huggingfacehub_api_token=hf_api_key,
                    temperature=0.7,
                    max_new_tokens=150
                )

                # Summarize using LangChain
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                summary = chain.run(docs)

                st.success("✅ Summary Generated:")
                st.write(summary)

        except Exception as e:
            st.exception(f"❌ Exception: {e}")
