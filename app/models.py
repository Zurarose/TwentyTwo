"""
Definition of models.

python manage.py makemigrations
python manage.py migrate
manage.py migrate --run-syncdb

"""

from django.db import models


#Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='news')

    class Meta:
        managed = True
        db_table = 'News'
