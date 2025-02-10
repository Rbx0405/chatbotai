import requests

# DeepSeek Chat Assistant
def get_chat_response(prompt):
    chat_url = "https://api.deepseek.com/v1/chat/completions"
    chat_headers = {
        "Authorization": "Bearer sk-your_actual_api_key",  #API Key
        "Content-Type": "application/json"
    }
    chat_payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Respond in 1-2 lines, under 30 words. Ask before elaborating."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(chat_url, headers=chat_headers, json=chat_payload)
    
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
    return f"Error {response.status_code}: {response.text}"

# Sports Stats (SportsData API)
def get_sports_stats():
    sports_url = "https://api.sportsdata.io/v4/soccer/scores/json/Competitions"
    sports_headers = {"Ocp-Apim-Subscription-Key": "your_sportsdata_api_key"}  # Replace with your SportsData API Key
    response = requests.get(sports_url, headers=sports_headers)
    
    if response.status_code == 200:
        data = response.json()
        return data[:3]  # Returning first 3 competitions for brevity
    return f"Error {response.status_code}: {response.text}"

# Weather Updates (OpenWeather API)
def get_weather(city):
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_openweather_api_key&units=metric"  # Replace with your OpenWeather API Key
    response = requests.get(weather_url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {condition}."
    return f"Error {response.status_code}: {response.text}"

# Main Function
if __name__ == "__main__":
    while True:
        print("\n🤖 How can I help you today?")
        print("1️⃣ Chat with AI\n2️⃣ Get Sports Stats\n3️⃣ Check Weather\n4️⃣ Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            user_input = input("Ask me anything: ")
            print(get_chat_response(user_input))

        elif choice == "2":
            print(get_sports_stats())

        elif choice == "3":
            city = input("Enter city name: ")
            print(get_weather(city))

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")