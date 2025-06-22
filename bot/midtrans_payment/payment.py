# bot/midtrans_payment/payment.py
from dotenv import load_dotenv
from datetime import datetime
import os
import requests
import base64
import random

load_dotenv()
KEY = os.getenv("MIDTRANS_KEY")

def create_auth_header():
    auth_string = f"{KEY}:"
    base64_auth_string = base64.b64encode(auth_string.encode()).decode()
    return f"Basic {base64_auth_string}"

def create_midtrans_payment_link(user_id, username, nominal, no_hp, total_price):
    order_id = f"{random.randint(10000,99999)}-PULSA-{nominal.replace('.', '')}-{no_hp}"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": create_auth_header()
    }

    payload = {
        "transaction_details": {
            "order_id": order_id,
            "gross_amount": total_price
        },
        "item_details": [
            {
                "id": "pulsa",
                "price": total_price,
                "quantity": 1,
                "name": f"1x Pulsa {nominal} ke {no_hp}"
            }
        ],
        "customer_details": {
            "first_name": f"{username or 'User'}",
            "email": f"user{user_id}@example.com"
        },
        "usage_limit": 1,
        "expiry": {
            "start_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S %z'),
            "duration": 20,
            "unit": "minutes"
        }
    }

    response = requests.post("https://api.sandbox.midtrans.com/v1/payment-links", headers=headers, json=payload)

    if response.json():
        return response.json().get("payment_url"), order_id
    else:
        return None, None