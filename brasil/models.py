from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django.contrib.comments.moderation import CommentModerator, moderator
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=True,
            blank=False, null=False)
    slug = models.SlugField(editable=False)
    enable_comments = models.BooleanField()
    published = models.BooleanField(default=False)
    body = models.TextField()
    autor = models.ForeignKey(User, blank=True, null=True, editable=False)
    tags = TaggableManager()

    def __unicode__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('brasil.views.blog_detail', [str(self.slug)])

class PostCommentModerator(CommentModerator):
    email_notification = True
    enable_field = 'enable_comments'

moderator.register(Post, PostCommentModerator)
