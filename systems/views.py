from django.db.models import query
from django.shortcuts import render, redirect
from users.views import Project
from django.db.models import Q
from systems.forms import contactForm
from systems.models import contact

# Create your views here.
def Home (request):
    best_download = Project.objects.all().order_by('-count_download')[:4] 

    context = {
        'best_download': best_download
    }
    return render(request, 'main/home.html',context)

def about (request):
    return render(request, 'main/about.html')

def academics (request):
    return render(request, 'main/academics.html')

def students (request):
    return render(request, 'main/students.html')

def contact (request):
    c_contact = contactForm()

    if 'submit_c_contact' in request.POST:
        c_contact = contactForm(request.POST)
        if c_contact.is_valid():
            instance = c_contact.save(commit=False)
            instance.save()
            c_contact = contactForm()
    
    context = {
        'c_contact' : c_contact,
    }

    return render(request, 'main/contact.html',context)

def administrator (request):
    best_download = Project.objects.all().order_by('-count_download')[:5] 

    context = {
        'best_download': best_download
    }
    return render(request, 'main/administrator.html',context)

def is_valid_queryparam(param):
    return param != '' and param is not None

def search(request):
    p_project = Project.objects.all()
    v_project = Project.objects.all()
    search_post = request.GET.get('q')
    if search_post:
        p_project = Project.objects.filter(Q(p_name__icontains=search_post))

    p_name = request.GET.get('title')
    # p_author = request.GET.get('author')
    p_category = request.GET.get('category')
    if p_name != '' and p_name is not None:
        p_project = p_project.filter(p_name__icontains=p_name)

    # elif p_category != 'ปี' and p_category is not None:
    #     p_project = p_project.filter(Q(p_date__icontains=p_category))

    if is_valid_queryparam(p_category) and p_category != 'ปี':
        p_project = p_project.filter(p_date__icontains=p_category)


    context = {
        # 'post': post,
        'v_project':v_project,
        'p_project':p_project
        }

    return render(request, 'main/search.html', context)