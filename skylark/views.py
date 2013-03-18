# Create your views here.
import os
from django.conf import settings as conf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.comments.models import Comment
from skylark.forms import PostForm
from skylark.models import Settings
from skylark.models import SettingsBlog
from skylark.forms import SettingsForm
from skylark.models import ContactSettings
from skylark.forms import SettingsBlogForm
from skylark.forms import SettingsContactForm
from skylark.forms import  SettingsContactForm
from skylark.forms import ContactForm
from brasil.models import Post
from cheryl.models import Page
from taggit.models import Tag
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, BadHeaderError

# from django.core import management
# management.call_command("update_index")

def dashboard(request):
    pages = Page.objects.all().count()
    posts = Post.objects.all().count()
    posts_comments = Comment.objects.all().order_by('-id')[:3]

    return render_to_response('dashboard.html', {'n_posts': posts,
        'n_pages': pages, 'comments': posts_comments}, context_instance=RequestContext(request))


def settings(request):
    if Settings.objects.count() is 0:
        settings = Settings()
        settings.save()
        return HttpResponseRedirect('/skylark/settings/')
    else:
        site_settings = Settings.objects.get(id=1)
        data = {
                'site_name': site_settings.site_name,
                'site_domain': site_settings.site_domain,
                'site_theme': site_settings.site_theme,
                #  'index_page': site_settings.index_page,
                }
        # data_blog = {
        #         'blog_url': blog_settings.blog_url,
        #         'blog_title': blog_settings.blog_title,
        #         }
        form = SettingsForm(initial=data)
        if request.method == 'POST':
            form = SettingsForm(request.POST, instance=site_settings)
            if form.is_valid():
                form.save()
                ## why god why vv'
                # print os.path.join(conf.PROJECT_ROOT, 'bentyne/settings.py')
                fd = os.path.join(conf.PROJECT_ROOT, 'bentyne/urls.py')
                open_settings_for_reload = open(fd, 'a')
                open_settings_for_reload.write('\n#BlogURLChangued')
                open_settings_for_reload.close()
                ## sorry for that stupidity
                return HttpResponseRedirect('/skylark/settings/')
        else:
            data = {
                'site_name': site_settings.site_name,
                'site_domain': site_settings.site_domain,
                'site_theme': site_settings.site_theme,
                # 'blog_url': site_settings.blog_url,
                # 'blog_title': site_settings.blog_title,
                # 'index_page': site_settings.index_page
                }
            form = SettingsForm(initial=data)

            return render_to_response('form.html', {'form': form},
                        context_instance=RequestContext(request))

    return HttpResponseRedirect('/skylark/dashboard/')


def settings_blog(request):
    if SettingsBlog.objects.count() is 0:
        settings = SettingsBlog()
        settings.save()
        return HttpResponseRedirect('/skylark/settings/blog/')
    else:
        site_settings = SettingsBlog.objects.get(id=1)
        data_blog = {
                'blog_url': site_settings.blog_url,
                'blog_title': site_settings.blog_title,
                'blog_description': site_settings.blog_description,
                'blog_posts': site_settings.blog_posts,
                }
        form = SettingsBlogForm(initial=data_blog)
        if request.method == 'POST':
            form = SettingsBlogForm(request.POST, instance=site_settings)
            if form.is_valid():
                form.save()
                ## why god why vv'
                # print os.path.join(conf.PROJECT_ROOT, 'bentyne/settings.py')
                fd = os.path.join(conf.PROJECT_ROOT, 'bentyne/settings.py')
                open_settings_for_reload = open(fd, 'a')
                open_settings_for_reload.write('\n#ThemeChangued')
                open_settings_for_reload.close()
                ## sorry for that stupidity
                return HttpResponseRedirect('/skylark/settings/blog/')
        else:
            data_blog = {
                'blog_url': site_settings.blog_url,
                'blog_description': site_settings.blog_description,
                'blog_posts': site_settings.blog_posts,
                'blog_title': site_settings.blog_title,
                }
            form = SettingsBlogForm(initial=data_blog)

            return render_to_response('form.html', {'form': form},
                        context_instance=RequestContext(request))

    return HttpResponseRedirect('/skylark/settings/blog/')





def post_list(request):
    posts = Post.objects.all().order_by('-creation_date');
    return render_to_response('brasil/post_list.html', {'posts':posts})

def tags_post(request):
    tags = Tag.objects.all().order_by('name')
    return render_to_response('brasil/tags_list.html', {'tags':tags})

def tag_post(request, name):
    posts = Post.objects.filter(tags__name__in=name)
    return render_to_response('brasil/post_list.html', {'posts':posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autor = request.user
            instance.save()
            form.save_m2m()

            return HttpResponseRedirect('/skylark/brasil/list/')
    else:
        form = PostForm()

    return render_to_response('brasil/blog.html', {'form': form},
            context_instance=RequestContext(request))


def edit_post(request, id):
    post = Post.objects.get(id=id)
    data = {'title': post.title,
            'body': post.body,
            'published': post.published,
            'slug': post.slug,
            'autor': post.autor,
            'tags': u'%s' % u','.join(unicode(t) for t in post.tags.all())
            }
    form = PostForm(initial=data)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/skylark/brasil/list/')
    else:
        data = {'title': post.title,
                'body': post.body,
                'published': post.published,
                'slug': post.slug,
                'autor': post.autor,
                'tags': u'%s' % u', '.join(unicode(t) for t in post.tags.all())
                }
        form = PostForm(initial=data)

    return render_to_response('brasil/blog.html', {'form': form,'post':post,},
            context_instance=RequestContext(request))


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/skylark/brasil/list/')



def contact_settings(request):
    if ContactSettings.objects.count() is 0:
        settings = ContactSettings()
        settings.save()
        return HttpResponseRedirect('/skylark/settings/contact/')
    else:
        contact_settings = ContactSettings.objects.get(id=1)
        data_contact = {
                'url': contact_settings.url,
                'succes_url': contact_settings.succes_url,
                'email': contact_settings.email,
                }
        form = SettingsContactForm(initial=data_contact)
        if request.method == 'POST':
            form = SettingsContactForm(request.POST, instance=contact_settings)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/skylark/settings/contact/')
        else:
            data_contact = {
                    'url': contact_settings.url,
                    'succes_url': contact_settings.succes_url,
                    'email': contact_settings.email,
                    }
            form = SettingsContactForm(initial=data_contact)

            return render_to_response('form.html', {'form': form},
                        context_instance=RequestContext(request))

    return HttpResponseRedirect('/skylark/settings/contact/')


def contact_send(request):
    subject = request.POST.get('topic', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')

    try:
        contact = ContactSettings.objects.get(id=1)
    except:
        return HttpResponseRedirect('/skylark/settings/contact/')

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [contact.email])
        except BadHeaderError:
            return HttpResponse("Can't send the email")
        try:
            return HttpResponseRedirect('/%s' % contact.succes_url )
        except:
            return HttpResponseRedirect('/%s' % contact.url)

    else:
        return render_to_response('contact_form.html', {'contact_form': ContactForm() }
                ,RequestContext(request)
                )

    return render_to_response('contact_form.html', {'contact_form': ContactForm()},
            RequestContext(request))


def success_contact(request):
    try:
        contact = ContactSettings.objects.get(id=1)
    except:
        return HttpResponseRedirect('/skylark/settings/contact/')
    return HttpResponseRedirect('/%s' % contact.succes_url)
