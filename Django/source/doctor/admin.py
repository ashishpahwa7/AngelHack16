from django.contrib import admin

# Register your models here.
from .models import Doctoral

class DoctoralAdmin(admin.ModelAdmin):
	list_display = ["Enter_Government_Registered_No", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["Enter_Government_Registered_No"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["Enter_Government_Registered_No", "Doctor_Email_id"]
	class Meta:
		model = Doctoral


admin.site.register(Doctoral)