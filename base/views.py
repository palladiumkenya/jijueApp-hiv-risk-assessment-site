import email
from email import message
from multiprocessing import context
from django.db.models import Q
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse

# imports
from django.shortcuts import render
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBRegressor
from joblib import load
from .models import PredictedResult, Message, resultMail
from .forms import DataForm, MessageForm


# Appointment imports
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template

# App views here


class Home(TemplateView):
    template_name = "base/index.html"

# contact form
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # contactMessage.objects.create(
        #     name=name, email=email, message=message)

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


# App views here.
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
        if y_pred <= 0.09:
            y_pred = 'LOW'

        elif y_pred > 0.1 or y_pred <= 0.2:
            y_pred = 'MODERATE'

        elif y_pred > 0.21 or y_pred <= 0.6:
            y_pred = 'HIGH'
        else:
            y_pred = 'HIGH and SHOULD TEST NOW'

        PredictedResult.objects.create(age=age,
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

        return render(request, 'result.html', {'result': y_pred})
    return render(request, 'main.html')


# class PredictorTemplateView(TemplateView):
#     template_name = "result.html"

#     def send_result(request):
#         if request.method == 'POST':
#             senders_email = request.POST.get('mail')

#             resultMail.objects.create(email=senders_email)

#             messages.add_message(request, messages.SUCCESS,
#                                  f"Your results has been sent successfully!")
#             return HttpResponseRedirect(request.path)
#         return render(request, 'result.html')


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


def MsgPage(request):
    return render(request, 'referral.html')


# Appointment views here.

class HomeAppointment(TemplateView):
    template_name = "homeappointment.html"


class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks {fname} for making an appointment, we will email you as soon as possible!")
        return HttpResponseRedirect(request.path)


class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname": appointment.first_name,
            "date": date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS,
                             f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "title": "Manage Appointments"
        })
        return context


# Referral message view here

class MessageView(TemplateView):
    template_name = "referral.html"
    model = Message

    def post(self, request):
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')

        Message.objects.create(
            name=name, phonenumber=phonenumber)

        messages.add_message(request, messages.SUCCESS,
                             f"Thank you for referring {name} for HIV self risk assessment. The message has been sent successfully!")
        return HttpResponseRedirect(request.path)
