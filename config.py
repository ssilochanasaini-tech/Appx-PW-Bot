import os

api_id = int(os.environ.get("API_ID", 36237546))
api_hash = os.environ.get("API_HASH", "6f01984353006ed4bb09e8fd1ff5c2af")
bot_token = os.environ.get("BOT_TOKEN", "8994153594:AAGQdH8yKxufLRBqA8kRFTEHFcxiGTZ5db4")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "8852146747").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")
