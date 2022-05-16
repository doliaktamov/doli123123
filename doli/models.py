from cgitb import text
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    text = models.CharField(max_length=255)
    date_publicate = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
