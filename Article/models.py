from django.db import models

class Article(models.Model):
    discipline = models.CharField(max_length=100)
    discipline_id = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    article = models.TextField()
    number_ext = models.IntegerField()
    paragraphs = models.IntegerField()

    def __str__(self):
        return self.subject