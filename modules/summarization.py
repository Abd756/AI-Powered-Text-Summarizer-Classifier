# Summarization Module
# Functions for generating summaries using LangChain (LLM) only

from typing import List
from dotenv import load_dotenv
import os

# LangChain imports
from langchain_openai import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def summarize_documents(documents: List[str], api_key: str = None) -> List[str]:
    """Summarize a list of documents using LLM (abstractive) only, with custom prompt and output parser."""
    if not api_key:
        api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key required for summarization.")
    llm = OpenAI(openai_api_key=api_key)
    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
        Summarize the following text in 2-3 clear, concise sentences:
        {text}
        """
    )
    output_parser = StrOutputParser()
    results = []
    for doc in documents:
        formatted_prompt = prompt.format(text=doc)
        llm_output = llm.invoke(formatted_prompt)
        summary = output_parser.parse(llm_output)
        results.append(summary)
    return results

# Example usage:
# summaries = summarize_documents(docs)