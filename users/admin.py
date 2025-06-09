from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'value')
    search_fields = ('user__email', 'value')
    list_filter = ('type',)
class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [ContactInline]
    list_display = ('id', 'fullname', 'email', 'is_dealer', 'is_staff')
    search_fields = ('fullname', 'email')
    list_filter = ('is_dealer', 'is_staff', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('fullname', 'avatar', 'is_dealer', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    ordering = ('email',)
    base_field = 'email'