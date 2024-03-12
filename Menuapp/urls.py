from django.urls import path
from . import views

urlpatterns = [
    path("", views.MenuList.as_view(), name="MenuList"),
    path("dishdetails/<int:pk>/", views.DishDetails.as_view(), name="dishdetails"),
]