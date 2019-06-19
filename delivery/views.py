from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize

from .models import Rivers, States


class HomePageView(TemplateView):
    template_name = 'index.html'


def river_datasets(request):
    rivers = serialize('geojson', Rivers.objects.filter(streamorde__gt=4))
    return HttpResponse(rivers, content_type='json')
    
class StateView(TemplateView):
    template_name = 'state.html'

def state_datasets(request):
    states = serialize('geojson', States.objects.all())
    return HttpResponse(states, content_type='json')

class PlaygroundView(TemplateView):
    template_name = 'base.html'