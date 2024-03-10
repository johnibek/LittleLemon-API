from django.contrib import admin
from . import models

admin.site.register([models.Category, models.MenuItem, models.Cart, models.Order, models.OrderItem])
