"""
Definition of models.

python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

django-admin makemessages --locale=uk --extension=html

django-admin compilemessages
"""

from django.db import models


#Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    title_ua = models.CharField(max_length=255)
    text = models.TextField()
    text_ua = models.TextField()
    image = models.ImageField(upload_to='news')

    class Meta:
        managed = True
        db_table = 'News'
