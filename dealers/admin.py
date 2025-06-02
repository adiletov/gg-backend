from django.contrib import admin
from .models import Dealer, DealerImage

class DealerImageInline(admin.TabularInline):
    model = DealerImage
    extra = 1

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    inlines = [DealerImageInline]
    list_display = ['id', 'name', 'user', 'address', 'created_at']