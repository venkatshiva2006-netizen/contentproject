from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Content

def add_content(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        Content.objects.create(title=title, body=body)
        return redirect('add_content')  # refresh after saving

    return render(request, "add_content.html")


def content_api(request):
    data = list(Content.objects.values())
    return JsonResponse(data, safe=False)
def display_content(request):
    return render(request, "display_content.html")



