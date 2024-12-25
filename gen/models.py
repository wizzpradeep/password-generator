from django.db import models

# Create your models here.
class Password(models.Model):
    password = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']