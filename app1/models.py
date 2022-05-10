from django.db import models

class TODO(models.Model):
    title = models.CharField(max_length = 20)
    time = models.DateTimeField()
    description = models.CharField(max_length = 150)
    status = models.CharField(max_length = 10, choices = (('done', 'done'), ('new', 'new')))

    def __str__(self):
        return self.title