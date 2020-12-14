from django.contrib import admin

from analyzer.models import Website, WebsiteAvailability


class WebsiteAvailabilityAdmin(admin.ModelAdmin):
    list_display = ("__str__", "ip_address", "response_status_code", "reason", "server", "checked_at")
    list_filter = ("checked_at",)
    search_fields = ('website__url',)


admin.site.register(Website)
admin.site.register(WebsiteAvailability, WebsiteAvailabilityAdmin)
