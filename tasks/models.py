from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title