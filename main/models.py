from django.db import models


# Create your models here.
class Question(models.Model):
    content = models.CharField(max_length=256)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content


class Option(models.Model):
    content = models.CharField(max_length=256)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question} - {self.content}"
