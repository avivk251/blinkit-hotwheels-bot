import requests

BOT_TOKEN = "8944227127:AAFzNEzvnMUDWrr6jcSHLHBPys5_W85YbN8"
CHAT_ID = "8966437145"

URL = "https://blinkit.com/s/?q=hot%20wheels"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def send_telegram(message):

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(telegram_url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

    print("Telegram response:")
    print(response.text)

print("Starting bot...")

response = requests.get(URL, headers=headers)

print("Blinkit status code:")
print(response.status_code)

print("First 500 characters:")
print(response.text[:500])

send_telegram("✅ GitHub bot is running successfully")
