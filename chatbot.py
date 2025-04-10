import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not found")
    exit(1)

openai.api_key = api_key

def get_chat_response(prompt: str) -> str:
    """Get a response from ChatGPT."""
    try:
        # Create the chat completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Keep responses concise and friendly."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("\n🌟 Welcome to ChatGPT Chatbot! 🌟")
    print("Type 'exit' to quit\n")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'exit':
            print("\n👋 Goodbye! Have a great day!")
            break
            
        print("\n🤖 Thinking...")
        response = get_chat_response(user_input)
        print(f"\n🤖: {response}")

if __name__ == "__main__":
    main()
