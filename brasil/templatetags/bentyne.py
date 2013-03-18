from cheryl.models import Content
from django.views.decorators.csrf import csrf_protect
from django.template import Library, Node
from django.db.models import get_model
from cheryl.models import Page
from brasil.models import Post
from skylark.models import Settings, SettingsBlog, ContactSettings
from oriel.models import Gallery
# from django.template.loader import add_to_builtins




register = Library()

class LatestContentNode(Node):
    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))

    def render(self, context):
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''

def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
    return LatestContentNode(bits[1], bits[2], bits[4])

get_latest = register.tag(get_latest)


# @csrf_protect
def content(context, title):
    try:
        content = Content.objects.get(title__iexact=title)
    except:
        content = Content()
        content.title = title
        content.body = 'New content whit title: '+ content.title +' created modify here or signin for changue this'
        content.save()
    return {'content': content,
            'request': context['request'],
            }

def site_name():
    try:
        site = Settings.objects.get(id=1)
        site_name = site.site_name
    except:
        site_name = 'Bentyne'
    return site_name

register.simple_tag(site_name)

def blog_name():
    try:
        blog = SettingsBlog.objects.get(id=1)
        blog_title = blog.blog_title
    except:
        blog_title = 'Blog'
    return blog_title

register.simple_tag(blog_name)


def blog_description():
    try:
        blog = SettingsBlog.objects.get(id=1)
        blog_description = blog.blog_description
    except:
        blog_description = 'This is a blog in Bentyne CMS'
    return blog_description

register.simple_tag(blog_description)


def blog_url():
    try:
        blog = SettingsBlog.objects.get(id=1)
        blog_url = blog.blog_url
    except:
        blog_url = '/blog/'
    return blog_url

register.simple_tag(blog_url)


def contact_url():
    try:
        contact = ContactSettings.objects.get(id=1)
        contact_url = contact.url
    except:
        contact_url = '/contact/'
    return contact_url

register.simple_tag(contact_url)


def tree_menu(rootclass='root', menuclass='menu', childrenclass='children'):
    nodes = Page.objects.all()
    return {'nodes': nodes, 'rootclass': rootclass,
            'childrenclass':childrenclass,
            'menuclass': menuclass}

def root_menu(rootclass='root'):
    nodes = Page.objects.all()
    return {'nodes': nodes, 'rootclass': rootclass}

def page_menu(title='index', rootclass='root', menuclass='menu', childrenclass='children'):
    nodes = Page.objects.get(title__exact=title).get_children()
    return {'nodes': nodes, 'rootclass': rootclass,
            'childrenclass':childrenclass,
            'menuclass': menuclass}

def image_grid(gallery):
    gallery = Gallery.objects.get(name__exact=gallery)
    gallery_pictures = galery.picture_set.all()
    return {'gallery': gallery,
            'pictures': gallery_pictures}


def gallery_grid(gallery):
    gallery = Gallery.objects.get(name__exact=gallery)
    gallery_pictures = gallery.picture_set.all()
    return {'gallery': gallery,
            'pictures': gallery_pictures}

def gallery_slider(gallery, theme="default"):
    gallery = Gallery.objects.get(name=gallery)
    gallery_pictures = gallery.picture_set.all()
    return {'gallery': gallery,
            'pictures': gallery_pictures,
            'theme': theme}

def gallery_show(gallery):
    gallery = Gallery.objects.get(name__exact=gallery)
    gallery_pictures = gallery.picture_set.all()
    return {'gallery': gallery,
            'pictures': gallery_pictures}


def posted_lately(n="3"):
    try:
        posts = Post.objects.all().order_by('-creation_date')[:n]
    except:
        posts = Post.objects.all().order_by('-creation_date')[:3]
    return {'posts': posts}

def social_buttons(context):
    url = context['request']
    url = url.build_absolute_uri()
    return {'url': url }


register.inclusion_tag('posts_load.html')(posted_lately)
register.inclusion_tag('tree_menu.html')(tree_menu)
register.inclusion_tag('root_menu.html')(root_menu)
register.inclusion_tag('tree_menu.html')(page_menu)
register.inclusion_tag('gallery_slider.html')(gallery_slider)
register.inclusion_tag('gallery_show.html')(gallery_show)
register.inclusion_tag('gallery_grid.html')(gallery_grid)
register.inclusion_tag('get_content.html', takes_context=True)(content)
register.inclusion_tag('social_buttons.html',  takes_context=True )(social_buttons)
