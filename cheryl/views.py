# Create your views here.
from cheryl.models import Page
from cheryl.models import Content
from oriel.views import JSONResponse
from oriel.views import response_mimetype
from cheryl.forms import PageForm, ContentForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.utils import simplejson as json

def page(request, page_url=None):
    page = get_object_or_404(Page, url=page_url)
    try:
        get_template(page.template)
        template = page.template
        t_existe = True
    except:
        template = 'default.html'
        t_existe = False

    try:
        contents = page.content_set.all()
    except:
        contents = ''
    context = {
            'contents': contents,
            'title': page.title,
            'page': page,
            'user': request.user,
            }

    return render_to_response(template,
            RequestContext(request, context))


def index(request):
    try:
        index = Page.objects.get(slug__exact='index')
        context = {
                'contents': index.content_set.all(),
                'title': index.title,
                'page': index,
                }
        if index.template:
            template = index.template
        else:
            template = 'default.html'
        return render_to_response(template,
                RequestContext(request, context))
    except:
        template = 'default.html'
        return render_to_response(template)




def index_pages(request):
    return render_to_response('cheryl/page.html',
            {'nodes': Page.objects.all().order_by('title')},
            context_instance=RequestContext(request))


def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/skylark/cheryl/')
    else:
        form = PageForm()

    return render_to_response('cheryl/page_add.html', {'form':form},
            context_instance=RequestContext(request))



def modify_page(request, id):
    page = Page.objects.get(id=id)
    data = {'title': page.title,
            'slug':  page.slug,
            'body': page.body,
            'template': page.template,
            }
    form = PageForm(initial=data)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/skylark/cheryl/')

    else:
        form = PageForm(initial=data)

    return render_to_response('cheryl/page_add.html', {'form': form},
            context_instance=RequestContext(request))


def delete_page(request, id):
    page = Page.objects.get(id=id)
    page.delete()
    return HttpResponseRedirect('/skylark/cheryl/')


def index_content(request):
    contents = Content.objects.all()
    return render_to_response('cheryl/content.html', {'contents': contents})


def add_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/skylark/cheryl/content/')
    else:
        form = ContentForm()

    return render_to_response('cheryl/contentform.html', {'form': form},
            context_instance=RequestContext(request))


def see_content(request, title):
    content = Content.objects.get(title=title)
    return render_to_response('cheryl/content_see.html', {'content': content},
                context_instance=RequestContext(request))



def modify_content(request, id):
    content = Content.objects.get(id=id)
    data = {'title': content.title,
            'slug':  content.slug,
            'body':  content.body,
            'page':  content.page
            }
    form = ContentForm(initial=data)
    if request.method == 'POST':
        form = ContentForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/skylark/cheryl/content/')

    else:
        form = ContentForm(initial=data)

    return render_to_response('cheryl/contentform.html', {'form': form},
                context_instance=RequestContext(request))


def delete_content(request, id):
    content = Content.objects.get(id=id)
    content.delete()
    return HttpResponseRedirect('/skylark/cheryl/content/')


def save_inlinedit(request):
    try:
        content_body = json.loads(request.POST['raptor-content'])
        for content in content_body:
            content_current = Content.objects.get(id=content)
            content_current.body = content_body.get(content)
            content_current.save()
            return HttpResponse('saved content')
    except:
        response = JSONResponse(request.POST['raptor-content'], {}, response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        print json.dumps(request.POST['raptor-content'])
        return response
