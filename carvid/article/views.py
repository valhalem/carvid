# Create your views here.
from django.shortcuts import render_to_response
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
    return render_to_response( 'tags.html', 
            {'articles' : articles_by_tag,})

def tags_search(request, tag):
    try:
        by_tag = Article.objects.filter(tags__name__in=[tag]).order_by('-pub_date')[0]
    except IndexError:
        raise Http404
    return render_to_response( 'tag_list.html',
            { 'list': by_tag,
              'title': by_tag.video_url ,
              'lead': by_tag.pub_date, })
