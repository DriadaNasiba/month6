from celery import shared_task
from celery import Celery
import time

@shared_tasks
def send_otp_email(user_email,code):
    print("Sending...")
    time.sleep(20)
    print("Email sent")
@shared_task()
def sent_daily_report():
    print("sending daily repost")
    time.sleep(50)
    print("daily report sent")


app = Celery('my_app', broker='redis://localhost:6379/0')

@app.task
def save_user_data(user_id, data):
    # Имитация сохранения в БД с задержкой
    time.sleep(5)
    print(f"User {user_id} data saved: {data}")
    return True


@app.task
def clean_temp_files():
    print("Cleaning temporary files...")

