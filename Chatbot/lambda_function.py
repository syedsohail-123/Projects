import json
import urllib.request
import os
import traceback

# ─── Load Bot Token ────────────────────────────────────────────────
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    raise Exception("Missing TELEGRAM_TOKEN environment variable")

TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

# ─── Static Question-Answer Pairs ──────────────────────────────────
qa_pairs = {
    "what is the capital of india": "The capital of India is New Delhi.",
    "who is the prime minister of india": "The Prime Minister of India is Narendra Modi.",
    "what is aws": "AWS stands for Amazon Web Services. It's a cloud computing platform.",
    "what is your name": "I'm your helpful Telegram bot!",
    "how are you": "I'm a Lambda function, so I'm always up 😄"
}

# ─── Answer Lookup ─────────────────────────────────────────────────
def get_answer(user_text):
    user_text = user_text.strip().lower()
    for question, answer in qa_pairs.items():
        if question in user_text:
            return answer
    return "Sorry, I don't know the answer to that yet."

# ─── Send Message to Telegram ──────────────────────────────────────
def send_telegram_message(chat_id, text):
    try:
        data = {
            'chat_id': chat_id,
            'text': text
        }

        headers = {
            'Content-Type': 'application/json'
        }

        req = urllib.request.Request(
            TELEGRAM_API,
            data=json.dumps(data).encode('utf-8'),
            headers=headers
        )

        with urllib.request.urlopen(req) as response:
            result = response.read().decode()
            print("✅ Telegram API response:", result)

    except urllib.error.HTTPError as e:
        print("⚠ Telegram returned error:", e.code, e.reason)
        print("📨 Telegram Response Body:", e.read().decode())
        # Don't raise again — just log and move on

    except Exception as e:
        print("❌ Unexpected error:", str(e))
        traceback.print_exc()
        # Don't raise again — just log and move on

# ─── Lambda Handler ────────────────────────────────────────────────
def lambda_handler(event, context):
    try:
        print("📥 Incoming event:", json.dumps(event))

        # 1. Extract and parse the body
        if 'body' not in event:
            raise Exception("Missing 'body' in event")

        body = json.loads(event['body'])
        print("📦 Parsed body:", body)

        # 2. Extract chat_id and user message
        chat_id = body['message']['chat']['id']
        text = body['message'].get('text', '')
        print(f"🗣 User: {text} | Chat ID: {chat_id}")

        # 3. Get bot's reply
        answer = get_answer(text)
        print(f"🤖 Bot Reply: {answer}")

        # 4. Send reply to Telegram
        send_telegram_message(chat_id, answer)

        # ✅ Respond with 200 if all is good
        return {
            'statusCode': 200,
            'body': json.dumps('Message processed')
        }

    except Exception as e:
        print("❌ Lambda Exception:", str(e))
        traceback.print_exc()
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error')
        }
