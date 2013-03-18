from django.db import models
from django.template.defaultfilters import slugify


def gallery_file_name(instance, filename):
        return '/'.join(['gallery', instance.gal.slug, filename])

class Gallery(models.Model):
    name =  models.CharField(max_length=100)
    slug = models.SlugField(editable=False, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Gallery, self).save(*args, **kwargs)

class Picture(models.Model):

    # This is a small demo using just two fields. The slug field is really not
    # necessary, but makes the code simpler. ImageField depends on PIL or
    # pillow (where Pillow is easily installable in a virtualenv. If you have
    # problems installing pillow, use a more generic FileField instead.

    #file = models.FileField(upload_to="pictures")
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file = models.ImageField(upload_to=gallery_file_name)
    gal = models.ForeignKey(Gallery, null=True, blank=True)
    slug = models.SlugField(max_length=50, blank=True)

    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Picture, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(False)
        super(Picture, self).delete(*args, **kwargs)
