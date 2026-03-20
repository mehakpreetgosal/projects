import os
from openai import OpenAI
from dotenv import load_dotenv

# Loading environment variables (ensure you have OPENAI_API_KEY set in a .env file)
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit("Please set OPENAI_API_KEY in .env or environment variables.")
client = OpenAI(api_key=api_key)
SYSTEM_PROMPT = "You are a helpful and friendly assistant."
def chat_with_ai(user_input, history):
    history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=history,
        temperature=0.7,
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply

messages_history = [{"role": "system", "content": SYSTEM_PROMPT}]
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("AI: Goodbye!")
        break
    if user_input.lower() == "hello":
        print("AI: hello!")
        print("AI: how can I help you?")
    



