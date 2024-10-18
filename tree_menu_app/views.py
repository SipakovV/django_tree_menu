from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


from .models import TreeMenu


def index(request):
    return HttpResponse("Здесь будет выведен список объявлений.")


def menu1(request):
    template = loader.get_template('menu1.html')
    #bbs = TreeMenu.objects.order_by('-published')
    #context = {'bbs': bbs}
    return HttpResponse(template.render({}, request))


class HomeView(TemplateView):
    template_name = 'index.html'


class Menu1View(TemplateView):
    template_name = 'menu1.html'
