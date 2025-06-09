from django.contrib import admin
from .models import HowTo, Recommendation


# Register How To model
@admin.register(HowTo)
class HowToAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'shared_on')
    search_fields = ('title', 'content')
    list_filter = ('status', 'shared_on')

# Register Recommendation model
admin.site.register(Recommendation)
