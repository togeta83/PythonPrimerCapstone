# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Titles


def index(request):
    mytitles = Titles.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mytitles': mytitles,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['anime']
    y = request.POST['author']
    z = request.POST['chapters']
    title = Titles(anime=x, author=y, chapters=z)
    title.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    title = Titles.objects.get(id=id)
    title.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mytitle = Titles.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mytitle': mytitle,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    anime = request.POST['anime']
    author = request.POST['author']
    chapters = request.POST['chapters']
    title = Titles.objects.get(id=id)
    title.anime = anime
    title.author = author
    title.chapters = chapters
    title.save()
    return HttpResponseRedirect(reverse('index'))
