# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from article.models import Article

def index(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render_to_response( 'index.html', { 'articles' : articles })

def article_details(request, article):
    idk = Article.objects.get(pk=article)

    return render_to_response( 'details.html',
            {
		'title': idk.title,
                'id': idk ,
                'video_url': idk.video_url,
                'tags' : idk.tags.names(),
                'lead': idk.lead ,
                'votes': idk.votes,
                'nickname' : idk.nickname ,
                'city' : idk.city , 
		'category' : idk.category,
		'pub_date': idk.pub_date,
		
		})

def tags( request ):
    return render_to_response( 'tags.html', 
            {'tags' : Article.tags.all(),})

def tags_search(request, tag):
    try:
        by_tag = Article.objects.filter(tags__name__in=[tag]).order_by('-pub_date')
    except IndexError:
        raise Http404
    return render_to_response( 'tag_list.html',
            { 
              'list': by_tag ,
              })
"""
def list(request):
    if request.method == 'POST':
	from = ImageForm(request.POST, request.FILES)
	if form.is_valid():
	    newimg = Aricle(imgfile = request.FILES['docfile'])
	    newimg.save()

	    return HttpResponseRedirect(reverse('article.views.list'))
    else:
	form ImageForm()

    images = ImageForm.object.all()

    return render_to_response( 'list.html',
	{ 'documents' : documents, 'form': form },
	context_instance = RequestContext(request)
	)
"""
