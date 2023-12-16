from django.db import models

from model_utils.models import TimeStampedModel, SoftDeletableModel


class Post(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(
        max_length=150
    )
    text = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
