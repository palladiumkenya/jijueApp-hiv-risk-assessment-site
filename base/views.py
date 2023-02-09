from django.shortcuts import render, redirect

from django.http import HttpResponse

# imports
from django.shortcuts import render
# from sklearn.tree import DecisionTreeClassifier
# from xgboost import XGBRegressor
from joblib import load
from .models import PredictedResult, ReferralMessage, resultMail, ContactMessage


# Mail imports
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string, get_template

from django.template.loader import render_to_string

# App views here


class Home(TemplateView):
    template_name = "base/index.html"

# contact form
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(name=name, email=email, message=message)

        email = EmailMessage(
            subject=f"{name} from JijueApp",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks {name} for contacting us, we will get back to you as soon as possible!")
        return HttpResponseRedirect(request.path)


# Importing the ML model for prediction.
model = load('./savedModels/G3model.joblib')


# Predictor views here.
def predictor(request):
    if request.method == 'POST':
        age = request.POST['age']
        gender = request.POST['gender']
        county = request.POST['county']
        maritalStatus = request.POST['maritalStatus']
        coupleDiscordant = request.POST['coupleDiscordant']
        SexWithWoman = request.POST['SexWithWoman']
        SexWithMan = request.POST['SexWithMan']
        condom_use = request.POST['condom_use']
        sw = request.POST['sw']
        pwid = request.POST['pwid']
        testedBefore = request.POST['testedBefore']
        presumedTB = request.POST['presumedTB']
        treatmentTB = request.POST['treatmentTB']
        sti = request.POST['sti']
        rapevictim = request.POST['rapevictim']
        HIVPrEP = request.POST['HIVPrEP']

        y_pred = model.predict(
            [[age, gender, maritalStatus, coupleDiscordant, sw, pwid, testedBefore, presumedTB, treatmentTB]])

        if y_pred <= 0.009:
            y_pred = 'LOW RISK'

        elif y_pred > 0.01 or y_pred <= 0.2:
            y_pred = 'MODERATE'

        elif y_pred > 0.21 or y_pred <= 0.6:
            y_pred = 'HIGH RISK'
        else:
            y_pred = 'HIGH RISK and SHOULD TEST NOW'

        # y_pred = result_out

        userresult = PredictedResult.objects.create(age=age,
                                                    gender=gender,
                                                    county=county,
                                                    maritalStatus=maritalStatus,
                                                    coupleDiscordant=coupleDiscordant,
                                                    SexWithWoman=SexWithWoman,
                                                    SexWithMan=SexWithMan,
                                                    condom_use=condom_use,
                                                    sw=sw,
                                                    pwid=pwid,
                                                    testedBefore=testedBefore,
                                                    presumedTB=presumedTB,
                                                    treatmentTB=treatmentTB,
                                                    sti=sti,
                                                    rapevictim=rapevictim,
                                                    HIVPrEP=HIVPrEP,
                                                    y_pred=y_pred)

        userresult.save()

        return render(request, 'result.html', {'result': y_pred})
    return render(request, 'main.html')


def welcomePage(request):
    return render(request, 'base/welcome.html')


def disclaimerPage(request):
    return render(request, 'base/disclaimer.html')


def vctPage(request):
    return render(request, 'base/vct.html')


def nutritionPage(request):
    return render(request, 'base/nutrition.html')


def statPage(request):
    return render(request, 'statistics.html')

# Result views here.


class ResultPage(TemplateView):
    model = PredictedResult
    template_name = 'base/getresult.html'
    # result = predictor(result_out)

    # def post(self, request):
    #     date = request.POST.get("date")
    #     appointment_id = request.POST.get("appointment-id")
    #     appointment = Appointment.objects.get(id=appointment_id)
    #     appointment.accepted = True
    #     appointment.accepted_date = datetime.datetime.now()
    #     appointment.save()

    #     data = {
    #         "fname": appointment.first_name,
    #         "date": date,
    #     }

    #     message = get_template('appointmentApp/email.html').render(data)
    #     email = EmailMessage(
    #         "About your appointment",
    #         message,
    #         settings.EMAIL_HOST_USER,
    #         [appointment.email],
    #     )
    #     email.content_subtype = "html"
    #     email.send()

    #     messages.add_message(request, messages.SUCCESS,
    #                          f"You accepted the appointment of {appointment.first_name}")
    #     return HttpResponseRedirect(request.path)

    def post(self, request):
        name = request.POST.get('name')
        senders_email = request.POST.get('mail')
        # userresult_id = request.POST.get("userresult-id")
        # userresult = PredictedResult.objects.get(id=userresult_id)
        # userresult.save()

        # newdata = {
        #     'name': name,
        #     'result': userresult.y_pred
        # }

        # predicted_result = PredictedResult.objects.get()
        # predicted_result.save()

        # result = y_pred
        result = "Low"

        data = {"name": name,
                "result": result}

        message = get_template('base/email.html').render(data)

        resultMail.objects.create(name=name,
                                  email=senders_email, result=result)

        email = EmailMessage(
            "Results of Your Requested HIV Risk Assessment",
            message,
            settings.EMAIL_HOST_USER,  # from
            [senders_email],  # to
            [settings.EMAIL_HOST_USER]  # reply to
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS,
                             f"Dear {name}, your results has been sent to your email successfully!")
        return HttpResponseRedirect(request.path)


# Referral message view here

class MessageView(TemplateView):
    template_name = "referral.html"
    model = ReferralMessage

    def post(self, request):
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')

        ReferralMessage.objects.create(
            name=name, phonenumber=phonenumber)

        messages.add_message(request, messages.SUCCESS,
                             f"Thank you for referring {name} for HIV self risk assessment. The message has been sent successfully!")
        return HttpResponseRedirect(request.path)
