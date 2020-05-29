from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Duty(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    point_value = models.PositiveIntegerField()

    def __str__(self):
        template ='{0.title} is worth {0.point_value} points!'
        return template.format(self)

    def get_absolute_url(self):
        return reverse('duty_detail', args=[str(self.id)])
