from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import Contact
#from django.http import HttpResponse

def contact_new(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = ContactForm()
	contacts = Contact.objects.all().order_by('first_name')
	return render(request, 'home/contact_list.html', {'form':form, 'contacts':contacts})