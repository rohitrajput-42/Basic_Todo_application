from django.db import models

class Task(models.Model):

    title = models.CharField(max_length = 2000)
    complete = models.BooleanField(default = False, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title