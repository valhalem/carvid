from django.db import models
from taggit.managers import TaggableManager
from django.core.files.base import ContentFile
import Image

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
    video_url = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    tags = TaggableManager()
    image = models.FileField(upload_to='images/')

    def get_thumbnail(self, size = None ):
	base = Image.open(StringIO(chosen_image.image.read()))

	if not size:
		rate = 0.2
		size = base.size
		size = (int(size[0] * rate), int(size[1] * rate))
	base.thumbnail(size)
	thmibnail = StringIO()
	base.save(thumbnail, "PNG")
	thumbnail = ContentFile(thumbnail.getvalue())
	return thumbnail

    def __unicode__(self):
	    return self.title

