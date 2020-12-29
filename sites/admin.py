from django.contrib import admin
from .models import *

admin.site.register(Calculate)
admin.site.register(SubTags)


# Project
class ProjectsImageAdmin(admin.StackedInline):
    model = Images_Projects
 
@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectsImageAdmin]
 
    class Meta:
       model = Projects
 
@admin.register(Images_Projects)
class ProjectsImageAdmin(admin.ModelAdmin):
    pass



# Products
class ProductsImageAdmin(admin.StackedInline):
    model = Images_Products
 
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductsImageAdmin]
 
    class Meta:
       model = Products
 
@admin.register(Images_Products)
class ProductsImageAdmin(admin.ModelAdmin):
    pass


















# News
class NewImageAdmin(admin.StackedInline):
    model = Images_news
 
@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    inlines = [NewImageAdmin]
 
    class Meta:
       model = News
 
@admin.register(Images_news)
class NewImageAdmin(admin.ModelAdmin):
    pass