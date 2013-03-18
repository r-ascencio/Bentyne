from django.conf import settings
from django.db import models
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
import os
# Create your models here.

try:
    site = Site.objects.get(id=1)
except:
    class Site:
        name = 'bad_example'
        domain = 'bad_example.com'
    site = Site()

def get_themes():
    for t in os.listdir(os.path.join(settings.PROJECT_ROOT, 'themes')):
        if os.path.basename(t) != 'static':
            if os.path.basename(t) != '__init__.py':
                if os.path.basename(t) != '__init__.pyc':
                    yield t

THEMES = tuple( (t, t) for t in get_themes())

class Settings(models.Model):
    site_name = models.CharField(max_length=500,
            default=site.name)
    site_domain = models.URLField(default=site.domain)
    site_theme = models.CharField(max_length=100, choices=THEMES)
    def save(self, *args, **kwargs):
        try:
            site = Site.objects.get(id=1)
            site.name = self.site_name
            site.domain = self.site_domain
            site.save()
        except:
            print "shit"
            pass

        super(Settings, self).save(*args, **kwargs)

class SettingsBlog(models.Model):
    blog_url = models.CharField(max_length=100,
            help_text='Should be something like blog/ or foo/blog/',
            default='blog/', null=True, blank=True)
    blog_title = models.CharField(max_length=100, blank=True, null=True)
    blog_description = models.TextField(blank=True, null=True)
    blog_posts = models.IntegerField('Index Post',default=5)


class ContactSettings(models.Model):
    url = models.CharField(max_length=100, default='/')
    succes_url = models.CharField(max_length=100)
    email = models.EmailField(default='to@example.com')
