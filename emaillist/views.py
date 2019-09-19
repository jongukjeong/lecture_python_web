from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist.models import Emaillist


def index(request):
    emaillist = Emaillist.objects.all().order_by('-id')

    data = {'emaillist': emaillist}

    return render(request, 'emaillist/index.html', data)


def form(request):
    return render(request, 'emaillist/form.html')


def add(request):
    emaillist = Emaillist()

    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    # db에 데이터 저장
    emaillist.save()

    return HttpResponseRedirect('/emaillist')
