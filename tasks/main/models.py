from django.db import models


class Performer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    choices = (
        (1, 'Low'),
        (2, 'Moderate'),
        (3, 'High'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    priority = models.IntegerField(choices=choices, default=1)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
