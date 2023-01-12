from django.contrib import admin
from .models import Appointment, PredResults, Message

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ('age', 'gender', 'county', 'maritalStatus','coupleDiscordant', 'SexWithWoman', 'SexWithMan', 'condom_use',
     'sw', 'pwid', 'testedBefore', 'presumedTB', 'treatmentTB', 'sti', 'rapevictim', 'HIVPrEP', 'y_pred')


admin.site.register(PredResults, DataAdmin)

admin.site.register(Appointment)


class MesssageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber')


admin.site.register(Message, MesssageAdmin)
