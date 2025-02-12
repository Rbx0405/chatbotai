import openai

OPENAI_API_KEY = "your_openai_api_key"

def chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" if needed
        messages=[{"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_input = input("You: ")
    print("ChatGPT:", chatgpt_response(user_input))