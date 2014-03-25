# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, Http404
from article.models import Article

def index(request):
	articles = Article.objects.all().order_by('-pub_date')
	t = loader.get_template('index.html')
	c = Context ({'articles': articles,})
	return HttpResponse(t.render(c))

def article_details(request, article):
	idk = Article.objects.get(pk=article)
	td = loader.get_template('details.html')
	cd = Context({
		'article_title': idk ,
		'article_title2': idk.video_url })
	print idk, article
	return HttpResponse(td.render(cd))
	

