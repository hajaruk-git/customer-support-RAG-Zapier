from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "system",
        "content": """Generate a structured .txt file containing realistic FAQs and answers for a Moroccan e-commerce business that sells t-shirts.

The store operates from Morocco and offers international delivery to Europe and North America.

Cover common topics such as:
- shipping (countries, delays, customs, fees)
- payment methods (cards, currencies, security)
- sizing and fit
- product materials and quality
- return and exchange policies
- personalization options
- contact and support
- special offers and discounts
- ethical production and sustainability

Use the following format:
Q: [customer question]
A: [clear and professional answer]

Provide around 20 to 25 Q&A pairs."""
    }]
)

with open("content.txt", "w") as my_file:
    my_file.write(response.choices[0].message.content)