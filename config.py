# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25354710"))
API_HASH = os.environ.get("API_HASH", "aaf91c6dbf69dbe0a5e2350360ca18a0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6115789527:AAH4lkl1gWoBbz3gu0L53zBX_oF09yVEgCw")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1834587403")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cynite")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Mybot:<password>@cluster0.nw3eqvu.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1834587403")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001822614989")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "shortnerfly") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
