from oriel.models import Picture, Gallery
from django.views.generic import CreateView, DeleteView


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core.urlresolvers import reverse

from django.conf import settings
from django.forms import ModelForm

from django.contrib.auth.decorators import login_required

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery

def gallery_list(request):
    galleries = Gallery.objects.all();
    if galleries.count() > 0:
        return render_to_response('oriel/gallery_list.html', {'galleries':galleries})
    else:
        return HttpResponseRedirect('/skylark/oriel/add/')


def view_gallery(request, slug):
    gallery = Gallery.objects.get(slug=slug)
    images = gallery.picture_set.all()
    return render_to_response('oriel/gallery_edit.html', {'images':images,
        'gallery': gallery})


def show_gallery(request, slug):
    gallery = Gallery.objects.get(slug=slug)
    images = gallery.picture_set.all()
    return render_to_response('oriel/gallery_show.html', {'images':images,
        'gallery': gallery})

def add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/skylark/oriel/')
    else:
        form = GalleryForm()

    return render_to_response('oriel/form.html', {'form': form},
            context_instance=RequestContext(request))



def edit_gallery(request, id):
    gal = Gallery.objects.get(id=id)
    data = {'name': gal.name,
            'slug': gal.slug,
            }
    form = GalleryForm(initial=data)
    if request.method == 'POST':
        form = GalleryForm(request.POST, instance=gal)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/skylark/oriel/')
    else:
        data = {'name': gal.name,
                'slug': gal.slug,
                }
        form = GalleryForm(initial=data)

    return render_to_response('oriel/form.html', {'form': form},
            context_instance=RequestContext(request))




class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ('name','description','gal')


def edit_picture(request, id):
    picture = Picture.objects.get(id=id)
    data = {'name': picture.name,
            'slug': picture.slug,
            'description': picture.description,
            'slug': picture.slug,
            'file': picture.file,
            'gal': picture.gal
            }
    form = PictureForm(initial=data)
    if request.method == 'POST':
        form = PictureForm(request.POST, instance=picture)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/skylark/oriel/')
    else:
        data = {'name': picture.name,
                'slug': picture.slug,
                'description': picture.description,
                'slug': picture.slug,
                'file': picture.file,
                'gal': picture.gal,
                }
        form = PictureForm(initial=data)

    return render_to_response('oriel/form.html', {'form': form},
                context_instance=RequestContext(request))


def delete_picture(request, id):
    picture = Picture.objects.get(id=id)
    picture.delete()
    return HttpResponseRedirect('/skylark/oriel/')


def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"


class PictureCreateView(CreateView):
    model = Picture
    context_objects_name = "gallery"

    def get_queryset(self):
         return Gallery.objects.get(slug=self.kwargs['slug'])


    def get_context_data(self, **kwargs):
        context = super(PictureCreateView, self).get_context_data(**kwargs)
        context['gal'] = Gallery.objects.get(slug=self.kwargs['slug'])
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.gal = Gallery.objects.get(slug=self.kwargs['slug'])
        self.object.save()
        f = self.request.FILES.get('file')
        data = [{'name': f.name, 'url': settings.MEDIA_URL + "gallery/" + self.object.gal.slug + "/" + f.name.replace(" ", "_"), 'thumbnail_url': settings.MEDIA_URL + "gallery/" + self.object.gal.slug + "/" + f.name.replace(" ", "_"), 'delete_url': reverse('upload-delete', args=[self.object.id]), 'delete_type': "DELETE"}]
        response = JSONResponse(data, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class PictureDeleteView(DeleteView):
    model = Picture

    def delete(self, request, *args, **kwargs):
        """
        This does not actually delete the file, only the database record.  But
        that is easy to implement.
        """
        self.object = self.get_object()
        self.object.delete()
        if request.is_ajax():
            response = JSONResponse(True, {}, response_mimetype(self.request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
        else:
            return HttpResponseRedirect('/upload/new')

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
        content = simplejson.dumps(obj,**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)
