from article.models import Article
from django.contrib import admin

class ArticleAdminView(admin.ModelAdmin):
	date_hierarchy = 'pub_date'
	list_display = ('title','pub_date','video_url')

admin.site.register(Article,ArticleAdminView)
