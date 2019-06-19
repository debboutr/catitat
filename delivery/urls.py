from django.urls import path
from .views import HomePageView, river_datasets, PlaygroundView, StateView, state_datasets

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('county_data/', county_datasets, name='county'),
    path('centroid_data/', river_datasets, name='rivers'),
    path('state_data/', state_datasets, name='state_data'),
    path('playground/', PlaygroundView.as_view(), name='play'),
    path('states/', StateView.as_view(), name='states'),

]
