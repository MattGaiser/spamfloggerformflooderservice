from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
import string
from . import models

def random_string(N):
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase +string.digits, k=N))

@csrf_exempt
def generate_code(request):
    input = json.loads(request.body)
    temp = {}
    temp["email"] = random_string(10) + '@' + random_string(7) + '.' + random_string(3)
    temp["password"] = random_string(12) + '#'
    models.CodesForForms.objects.create(url=input, email=temp["email"], password=temp["password"])
    return HttpResponse(json.dumps(temp))

@csrf_exempt
def get_code_by_url(request):
    input = json.loads(request.body)
    results = models.CodesForForms.objects.filter(url=input[0])
    data = []
    for result in results:
        temp = {}
        temp["url"] = result.url
        temp["email"] = result.email
        temp["password"] = result.password
        data.append(temp)
    return HttpResponse(json.dumps(data))

def index(request):
    potentials = models.CodesForForms.objects.all()
    context = {
        "potentials":potentials,
    }
    return render(request, "index.html", context)