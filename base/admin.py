from django.contrib import admin
from .models import Appointment, PredictedResult, Message, resultMail

# Register your models here.

# prediction results register


class DataAdmin(admin.ModelAdmin):
    list_display = ('age',
                    'gender',
                    'county',
                    'maritalStatus',
                    'coupleDiscordant',
                    'SexWithWoman',
                    'SexWithMan',
                    'condom_use',
                    'sw',
                    'pwid',
                    'testedBefore',
                    'presumedTB',
                    'treatmentTB',
                    'sti',
                    'rapevictim',
                    'HIVPrEP',
                    'y_pred',
                    'date')


admin.site.register(PredictedResult, DataAdmin)

# sent results register


class sentResult(admin.ModelAdmin):
    list_display = ('email',
                    'result',
                    'sent_date')


admin.site.register(resultMail, sentResult)

# appointment register
admin.site.register(Appointment)

# Referral messages register


class MesssageAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'phonenumber',
                    'sent_date')


admin.site.register(Message, MesssageAdmin)
