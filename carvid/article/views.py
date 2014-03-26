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
		'article_video_url': idk.video_url,
        'article_tags' : idk.tags.all(),
        'article_lead': idk.lead ,
        'article_votes': idk.votes,
        'nickname' : idk.nickname ,
        'city' : idk.city ,
        })
	return HttpResponse(td.render(cd))

def tags( request ):
    articles_by_tag = Article.objects.all()
    tt = loader.get_template('tags.html')
    ct = Context({
        'articles': articles_by_tag, })
    return HttpResponse(tt.render(ct))
	
def tags_search(request, tag):
    by_tag = Article.objects.filter(tags__name__in=[tag])
    ty = loader.get_template('tag_list.html')
    tt = Context({ 
        'list': by_tag , 
        'title': by_tag[0].video_url ,
        'lead': by_tag[0].pub_date,

        })
    return HttpResponse(ty.render(tt)) 
