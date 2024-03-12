from django.shortcuts import render
from django.views import generic
from .models import Menu, MENU_CATEGORY


# Create your views here.
class MenuList(generic.ListView):
    # A variable which will store list of data
    queryset = Menu.objects.order_by("dish_name")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menucategory']=MENU_CATEGORY
        return context


class DishDetails(generic.DetailView):
    model = Menu
    template_name = "dish_details.html"
