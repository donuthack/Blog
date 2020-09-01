from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
    author = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    article = models.TextField(null=False, max_length=255)
    publication_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.author)
