from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    if request.method == "POST":
        form = request.POST
        print(form.cleaned_data)
    return render(request, "project_form.html")
