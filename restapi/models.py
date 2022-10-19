from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

