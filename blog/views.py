from urllib import request

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.
from blog import forms, models
from blog.forms import commentsForm
from blog.models import article, comments


def Home(request):
    art = article.objects.all()
    paginator = Paginator(art,5) #show  article per page
    page_var = 'page'
    page = request.GET.get(page_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'query' : queryset,
        'page_var' : page_var,
        'art' : art
    }
    return render(request, 'index.html', context)

def viewarticle(request,aid):
     art = article.objects.get(id=aid)
     co = comments.objects.all()
     form_data = forms.commentsForm(request.POST or None)
     msg = ''
     if form_data.is_valid():
         comment = models.comments()
         comment.name = form_data.cleaned_data['name']
         comment.comment = form_data.cleaned_data['comment']
         comment.save()
         msg = 'Comment Published'
     else:
         msg = 'Error,Please Try Again'
     context = {
         'co' : co,
      'art' : art,
      'form_data' : form_data,
      'msg' : msg
      }
     return render(request, 'article.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')