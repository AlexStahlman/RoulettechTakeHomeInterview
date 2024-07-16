from django.urls import path
from . import views
from .views import SubmitContactFormView

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('greetings-traveler/', views.greetings_traveler, name='greetings_traveler'),
    path('submit_contact_form/', SubmitContactFormView.as_view(), name='submit_contact_form'),

]