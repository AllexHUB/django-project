from django.http import HttpResponseRedirect
from django.shortcuts import render
from YourChance.forms import AddProjectForm
from djangoProject.utils import get_db_handle

db_client, current_db = get_db_handle("yourchancedb")
projects_collection = current_db["projects"]
users_collection = current_db["users"]
inv_views_collection = current_db["investment_views"]

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить проект", 'url_name': 'form'},
        {'title': "Мои проекты", 'url_name': 'my-projects'}]

web = {range(8, 15): range(120000, 180000),
       range(16, 25): range(70000, 119999),
       range(26, 35): range(45800, 69999),
       range(36, 60): range(18000, 45799),
       range(61, 90): range(0, 17999)}

android = {range(31, 62): range(100000, 124999),
           range(63, 124): range(125000, 239999),
           range(124, 360): range(240000, 350000)}

new_project = {}


def home(request):
    return render(request, 'home.html', {'menu': menu})


def project_form(request):
    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            d_project = form.cleaned_data
            projects_collection.insert_one(d_project)
            new_project.update(d_project)
            return HttpResponseRedirect('/analysis/')
    else:
        form = AddProjectForm()
    return render(request, 'project_form.html', {'form': form, 'menu': menu})


def project_analysis(request):
    prices = 0
    print(new_project)
    project_terms = new_project['terms']
    project_platform = new_project['platform']
    if project_platform == 'Android':
        for terms in android:
            if project_terms in terms:
                prices = android[terms]
    else:
        for terms in web:
            if project_terms in terms:
                prices = web[terms]
    print("PRICES = ", prices)
    return render(request, 'project_analysis.html', {'menu': menu, 'project': new_project, 'prices': prices})


def about_site(request):
    return render(request, 'about_site.html', {'menu': menu})


def my_projects(request):
    projects_list = projects_collection.find()
    return render(request, 'my_projects.html', {'menu': menu})
