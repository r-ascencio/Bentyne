from django.db import models
from django.template.defaultfilters import slugify
from skylark.utils import TEMPLATES
from mptt.models import MPTTModel, TreeForeignKey


class Page(MPTTModel):
    title = models.CharField(max_length=100, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=True,
            blank=False, null=False)
    slug = models.SlugField(editable=False)
    template = models.CharField(max_length=100,
            help_text="Your templates for example: 'page/content.html'",
            choices=TEMPLATES)
    published = models.BooleanField(default=True)
    url = models.CharField(max_length=500, editable=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    body = models.TextField('Main Content', null=True, blank=True)


    class MPTTMeta:
        order_insertion_by = ['title']
        level_attr = 'mptt_level'

    def __unicode__(self):
           return '%s' % (self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            brothers = self.get_siblings()
            p = 1
            while brothers.filter(slug=self.slug).exists():
                p += 1
                self.slug = slug + '-%d' % p
            if self.parent:
                self.url = '%s/%s' % (self.parent.slug, self.slug)
            else:
                self.url = self.slug
        super(Page, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('cheryl.views.page', [str(self.url)])






class Content(models.Model):
    title = models.CharField(max_length=100, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=True,
            blank=False, null=False)
    body = models.TextField()
    slug = models.SlugField(editable=False)
    page = models.ForeignKey(Page, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.title


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Content, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('cheryl.views.see_content', [str(self.title)])

class PageSettings(models.Model):
    index_page = models.ForeignKey(Page,
            limit_choices_to = {'mptt_level__lte': 0},
            null=True, blank=True)
