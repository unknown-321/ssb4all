from django.urls import path
from .import views
urlpatterns = [
    path('signup/', views.handlesignup, name='handlesignup'),
]

