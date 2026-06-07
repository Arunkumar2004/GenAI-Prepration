from openai import OpenAI
from pydantic import BaseModel
from fastapi import FastAPI

# Add this line after imports
app = FastAPI()  # Create a variable to store the api



# Create a variable to store the api
client = OpenAI(
        api_key= "Your API KEY", # Here you can add your api key
        base_url= "https://api.groq.com/openai/v1"

)

# Histroy of the conversation
messages= [{ "role": "system", "content": "You are a world best ai engineer"}]

# Create a pydantic model to store the user message
class UserMessage(BaseModel):
    message: str


@app.post("/chat")
def chat(user_message: UserMessage):
    
    #Step 1: Save user msg in the messages list 
    messages.append({"role": "user","content": user_message.message})

    # Step 2: send all the msg history
    response = client.chat.completions.create(
        model= "llama-3.3-70b-versatile", # Here we can chnage the name of each model  
        messages= messages
    )
    bot_reply= response.choices[0].message.content

    # Step 3: save the bot reply in the messages list
    messages.append({"role": "assistant", "content": bot_reply})


    return {
        "bot": bot_reply,
        "msg_length": len(messages)

}