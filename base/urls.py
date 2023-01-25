from django.urls import path
from . import views
from .views import Home, HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView, statPage


urlpatterns = [
    path('', Home.as_view(), name='main'),

    path("stat-page/", statPage, name="stat-page"),

    path('vct/', views.vctPage, name='vct-page'),

    path('nutrition/', views.nutritionPage, name='nutrition-page'),

    path('welcome/', views.welcomePage, name='welcome-page'),

    path('welcome/disclaimer/', views.disclaimerPage, name='disclaimer-page'),

    path('predictor/', views.predictor, name='predictor'),

    path('predictor/message/', views.sent, name="sent"),

    path('index-2/',  HomeTemplateView.as_view(), name="home"),

    path("make-an-appointment/",
         AppointmentTemplateView.as_view(), name="appointment"),

    path("manage-appointments/",
         ManageAppointmentTemplateView.as_view(), name="manage"),



    # path('predictor/message/', views.MsgPage, name = 'message-page'),



    # path('sent/', PredictorTemplateView.as_view(), name='send_result')
]
