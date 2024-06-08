from django.db import models


class Message(models.Model):
    author_name = models.CharField('Пользователь', max_length=50)
    author_email = models.EmailField('Email')
    message_text = models.TextField('Сообщение')
    date_posted = models.DateTimeField('Дата публикации',auto_now=True)


def __str__(self):
    return self.author_name
