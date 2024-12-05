from django.contrib import admin
from .models import Feedback

# Customize the Feedback display in the admin panel
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'created_at')  # Columns to display
    list_filter = ('rating', 'created_at')  # Filters in the sidebar
    search_fields = ('rating',)  # Search bar

# Register the Feedback model with the admin
admin.site.register(Feedback, FeedbackAdmin)
