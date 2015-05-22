from django.contrib import admin
from newstreet.models import Category, Page

from newstreet.models import UserProfile


admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)

