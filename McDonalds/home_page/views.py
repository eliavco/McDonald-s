from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from home_page.models import Restaurant,Workers
from django.urls import reverse_lazy
# Create your views here.
class McGallery(TemplateView):
    template_name = 'gallery.html'

class McHomeView(TemplateView):
    template_name = 'home.html'

class McListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'

class McDetailView(DetailView):
    context_object_name = 'restaurant_details'
    model = Restaurant
    template_name = 'restaurant_detail.html'

class McCreateView(CreateView):
    model = Restaurant
    fields = '__all__'
    template_name = 'restaurant_form.html'

class McUpdateView(UpdateView):
    model = Restaurant
    fields = '__all__'
    template_name = 'restaurant_form.html'

class McDeleteView(DeleteView):
    model = Restaurant
    success_url = reverse_lazy("home:list")
    template_name = 'confirm_delete.html'
