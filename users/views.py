from typing import List
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from systems.models import * 
from users.forms import categoryForm,ProjectForm,UserRegisterForm
from users.models import Category,Profile,Project
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.htm', {'form':form})

def post (request):
    view_Project = Project.objects.all()
    u_user = User.objects.all()
    view_profile = Profile.objects.filter(user_id=request.user)
    
    context = {
        'view_Project':view_Project,
        'u_user':u_user,
        'view_profile':view_profile
    }
    return render(request, 'users/main/posts.htm', context)


def PostDetailView(request, pk):
    try:
        p = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        raise Http404("does not exist")

    if 'increment_download' in request.POST:
            increment = Project.objects.get(pk=pk)
            increment.count_download += 1
            increment.save()

    context = {'project': p}
    return render(request, 'users/main/assets/postdetail.htm', context)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'users/main/assets/confirm_del.htm'
    success_url = reverse_lazy('posts:post_list')

    def get_object(self , *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Project.objects.get(pk=pk)
        if not obj.p_author.user == self.request.user:
            messages.warning(self.request, 'your need to be the author of the post in order to delete')
        return obj
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProjectForm
    model = Project
    template_name = 'users/main/assets/update.htm'
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self,form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.p_author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None,"You need to be the author of the post in order to update it")
            return super().form_invalid(form)

class settingUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'users/main/updateProfile.htm'
    fields = ['full_name','phone','image','cover']
    
    def get_success_url(self): 
        return reverse('profiles:profile_default', args=[str(self.request.user.id)])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_profile'] = Profile.objects.filter(user_id=self.request.user)
        return context


def setting (request):
    view_profile = Profile.objects.filter(user_id=request.user)

    context = {
        'view_profile':view_profile
    }

    return render(request, 'users/main/setting.htm',context)

def createPost (request):
    create_category = categoryForm()
    p_post = ProjectForm()
    view_category = Category.objects.all()
    view_profile = Profile.objects.filter(user_id=request.user)
    
    if 'submit_c_category' in request.POST:
        create_category = categoryForm(request.POST)
        if create_category.is_valid():
            instance = create_category.save(commit=False)
            instance.save()
            create_category = categoryForm()

    if 'submit_p_post' in request.POST:
        p_post = ProjectForm(request.POST, request.FILES)
        if p_post.is_valid():
            instance = p_post.save(commit=False)
            instance.p_author = Profile.objects.get(user=request.user)
            instance.p_type = Category.objects.get(id=request.POST.get('p_type'))
            instance.save()
            p_post = ProjectForm()
            return redirect('posts:post_list')

    context = {
        'create_category' : create_category,
        'view_category' : view_category,
        'p_post':p_post,
        'view_profile':view_profile
    }
    return render(request, 'users/main/assets/createpost.htm', context)

@login_required
# def profile(request):
#     view_profile = Profile.objects.filter(user_id=request.user)

#     context = {
#         'view_profile':view_profile
#     }
#     return render(request, 'users/main/profile_.htm',context)

def p_profile(request):
    view_profile = Profile.objects.filter(user_id=request.user)

    context = {
        'view_profile':view_profile
    }
    return render(request, 'users/main/profile_.htm',context)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'users/main/profile_.htm'
    fields = ['bio']

    def get_success_url(self): 
        return reverse('profiles:profile_default', args=[str(self.request.user.id)])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_profile'] = Profile.objects.filter(user_id=self.request.user)
        return context