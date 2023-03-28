from django.core.management.base import BaseCommand
from appointment.models import County, SubCounty, Ward, Facility


class Command(BaseCommand):
    help = 'Load County, SubCounty, Wards, and Facilities'

    def handle(self, *args, **kwargs):
        SubCounty.objects.all().delete()
        county_names = [
            'Mombasa',
            'Kwale',
            'Kilifi',
            # 'Tana-River',
            # 'Lamu',
            'Taita-Taveta',
            # 'Garissa',
            # 'Wajir',
            # 'Mandera',
            # 'Marsabit',
            # 'Isiolo',
            'Meru',
            'Tharaka-Nithi',
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
            'West-Pokot',
            # 'Samburu',
            'Trans-Nzoia',
            'Uasin-Gishu',
            'Elgeyo-Marakwet',
            # 'Nandi',
            # 'Baringo',
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
            'Homa-Bay',
            'Migori',
            'Kisii',
            'Nyamira',
            'Nairobi',
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
            'Kaloleni',
            'Kilifi North',
            'Malindi',
            'Rabai',
            'Kilifi South',


        ]

        for subcounty in kilifi_subcounties:
            SubCounty.objects.create(name=subcounty, county=kilifi)

        # Tana River Subcounties

        # tanariver = County.objects.get(name='Tana-River')

        # tanariver_subcounties = [
        #     '',
        # ]

        # for subcounty in tanariver_subcounties:
        #     SubCounty.objects.create(name=subcounty, county=tanariver)

        # # 'Lamu Subcounties
        # lamu = County.objects.get(name='Lamu')

        # lamu_subcounties = [
        #     '',
        # ]

        # for subcounty in lamu_subcounties:
        #     SubCounty.objects.create(name=subcounty, county=lamu)

        # 'Taita-Taveta subcounties',
        taitataveta = County.objects.get(name='Taita-Taveta')

        taita_subcounties = [
            'Voi',
            'Mwatate',
            'Wundanyi'
        ]

        for subcounty in taita_subcounties:
            SubCounty.objects.create(name=subcounty, county=taitataveta)

        # Garissa Subcounties
        # garissa = County.objects.get(name='Garissa')

        # garissa_subcounties = [
        #     '',
        # ]

        # for subcounty in garissa_subcounties:
        #     SubCounty.objects.create(name=subcounty, county=garissa)

        # # 'Wajir Subcounties
        # wajir = County.objects.get(name='Wajir')

        # wajir_subcounties = [
        #     '',
        # ]

        # for subcounty in wajir_subcounties:
        #     SubCounty.objects.create(name=subcounty, county=wajir)

        # # 'Mandera Subcounties
        # mandera = County.objects.get(name='Mandera')

        # mandera_subcounties = [
        #     '',
        # ]

        # for subcounty in mandera_subcounties:
        #     SubCounty.objects.create(name=subcounty, county=mandera)

        # # 'Marsabit Subcounties
        # marsabit = County.objects.get(name='Marsabit')

        # marsabit_subcounties = [
        #     '',
        # ]

        # for subcounty in marsabit_subcounties:
        #     SubCounty.objects.create(name=subcounty, county=marsabit)

        # # 'Isiolo Subcounties
        # isiolo = County.objects.get(name='Isiolo')

        # isiolo_subcounties = [
        #     '',
        # ]

        # for subcounty in isiolo_subcounties:
        #     SubCounty.objects.create(name=subcounty, county=isiolo)

        # 'Meru Subcounties
        meru = County.objects.get(name='Meru')

        meru_subcounties = [
            'Igembe South',
            'Imenti South',
            'Igembe North'
        ]

        for subcounty in meru_subcounties:
            SubCounty.objects.create(name=subcounty, county=meru)

        # 'Tharaka Subcounties
        tharakanithi = County.objects.get(name='Tharaka-Nithi')

        tharakanithi_subcounties = [
            'Maara',
            'Tharaka South',
            'Chuka',
            'Tharaka South',

        ]

        for subcounty in tharakanithi_subcounties:
            SubCounty.objects.create(name=subcounty, county=tharakanithi)

        # 'Embu Subcounties
        embu = County.objects.get(name='Embu')

        embu_subcounties = [
            'Runyenjes',
            'Mbeere South'
        ]

        for subcounty in embu_subcounties:
            SubCounty.objects.create(name=subcounty, county=embu)

        # 'Kitui Subcounties
        kitui = County.objects.get(name='Kitui')

        kitui_subcounties = [
            'Kitui Central',
            'Kitui Rural',
            'Kitui East',
            'Kitui South',
            'Mwingi West',
            'Mwingi Central',
            'Mwingi North'
            'Kitui West'
        ]

        for subcounty in kitui_subcounties:
            SubCounty.objects.create(name=subcounty, county=kitui)

        # 'Machakos Subcounties
        machakos = County.objects.get(name='Machakos')

        machakos_subcounties = [
            'Mavoko',
            'Kangundo',
            'Yatta',
            'Kathiani',
            'Mwala',
            'Machakos Town',
            'Matungulu',
            'Masinga'
        ]

        for subcounty in machakos_subcounties:
            SubCounty.objects.create(name=subcounty, county=machakos)

        # 'Makueni Subcounties
        makueni = County.objects.get(name='Makueni')

        makueni_subcounties = [
            'Kibwezi East',
            'Kibwezi West',
            'Kilome',
            'Mbooni',
            'Makueni',
            'Kaiti'
        ]

        for subcounty in makueni_subcounties:
            SubCounty.objects.create(name=subcounty, county=makueni)

        # 'Nyandarua Subcounties
        nyandarua = County.objects.get(name='Nyandarua')

        nyandarua_subcounties = [
            'Kinangop',
            'kipipiri',
            'Oljoroorok',
            'Olkalou',
            'Ndaragwa'
        ]

        for subcounty in nyandarua_subcounties:
            SubCounty.objects.create(name=subcounty, county=nyandarua)

        # 'Nyeri Subcounties
        nyeri = County.objects.get(name='Nyeri')

        nyeri_subcounties = [
            'Kieni East',
            'Kieni West',
            'Mathira East',
            'Mathira West',
            'Mukurweini',
            'Nyeri Central',
            'Nyeri South',
            'Tetu'
        ]

        for subcounty in nyeri_subcounties:
            SubCounty.objects.create(name=subcounty, county=nyeri)

        # 'Kirinyaga Subcounties
        kirinyaga = County.objects.get(name='Kirinyaga')

        kirinyaga_subcounties = [
            'Kirinyaga East',
            'kirinyaga North',
            'Kirinyaga West',
        ]

        for subcounty in kirinyaga_subcounties:
            SubCounty.objects.create(name=subcounty, county=kirinyaga)

        # 'Muranga Subcounties
        muranga = County.objects.get(name='Muranga')

        muranga_subcounties = [
            'Kandara',
            'Kiharu',
            'Kangema',
            'Gatanga',
            'Mathioya',
            'Kigumo',
            'Maragwa'
        ]

        for subcounty in muranga_subcounties:
            SubCounty.objects.create(name=subcounty, county=muranga)

        # 'Kiambu Subcounties
        kiambu = County.objects.get(name='Kiambu')

        kiambu_subcounties = [
            'Limuru',
            'Kiambu Town',
            'Ruiru',
            'Kiambaa',
            'Kikuyu',
            'Githunguri',
            'Lari',
            'Thika Town'
        ]

        for subcounty in kiambu_subcounties:
            SubCounty.objects.create(name=subcounty, county=kiambu)

        # 'Turkana Subcounties
        turkana = County.objects.get(name='Turkana')

        turkana_subcounties = [
            'Turkana South',
            'Turkana Central',
            'Turkana West',
            'Turkana North',
        ]

        for subcounty in turkana_subcounties:
            SubCounty.objects.create(name=subcounty, county=turkana)

        # 'West Pokot Subcounties
        westpokot = County.objects.get(name='West-Pokot')

        westpokot_subcounties = [
            'Pokot South',
            'Pokot North',
            'Pokot Central',
        ]

        for subcounty in westpokot_subcounties:
            SubCounty.objects.create(name=subcounty, county=westpokot)

        # 'Samburu Subcounties
        # samburu = County.objects.get(name='Samburu')

        # samburu_subcounties = [
        #     '',
        # ]

        # for subcounty in samburu_subcounties:
        #     SubCounty.objects.create(name=subcounty, county=samburu)

        # 'Trans-Nzoia Subcounties
        transnzoia = County.objects.get(name='Trans-Nzoia')

        transnzoia_subcounties = [
            'Kiminini',
            'Cherangany',
            'Kwanza',
            'Saboti',
        ]

        for subcounty in transnzoia_subcounties:
            SubCounty.objects.create(name=subcounty, county=transnzoia)

        # 'Uasin-Gishu Subcounties
        uasingishu = County.objects.get(name='Uasin-Gishu')

        uasingishu_subcounties = [
            'Yatta',
            'Kapseret'
        ]

        for subcounty in uasingishu_subcounties:
            SubCounty.objects.create(name=subcounty, county=uasingishu)

        # 'Elgeyo-Marakwet Subcounties
        elgeyo = County.objects.get(name='Elgeyo-Marakwet')

        elgeyo_subcounties = [
            'Marakwet West',
        ]

        for subcounty in elgeyo_subcounties:
            SubCounty.objects.create(name=subcounty, county=elgeyo)

        # 'Nandi Subcounties
        # nandi = County.objects.get(name='Nandi')

        # nandi_subcounties = [
        #     '',
        # ]

        # for subcounty in nandi_subcounties:
        #     SubCounty.objects.create(name=subcounty, county=nandi)

        # # 'Baringo Subcounties
        # baringo = County.objects.get(name='Baringo')

        # baringo_subcounties = [
        #     '',
        # ]

        # for subcounty in baringo_subcounties:
        #     SubCounty.objects.create(name=subcounty, county=baringo)

        # 'Laikipia Subcounties
        laikipia = County.objects.get(name='Laikipia')

        laikipia_subcounties = [
            'Laikipia East',
            'Laikipia North',
            'Laikipia West',
        ]

        for subcounty in laikipia_subcounties:
            SubCounty.objects.create(name=subcounty, county=laikipia)

        # 'Nakuru Subcounties
        nakuru = County.objects.get(name='Nakuru')

        nakuru_subcounties = [
            'Naivasha',
            'Gilgil',
            'Njoro',
            'Nakuru North',
            'Rongai',
            'Nakuru West'
        ]

        for subcounty in nakuru_subcounties:
            SubCounty.objects.create(name=subcounty, county=nakuru)

        # 'Narok Subcounties
        narok = County.objects.get(name='Narok')

        narok_subcounties = [
            'Transmara West',
            'Narok West',
            'Narok South',
            'Narok North',

        ]

        for subcounty in narok_subcounties:
            SubCounty.objects.create(name=subcounty, county=narok)

        # 'Kajiado Subcounties
        kajiado = County.objects.get(name='Kajiado')

        kajiado_subcounties = [
            'Kajiado South',
            'Kajiado North',
            'Kajiado Central',
            'Loitokitok',
            'Kajiado East',
            'Kajiado West',
        ]

        for subcounty in kajiado_subcounties:
            SubCounty.objects.create(name=subcounty, county=kajiado)

        # 'Kericho Subcounties
        kericho = County.objects.get(name='Kericho')

        kericho_subcounties = [
            'Ainamoi',
            'Bureti',
            'Kipkelion',
        ]

        for subcounty in kericho_subcounties:
            SubCounty.objects.create(name=subcounty, county=kericho)

        # 'Bomet Subcounties
        bomet = County.objects.get(name='Bomet')

        bomet_subcounties = [
            'Bomet Central',
            'Bomet East',
            'Sotik'
        ]

        for subcounty in bomet_subcounties:
            SubCounty.objects.create(name=subcounty, county=bomet)

        # 'Kakamega Subcounties
        kakamega = County.objects.get(name='Kakamega')

        kakamega_subcounties = [
            'Likuyani',
            'Lurambi',
            'Malava',
            'Mumias West',
            'Butere',
            'Shinyalu',
        ]

        for subcounty in kakamega_subcounties:
            SubCounty.objects.create(name=subcounty, county=kakamega)

        # 'Vihiga Subcounties
        vihiga = County.objects.get(name='Vihiga')

        vihiga_subcounties = [
            'Hamisi',
            'Vihiga',
            'Sabatia',
            'Emuhaya'
        ]

        for subcounty in vihiga_subcounties:
            SubCounty.objects.create(name=subcounty, county=vihiga)

        # 'Bungoma Subcounties
        bungoma = County.objects.get(name='Bungoma')

        bungoma_subcounties = [
            'Kimilili',
            'Kanduyi',
            'Kabuchai',
            'Tongaren',
            'Webuye West'
        ]

        for subcounty in bungoma_subcounties:
            SubCounty.objects.create(name=subcounty, county=bungoma)

        # 'Busia Subcounties
        busia = County.objects.get(name='Busia')

        busia_subcounties = [
            'Butula',
            'Bunyala',
            'Matayos',
            'Samia',
            'Teso South'
        ]

        for subcounty in busia_subcounties:
            SubCounty.objects.create(name=subcounty, county=busia)

        # Siaya Subcounties
        siaya = County.objects.get(name='Siaya')

        siaya_subcounties = [
            'Ugunja',
            'Bondo',
            'Gem',
            'Alego Usonga',
            'Rarieda',
            'Ugenya'
        ]

        for subcounty in siaya_subcounties:
            SubCounty.objects.create(name=subcounty, county=siaya)

        # Kisumu Subcounties
        kisumu = County.objects.get(name='Kisumu')

        kisumu_subcounties = [
            'Kisumu Central',
            'Nyakach',
            'Kisimu East',
            'Nyando',
            'Kisumu West',
            'Muhoroni',
            'Seme'
        ]

        for subcounty in kisumu_subcounties:
            SubCounty.objects.create(name=subcounty, county=kisumu)

        # HomaBay Subcounties
        homabay = County.objects.get(name='Homa-Bay')

        homabay_subcounties = [
            'Rangwe',
            'Ndhiwa',
            'Mbita',
            'Karachuonyo'
            'Suba',
            'HomaBay Town',
            'Kasipul'

        ]

        for subcounty in homabay_subcounties:
            SubCounty.objects.create(name=subcounty, county=homabay)

        # Migori Subcounties
        migori = County.objects.get(name='Migori')

        migori_subcounties = [
            'Rongo',
            'Awendo',
            'Nyatike',
            'Kuria West',
            'Uriri',
            'Suna West',
            'Suna East'
        ]

        for subcounty in migori_subcounties:
            SubCounty.objects.create(name=subcounty, county=migori)

        # 'Kisii Subcounties
        kisii = County.objects.get(name='Kisii')

        kisii_subcounties = [
            'Bonchari',
            'South Mugirango',
            'Bobasi',
            'Kitutu Chache North',
            'Nyaribari Chache',
            'Nyaribari Masaba'
        ]

        for subcounty in kisii_subcounties:
            SubCounty.objects.create(name=subcounty, county=kisii)

        # 'Nyamira Subcounties
        nyamira = County.objects.get(name='Nyamira')

        nyamira_subcounties = [
            'Borabu',
            'Manga',
            'Nyamira',
            'Nyamira North',
            'Masaba North'
        ]

        for subcounty in nyamira_subcounties:
            SubCounty.objects.create(name=subcounty, county=nyamira)

        # 'Nairobi Subcounties
        nairobi = County.objects.get(name='Nairobi')

        nairobi_subcounties = [
            'Dagoretti North',
            'Dagoretti South',
            'Dagoretti Central',
            'Embakasi East',
            'Embakasi West',
            'Embakasi North',
            'Embakasi South',
            'Kamukunji',
            'Kasarani',
            'Kibera',
            'Langata',
            'Makadara',
            'Mathare',
            'Roysambu',
            'Ruaraka',
            'Starehe',

        ]

        for subcounty in nairobi_subcounties:
            SubCounty.objects.create(name=subcounty, county=nairobi)
