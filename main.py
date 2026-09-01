import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Initialize the client
client = OpenAI()

def generate_response(prompt):
    # Create a chat completion using the latest SDK syntax
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a concise, helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract and return the text from the response
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Sending request to OpenAI...")
    reply = generate_response("Explain what an API is in one sentence.")

    print("\n--- OpenAI Response ---")
    print(reply)