
# Register your models here.
from django.contrib import admin
from .models import Appointment, VirtualCounsellor

# Register your models here.

# appointment register
admin.site.register(Appointment)


class vcForm(admin.ModelAdmin):
    list_display = ('name',
                    'mail',
                    'phone_number',
                    'date_time')


admin.site.register(VirtualCounsellor, vcForm)
