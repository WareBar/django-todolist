from django.db import models

# Create your models here.


class Tasks(models.Model):
    todo = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.todo