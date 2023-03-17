from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ('first_name','last_name','email', 'id')
    fields = ('first_name','last_name','email','id','created', 'last_login','is_staff', 'is_active')
    readonly_fields = ('id','email','created', 'last_login')
  