from openai import OpenAI

# Create a variable to store the api
client = OpenAI(
        api_key= "your_api_key_here",
        base_url= "https://api.groq.com/openai/v1"

)

# Histroy of the conversation
messages= [{ "role": "system", "content": "You are a world best ai engineer"}]

# Now create a loop 
while True:
    user_msg= input("You: ")

    if user_msg.lower() == "exit":
        break
    
    #Step 1: Save user msg in the messages list 
    messages.append({"role": "user","content": user_msg})

    # Step 2: send all the msg history
    response = client.chat.completions.create(
        model= "llama-3.3-70b-versatile", # Here we can chnage the name of each model  
        messages= messages
    )
    bot_reply= response.choices[0].message.content

    # Step 3: save the bot reply in the messages list
    messages.append({"role": "system", "content": bot_reply})


    print("Bot: ", bot_reply)
    print(len(messages))