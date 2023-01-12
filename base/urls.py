from django.urls import path
from . import views
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView, statPage


urlpatterns = [
    path('', views.indexPage, name='index-page'),

    path('predictor/', views.predictor, name = 'predictor'),

    path('welcome/', views.welcomePage, name = 'welcome-page'),
    
    path('welcome/disclaimer/', views.disclaimerPage, name = 'disclaimer-page'),

    path('', views.declinePage, name = 'decline'),

    path('welcome/disclaimer/accept', views.acceptPage, name = 'accept-page'),

    path('vct/', views.vctPage, name = 'vct-page'),

    path('nutrition/', views.nutritionPage, name = 'nutrition-page'),

    path('image/', views.imagePage, name = 'image-page'),

    path('index-2/',  HomeTemplateView.as_view(), name="home"),

    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),

    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),

    path("stat-page/", statPage, name="stat-page"),

    path('predictor/message/', views.MsgPage, name = 'message-page'),

    path('predictor/message/sent/', views.sent, name="sent"),
]
