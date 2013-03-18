import os
from django.conf import settings
from skylark.models import Settings

try:
    conf = Settings.objects.get(id=1)
except:
    pass

def get_templates():
    try:
        dirt = os.path.join(settings.PROJECT_ROOT, 'themes', conf.site_theme)
    except:
        dirt = os.path.join(settings.PROJECT_ROOT, 'themes', 'default')

    for t in os.listdir(dirt):
        if os.path.basename(t) != 'static':
            if os.path.basename(t) != '__init__.py':
                if os.path.basename(t) != '__init__.pyc':
                    if os.path.basename(t) != '404.html':
                        if os.path.basename(t) != '505.html':
                            yield t

TEMPLATES = tuple( (t, t) for t in get_templates())
