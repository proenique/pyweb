from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.models import User
from . models import Profile
from .forms import ProfileForm
from apps.brands.models import Brand
# Create your views here.


class UserListView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'profiles'
        return context
    
    


class UserDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'profile'
        context["brand"] = Brand.objects.filter(active=True).first()
        return context
    
    



class UserUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "update_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'update/profile'
        return context
    
    


class UserDeleteView(DeleteView):
    model = User
    pk_url_kwarg = 'pk'
    template_name = "delete_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'delete/profile'
        context["profile"] = self.object.profile
        return context
    
   
