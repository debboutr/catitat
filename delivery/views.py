from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize

from .models import Rivers
from catitat.settings import KEEP


class HomePageView(TemplateView):
    template_name = 'index.html'


def river_datasets(request):
    rivers = serialize('geojson', Rivers.objects.filter(streamorde__gt=4))
    return HttpResponse(rivers, content_type='json')

class PlaygroundView(TemplateView):
    template_name = 'base.html'