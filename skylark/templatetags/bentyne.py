from cheryl.models import Content
from django import template
from django.template import Library, Node
from django.db.models import get_model
from cheryl.models import Page
from oriel.models import Gallery

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


register_template = template.Library()

def content(title):
    content = Content.objects.get(title__exact=title)
    return {'content': content}


def tree_menu(rootclass='root', menuclass='menu', childrenclass='children'):
    nodes = Page.objects.all()
    return {'nodes': nodes, 'rootclass': rootclass,
            'childrenclass':childrenclass,
            'menuclass': menuclass}

def root_menu(rootclass='root'):
    nodes = Page.objects.all()
    return {'nodes': nodes, 'rootclass': rootclass}

def page_menu(title='index', rootclass='root', menuclass='menu', childrenclass='children'):
    nodes = Page.objects.get(title__exact=title)
    return {'nodes': nodes, 'rootclass': rootclass,
            'childrenclass':childrenclass,
            'menuclass': menuclass}

def image_grid(gallery):
    gallery = Gallery.objects.get(title__exact=gallery)
    gallery_pictures = galery.picture_set.all()
    return {'gallery': gallery,
            'pictures': gallery_pictures}


def gallery_grid(gallery):
    gallery = Gallery.objects.get(title__exact=gallery)
    gallery_pictures = gallery.picture_set.all()
    return {'gallery': gallery,
            'pictures': gallery_pictures}

def gallery_slider(gallery, theme='default'):
    gallery = Gallery.objects.get(title__exact=gallery)
    gallery_pictures = gallery.picture_set.all()
    return {'gallery': gallery,
            'pictures': gallery_pictures
            'theme': theme}

def gallery_show(gallery):
    gallery = Gallery.objects.get(title__exact=gallery)
    gallery_pictures = gallery.picture_set.all()
    return {'gallery': gallery,
            'pictures': gallery_pictures}


register_template.inclusion_tag('tree_menu.html')(tree_menu)
register_template.inclusion_tag('root_menu.html')(root_menu)
register_template.inclusion_tag('tree_menu.html')(page_menu)
register_template.inclusion_tag('get_content.html')(content)
register_template.inclusion_tag('gallery_slider.html')(gallery_slider)
register_template.inclusion_tag('gallery_show.html')(gallery_show)
register_template.inclusion_tag('gallery_grid.html')(gallery_grid)
