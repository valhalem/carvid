from django.db import models

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
    video_url = models.CharField(max_length=100)

