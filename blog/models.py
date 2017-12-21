from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='article-images',default='article-images/default.png')
    details = models.TextField()
    review = models.TextField()
    id = models.AutoField(primary_key=True)

class comments(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    def __str__(self):
        return self.name