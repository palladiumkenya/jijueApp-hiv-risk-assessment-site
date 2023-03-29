from django.urls import path
from . import views
from .views import HomeAppointment, AppointmentTemplateView, ManageAppointmentTemplateView


urlpatterns = [
    path('appointment',  HomeAppointment.as_view(), name='home'),

    path('make-an-appointment/',
         AppointmentTemplateView.as_view(), name='appointment'),

    path('manage-appointments/',
         ManageAppointmentTemplateView.as_view(), name='manage'),

]
