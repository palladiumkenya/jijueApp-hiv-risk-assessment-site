from django.urls import path
from . import views

# url patterns

urlpatterns = [
    path('appoint', views.counties, name='counties'),
    path('appoint/sub-county', views.sub_counties, name='sub-county'),
    path('appoint/wards', views.wards, name='ward'),

]
