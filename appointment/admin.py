from django.contrib import admin
from . models import County, SubCounty, Ward, Facility

# Register your models here.
admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Ward)
admin.site.register(Facility)
