from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# Create your views here.
method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
	template_name = 'social_login_app/home.html'