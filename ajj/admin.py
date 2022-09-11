from django.contrib import admin

from ajj.models import Registration

# Register your models here.
@admin.register(Registration)
class RegisterModelAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','phone']