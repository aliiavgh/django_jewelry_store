from django.core.mail import send_mail
from config.celery import app
from applications.mailing.models import Spam


@app.task
def send_spam_emails():
    emails = Spam.objects.all()
    send_mail(
            'Hello, this is a jewerly store!',
            'Do not miss the opportunity to buy jewerly at low prices: http://localhost:8000/api/v1/product/',
            'aliyakomanovaa@gmail.com',
            [em.email for em in emails]
        )
