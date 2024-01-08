from django.urls import path
from authenticate import views

urlpatterns = [path("", views.signup, name="signup")]
