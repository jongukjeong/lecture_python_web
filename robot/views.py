from urllib.request import Request, urlopen

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def robot(request):
    return render(request, 'robot/robot.html')


def robot_token(request):
    token = request.GET['token_value']

    url = "https://www.google.com/recaptcha/api/siteverify?"
    url += "secret=6Le-q6kUAAAAAGWHCi3P7yb457bYJ9KGt5Rjc6h5"
    url += "&response=" + token

    recaptcha = Request(url)
    recaptcha.add_header("Content-Type", "json/application")

    http_response = urlopen(recaptcha)

    data = http_response.read().decode('utf-8')

    print(data)

    return HttpResponse(data, content_type='application/json')
