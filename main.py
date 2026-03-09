import threading
import crypto_hedj
from fastapi import FastAPI

app = FastAPI()
bot_thread = None

@app.on_event("startup")
def start_bot():
    global bot_thread
    if not bot_thread:
        bot_thread = threading.Thread(target=crypto_hedj.main, daemon=True)
        bot_thread.start()

@app.get("/")
def root():
    return {"status": "Crypto bot is running on Railway!"}

@app.get("/health")
def health():
    return {"status": "ok"}
