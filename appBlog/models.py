from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    e_mail = models.EmailField()

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=90)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


