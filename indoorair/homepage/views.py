from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index_page(request):
    return render(request, "homepage/index.html", {})


def contact_page(request):
    return render(request, "homepage/contact.html", {})


def get_version_api(request):
    return JsonResponse({
         'version': '1.0',
    })
