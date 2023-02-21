# Appointment imports
from django.shortcuts import render

from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from . models import Appointment, VirtualCounsellor
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template


# App views here

# Appointment views here.

class HomeAppointment(TemplateView):
    template_name = "appointmentApp/main.html"

    def post(self, request):
        name = request.POST.get("name")
        mail = request.POST.get("mail")
        phone_number = request.POST.get("phone_number")
        date_time = request.POST.get("date_time")

        virtual_counsellor = VirtualCounsellor.objects.create(
            name=name,
            mail=mail,
            phone_number=phone_number,
            date_time=date_time,
        )

        virtual_counsellor.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks {name} for making a virtual appointment, we will call you back at the requested time!")
        return HttpResponseRedirect(request.path)


class AppointmentTemplateView(TemplateView):
    template_name = "appointmentApp/appointment.html"

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
    template_name = "appointmentApp/manage-appointments.html"
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

        message = get_template('appointmentApp/email.html').render(data)
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
