from django.shortcuts import render
from . models import County, SubCounty, Ward, Facility

# Create your views here.


def counties(request):
    counties = County.objects.all()
    context = {'counties': counties}
    return render(request, 'appointment/appoint_ment.html', context)


def sub_counties(request):
    county = request.GET.get('county')
    sub_counties = SubCounty.objects.filter(county=county)
    context = {'sub_counties': sub_counties, 'is_htmx': True}
    return render(request, 'partials/sub_county.html', context)


def wards(request):
    sub_county = request.GET.get('sub_county')
    wards = Ward.objects.filter(sub_county=sub_county)
    context = {'wards': wards}
    return render(request, 'partials/ward.html', context)
