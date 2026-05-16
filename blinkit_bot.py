import requests

BOT_TOKEN = "8944227127:AAFzNEzvnMUDWrr6jcSHLHBPys5_W85YbN8"
CHAT_ID = "8966437145"

SEARCH_WORD = "Hot Wheels"

URL = "https://blinkit.com/s/?q=hot%20wheels"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def send_telegram(message):

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(telegram_url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

response = requests.get(URL, headers=headers)

html = response.text

print("Checking Blinkit...")

if SEARCH_WORD.lower() in html.lower():

    print("Found Hot Wheels!")

    send_telegram("🔥 Hot Wheels detected on Blinkit!")

else:

    print("Not found")