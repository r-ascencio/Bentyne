from brasil.models import Post
from taggit.models import Tag

from django import Template

register = Template.Library()



@regiter.tag(name='load_posts')
def do_load_posts(parser, token):
    return AllPosts()

