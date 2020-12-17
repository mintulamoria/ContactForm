from django.urls import path
from . import views
from .views import Contact

app_name = 'home'

urlpatterns = [

	path('', views.contact_new, name='contact_list'),
	path('', views.Contact, name='contact'),

]