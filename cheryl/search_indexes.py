import datetime
from haystack.indexes import *
from haystack import site
from cheryl.models import Page, Content


class PageIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    url = CharField(model_attr='url')
    creation_date = DateTimeField(model_attr='creation_date')
    body = CharField(model_attr='body')

    def index_queryset(self):
        return Page.objects.filter(creation_date__lte=datetime.datetime.now())


site.register(Page, PageIndex)

class ContentIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    creation_date = DateTimeField(model_attr='creation_date')
    body = CharField(model_attr='body')

    def index_queryset(self):
        return Content.objects.filter(creation_date__lte=datetime.datetime.now())


site.register(Content, ContentIndex)
