from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
class Message_Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='فرستنده',related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="private_received",verbose_name='گیرنده')
    text=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} --- {self.text}--- {self.timestamp}'
