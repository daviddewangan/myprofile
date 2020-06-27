from django.contrib import admin
from college.models import Project, Webpage, Category, Blog, Contact

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','tools','pub_date']
admin.site.register(Project,ProjectAdmin)
admin.site.register(Category)
admin.site.register(Webpage)
class BlogModel(admin.ModelAdmin):
    list_display = ['name','description']
    search_list = ['name','description']
admin.site.register(Blog,BlogModel)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','number']
    
admin.site.register(Contact,ContactAdmin)