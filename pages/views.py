from django.shortcuts import render

from django.views.generic import TemplateView



class HomePagesView(TemplateView):
    template_name = "home.html"

class AboutUsView(TemplateView):
    template_name = "pages/aboutsus.html"
