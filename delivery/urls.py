from django.urls import path
from .views import HomePageView, river_datasets

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('county_data/', county_datasets, name='county'),
    path('incidence_data/', river_datasets, name='rivers'),

]
