from django.urls import path
from . import views
from .views import Home, MessageView, statPage, ResultPage


urlpatterns = [
    path('', Home.as_view(), name='main'),

    path('stat-page/', statPage, name='stat-page'),

    path('vct/', views.vctPage, name='vct-page'),

    path('nutrition/', views.nutritionPage, name='nutrition-page'),

    path('welcome/', views.welcomePage, name='welcome-page'),

    path('welcome/disclaimer/', views.disclaimerPage, name='disclaimer-page'),

    path('predictor/', views.predictor, name='predictor'),

    # path('predictor/result/', ResultPage.as_view(), name='result'),

    path('predictor/result/', views.getResult, name='get-result'),

    path('message/', MessageView.as_view(), name='message'),
]
