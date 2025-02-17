from yookassa import Configuration,  Payment
import requests
import json
from config import TOKEN

Configuration.account_id = "1035226"
Configuration.secret_key = "test_-WMlgZy1q9rlbwK7r-deevIrTsZeH5IfqYZEgPKmN5k"


import uuid

async def create_payment(value, description, user_id):
    idempotence_key = str(uuid.uuid4())
    try:
        payment = Payment.create({
            "amount": {
                "value": f"{value}",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://www.example.com/return_url"
            },
            "capture": True,
            "description": f"{description}"
        }, idempotence_key)
        print(payment)
        payment_id = payment.id
        confirmation_url = payment.confirmation.confirmation_url  # Получаем ссылку на оплату
        print(f"Успешно создан платеж с ID: {payment_id}")
        print(f"Ссылка на оплату: {confirmation_url}{user_id}")
        return payment
        # Отправьте ссылку на оплату пользователю (например, в Telegram-боте)

    except Exception as e:
        print(f"Ошибка при создании платежа: {e}")

def check_payment_status(payment_id: str):
    """Проверяет статус платежа по его ID."""
    try:
        payment = Payment.find_one(payment_id)
        return payment.status #  Возвращаем статус платежа (succeeded, pending, canceled)
    except Exception as e:
        print(f"Ошибка при проверке статуса платежа: {e}")
        return None


