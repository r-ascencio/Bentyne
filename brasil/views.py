# Create your views here.
from brasil.models import Post
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.exceptions import ObjectDoesNotExist
from skylark.models import SettingsBlog
from django.utils import simplejson as json

try:
    site_settings = SettingsBlog.objects.get(id=1)
    titulo = site_settings.blog_title
except:
    titulo = 'Pulp Fiction Bitches!'
    pass


def blog_index(request):
    posts = Post.objects.filter(published=True).order_by('-id')
    try:
        paginator = Paginator(posts, site_settings.blog_posts)
    except:
        paginator = Paginator(posts, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        posts_pages = paginator.page(page)

    except (EmptyPage, InvalidPage):
        posts_pages = paginator.page(paginator.num_pages)

    context = {
            'posts': posts_pages,
            'titulo': titulo,
            }
    return render_to_response('blog_base.html',
            RequestContext(request, context))


def blog_detail(request, slug):
    detail_post = Post.objects.get(slug=slug)
    return render_to_response('blog_detail.html', {'post': detail_post},
            context_instance=RequestContext(request))

def blog_toggle(request, id):
    detail_post = Post.objects.get(id=id)
    if detail_post.published:
        detail_post.published = False
        detail_post.save()
    else:
        detail_post.published = True
        detail_post.save()

    return HttpResponseRedirect('/skylark/brasil/list/')

def save_inlinedit(request):
    try:
        content_body = json.loads(request.POST['raptor-content'])
        for content in content_body:
            content_current = Post.objects.get(id=content)
            content_current.body = content_body.get(content)
            content_current.save()
            return HttpResponse('saved')
    except:
        response = JSONResponse(request.POST['raptor-content'], {}, response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        print json.dumps(request.POST['raptor-content'])
        return response
