from django.db import models
from taggit.managers import TaggableManager
from thumbs import ImageWithThumbsField

try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO

# Create your models here.

CATEGORY = [
        (1, 'Europa'),
        (2, 'Azja'),
        (3, 'Afryka'),
        (4, 'Australia'),
        (5, 'Ameryka'),
        ]

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Tytul')
    lead = models.CharField(max_length=100, verbose_name='Lead')
    pub_date = models.DateTimeField('Data publikacji')
    votes = models.IntegerField()
    category = models.IntegerField(max_length=1, db_index=True, choices=CATEGORY, default=None, verbose_name='Kategoria' )
    video_url = models.URLField()
    nickname = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    tags = TaggableManager()
    photo = ImageWithThumbsField(upload_to='images', sizes=((125,125),(200,200)))
    #second_photo = ImageWithThumbsField(upload_to='images')

    def __unicode__(self):
	    return self.title

