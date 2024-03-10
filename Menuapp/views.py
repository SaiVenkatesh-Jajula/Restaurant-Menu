from django.shortcuts import render
from django.views import generic
from .models import Menu


# Create your views here.
class MenuList(generic.ListView):
    # A variable which will store list of data
    queryset = Menu.objects.order_by("dish_name")
    template_name = "index.html"


class DishDetails(generic.DetailView):
    model = Menu
    template_name = "dish_details.html"
