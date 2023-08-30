from django.db import models


class Article(models.Model):
   title = models.CharField(max_length=120)
   description = models.CharField(max_length=200)
   body = models.TextField()
   img = models.FileField(upload_to="news_img/")
   publication_date = models.DateField()
   img_url = img

   def __str__(self):
       return f"{ self.title }"