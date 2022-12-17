from django.core.mail import send_mail
from config.celery import app


@app.task
def send_activation_email(email, activation_code):
    full_link = f'http://localhost:8000/api/v1/account/activate/{activation_code}'
    send_mail(
        'Activate your account.',
        full_link,
        'aliyakomanovaa@gmail.com',
        [email]
    )


@app.task
def send_password_confirmation_email(email, activation_code):
    send_mail(
        'Use this code to activate the new password.',
        activation_code,
        'aliyakomanovaa@gmail.com',
        [email]
    )