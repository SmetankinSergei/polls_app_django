from django.urls import path

from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('poll/', views.poll, name='poll'),
]
