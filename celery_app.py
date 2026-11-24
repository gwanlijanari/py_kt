import os
from celery import Celery
import time

CELERY_BROKER = os.getenv("REDIS_URL")

celery_app = Celery(
    "tasks", broker=CELERY_BROKER, backend=CELERY_BROKER
)


@celery_app.task
def send_welcome_email(email):
    time.sleep(10)
    print(f"Письмо отправили на {email}")
    return 1 / 0
