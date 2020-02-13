from django.conf import settings
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]