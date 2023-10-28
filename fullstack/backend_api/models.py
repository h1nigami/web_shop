from django.db import models
from django.contrib.auth.models import User

class Bots(models.Model):
    owner = models.OneToOneField(User, verbose_name=("Владелец"), on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=("Название"))
    token = models.CharField(max_length=100, verbose_name=("Токен"))
    class Meta:
        verbose_name = ("Бот")
        verbose_name_plural = ("Боты")
        
    def __str__(self):
        return self.name
