from django.db import models
from _datetime import datetime

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(default=datetime.now,blank=True)