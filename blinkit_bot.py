import requests

BOT_TOKEN = "8944227127:AAFzNEzvnMUDWrr6jcSHLHBPys5_W85YbN8"
CHAT_ID = "8966437145"

URL = "https://blinkit.com/v1/layout/search?q=hot%20wheels&search_type=type_to_search"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://blinkit.com/",
    "Origin": "https://blinkit.com"
}

def send_telegram(message):

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(telegram_url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

print("Checking Blinkit API...")

response = requests.get(URL, headers=headers)

print("Status code:", response.status_code)

if response.status_code != 200:

    print("Blocked by Blinkit")

    send_telegram(f"⚠️ Blinkit blocked request. Status: {response.status_code}")

    exit()

data = response.json()

response_text = str(data)

keywords = [
    "skyline",
    "supra",
    "gtr",
    "nissan",
    "hot wheels"
]

products_found = []

for keyword in keywords:

    if keyword.lower() in response_text.lower():
        products_found.append(keyword)

if products_found:

    message = "🔥 Hot Wheels Match Found:\n\n"

    for item in products_found:
        message += f"• {item}\n"

    send_telegram(message)

else:

    send_telegram("ℹ️ Bot ran successfully but no matches found")
