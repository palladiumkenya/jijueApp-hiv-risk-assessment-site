from django.core.management.base import BaseCommand
from appointmentApp.models import County, SubCounty, Ward, Facility


class Command(BaseCommand):
    help = 'Load County, SubCounty, Wards, and Facilities'

    def handle(self, *args, **kwargs):
        SubCounty.objects.all().delete()
        county_names = [
            'Mombasa',
            'Kwale',
            'Kilifi',
            'Tana River',
            'Lamu',
            'Taita-Taveta',
            'Garissa',
            'Wajir',
            'Mandera',
            'Marsabit',
            'Isiolo',
            'Meru',
            'Tharaka Nithi',
            'Embu',
            'Kitui',
            'Machakos',
            'Makueni',
            'Nyandarua',
            'Nyeri',
            'Kirinyaga',
            'Muranga',
            'Kiambu',
            'Turkana',
            'West Pokot',
            'Samburu',
            'Trans-Nzoia',
            'Uasin-Gishu',
            'Elgeyo-Marakwet',
            'Nandi',
            'Baringo',
            'Laikipia',
            'Nakuru',
            'Narok',
            'Kajiado',
            'Kericho',
            'Bomet',
            'Kakamega',
            'Vihiga',
            'Bungoma',
            'Busia',
            'Siaya',
            'Kisumu',
            'HomaBay'
            'Migori',
            'Kisii',
            'Nyamira',
            'Nairobi'
        ]

        if not County.objects.count():
            for county_name in county_names:
                County.objects.create(name=county_name)

        # Mombasa subcounties
        mombasa = County.objects.get(name='Mombasa')

        mombasa_subcounties = [
            'Changamwe',
            'Jomvu',
            'Mvita',
            'Nyali',
            'Likoni',
            'Kisauni'

        ]

        for subcounty in mombasa_subcounties:
            SubCounty.objects.create(name=subcounty, county=mombasa)

        # Kwale subcounties
        kwale = County.objects.get(name='Kwale')

        kwale_subcounties = [
            'Msambweni',
            'Matuga',
            'Lunga Lunga'

        ]

        for subcounty in kwale_subcounties:
            SubCounty.objects.create(name=subcounty, county=kwale)

        # Kilifi Subcounties
        kilifi = County.objects.get(name='Kilifi')

        kilifi_subcounties = [
            'Msambweni',
            'Matuga',
            'Lunga Lunga'

        ]

        for subcounty in kilifi_subcounties:
            SubCounty.objects.create(name=subcounty, county=kilifi)

        # Tana River Subcounties

        tanariver = County.objects.get(name='Tana River')

        tanariver_subcounties = [
            '',
        ]

        for subcounty in tanariver_subcounties:
            SubCounty.objects.create(name=subcounty, county=tanariver)

        # 'Lamu Subcounties
        lamu = County.objects.get(name='Lamu')

        lamu_subcounties = [
            '',
        ]

        for subcounty in lamu_subcounties:
            SubCounty.objects.create(name=subcounty, county=lamu)

        # 'Taita-Taveta',
        taitataveta = County.objects.get(name='Taita-Taveta')

        taita_subcounties = [
            '',
        ]

        for subcounty in lamu_subcounties:
            SubCounty.objects.create(name=subcounty, county=lamu)

        # 'Garissa',
        # 'Wajir',
        # 'Mandera',
        # 'Marsabit',
        # 'Isiolo',
        # 'Meru',
        # 'Tharaka Nithi',
        # 'Embu',
        # 'Kitui',
        # 'Machakos',
        # 'Makueni',
        # 'Nyandarua',
        # 'Nyeri',
        # 'Kirinyaga',
        # 'Muranga',
        # 'Kiambu',
        # 'Turkana',
        # 'West Pokot',
        # 'Samburu',
        # 'Trans-Nzoia',
        # 'Uasin-Gishu',
        # 'Elgeyo-Marakwet',
        # 'Nandi',
        # 'Baringo',
        # 'Laikipia',
        # 'Nakuru',
        # 'Narok',
        # 'Kajiado',
        # 'Kericho',
        # 'Bomet',
        # 'Kakamega',
        # 'Vihiga',
        # 'Bungoma',
        # 'Busia',
        # 'Siaya',
        # 'Kisumu',
        # 'HomaBay'
        # 'Migori',
        # 'Kisii',
        # 'Nyamira',
        # 'Nairobi'
