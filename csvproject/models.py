from django.db import models
#for csv file to sqlite3
from django.utils.translation import gettext as _

# Create your models here.
class Book (models.Model):

  title = models.CharField(("title"), max_length=200)
  author=models.CharField(("author"), max_length=200)
  genre=models.CharField(("genre"), max_length=200)
  height=models.PositiveBigIntegerField(("height"))
  publisher=models.CharField(("publisher"), max_length=100)