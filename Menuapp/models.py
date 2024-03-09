from django.db import models
from django.contrib.auth.models import User

# for better UX (finite data)drop down list for existing choices
MENU_CATEGORY = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('desserts', 'Desserts'),
    ('main_course', 'Main Course'),
    ('cool_drinks', 'Cool Drinks')
)

STATUSES =(
    (0, 'Unavailable'),
    (1, 'Available')
)


# Create your models here.
class Menu(models.Model):
    menu_item = models.CharField(max_length=80, choices=MENU_CATEGORY)
    dish_name = models.CharField(max_length=80, unique=True)
    ingredients = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # Many to One relationship
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUSES, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_item



