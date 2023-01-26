from django.urls import path
from . import views
from .views import Home, MessageView, HomeAppointment, AppointmentTemplateView, ManageAppointmentTemplateView, statPage, ResultPage


urlpatterns = [
    path('', Home.as_view(), name='main'),

    path('stat-page/', statPage, name='stat-page'),

    path('vct/', views.vctPage, name='vct-page'),

    path('nutrition/', views.nutritionPage, name='nutrition-page'),

    path('welcome/', views.welcomePage, name='welcome-page'),

    path('welcome/disclaimer/', views.disclaimerPage, name='disclaimer-page'),

    path('predictor/', views.predictor, name='predictor'),

    path('predictor/result/', ResultPage.as_view(), name='result'),

    path('message/', MessageView.as_view(), name='message'),

    path('appointment',  HomeAppointment.as_view(), name='home'),

    path('make-an-appointment/',
         AppointmentTemplateView.as_view(), name='appointment'),

    path('manage-appointments/',
         ManageAppointmentTemplateView.as_view(), name='manage'),



    # path('sent/', PredictorTemplateView.as_view(), name='send_result')
]
