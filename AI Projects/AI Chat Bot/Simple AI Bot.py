from openai import OpenAI
import streamlit as st

# Create a variable to store the api
client = OpenAI(
        api_key= "your_api_key_here",
        base_url= "https://api.groq.com/openai/v1"

)


# Now create a loop 
while True:
    user_msg= input("You: ")

    if user_msg.lower() == "exit":
        break

    # Now create a response variable
    response = client.chat.completions.create(
        model= "llama-3.3-70b-versatile", # Here we can chnage the name of each model
        messages= [
            {
                "role": "system",
                "content": "You are a world best ai engineer"
            },
            {
                "role": "user",
                "content": user_msg
            }
        ]

    )

    print("Bot: ", response.choices[0].message.content)