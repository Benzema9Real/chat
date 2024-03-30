# Generated by Django 5.0.3 on 2024-03-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField(verbose_name='id: ')),
                ('author_name', models.CharField(max_length=50, verbose_name='Пользователь: ')),
                ('author_email', models.EmailField(max_length=254, verbose_name='Email: ')),
                ('message_text', models.TextField(verbose_name='Сообщение: ')),
                ('date_posted', models.DateTimeField(verbose_name='Дата публикации: ')),
            ],
        ),
    ]
