from django.contrib import admin

# Register your models here.

from .models import Wine, Winery

admin.site.register(Wine)

admin.site.register(Winery)
