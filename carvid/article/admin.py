from article.models import Article
from django.contrib import admin
from taggit.models import Tag, TaggedItem

class ArticleAdminView(admin.ModelAdmin):
	date_hierarchy = 'pub_date'
	list_display = ('title','pub_date','video_url')


admin.site.register( Article,ArticleAdminView )
