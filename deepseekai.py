import requests

DEEPSEEK_API_KEY = "your_deepseek_api_key"

def deepseek_response(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_input = input("You: ")
    print("DeepSeek:", deepseek_response(user_input))