from django.db import models


class Message(models.Model):
    chat_id = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chat_id}:{self.user_id} @ {self.timestamp}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    keywords = models.JSONField(default=list)  # список ключевых слов

    def __str__(self):
        return self.name


class StandardAnswer(models.Model):
    trigger = models.CharField(max_length=100)  # команда или ключевое слово
    response = models.TextField()

    def __str__(self):
        return self.trigger


class CRMRequest(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('error', 'Error'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CRMRequest for Msg {self.message.id}: {self.status}"

