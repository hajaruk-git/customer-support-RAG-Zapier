from openai import OpenAI
import os
from dotenv import load_dotenv
from llama_index.core import Document, VectorStoreIndex

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

with open("content/content.txt") as my_file:
    doc = Document(text=my_file.read())
index = VectorStoreIndex.from_documents([doc])
query_engine = index.as_query_engine()

def llama(question):
    return query_engine.query(question).response


def responder(user_question):
    messages=[{
        "role": "system",
        "content": f"""Based on the context delimited by triple backticks,
    answer the user's question delimited by brackets.
    Context: ```{llama(user_question)}```
    Question: [{user_question}]"""
    }]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
    )
    
    return response.choices[0].message.content


def classifier(user_question):
    messages=[{
        "role": "system",
        "content": f"""Based on the question delimited by brackets,
    classify it in one of the following categories:
    - Product
    - Price
    - Shipping
    - Return
    - Payment
    - Order Status
    - Custom Order
    - Other
    Only return the category name. Do not explain your choice.
    Question: [{user_question}]"""
    }]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
    )
    
    return response.choices[0].message.content