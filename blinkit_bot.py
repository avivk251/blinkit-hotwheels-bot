import requests

BOT_TOKEN = "8944227127:AAFzNEzvnMUDWrr6jcSHLHBPys5_W85YbN8"
CHAT_ID = "8966437145"

URL = "https://blinkit.com/v1/layout/search?q=hot%20wheels&search_type=type_to_search"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def send_telegram(message):

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(telegram_url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

    print(response.text)

print("Checking Blinkit API...")

response = requests.get(URL, headers=headers)

print("Status code:", response.status_code)

data = response.json()

products_found = []

response_text = str(data)

keywords = [
    "skyline",
    "supra",
    "gtr",
    "nissan",
    "hot wheels"
]

for keyword in keywords:

    if keyword.lower() in response_text.lower():
        products_found.append(keyword)

if products_found:

    message = "🔥 Hot Wheels Match Found:\n\n"

    for item in products_found:
        message += f"• {item}\n"

    send_telegram(message)

else:

    print("No matching models found")
