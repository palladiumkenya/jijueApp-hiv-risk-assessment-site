# Generated by Django 4.1 on 2022-09-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveBigIntegerField()),
                ('gender', models.PositiveBigIntegerField()),
                ('county', models.CharField(max_length=100)),
                ('maritalStatus', models.PositiveBigIntegerField()),
                ('coupleDiscordant', models.PositiveBigIntegerField()),
                ('SexWithWoman', models.CharField(max_length=256)),
                ('SexWithMan', models.CharField(max_length=256)),
                ('condom_use', models.CharField(max_length=256)),
                ('sw', models.PositiveBigIntegerField()),
                ('pwid', models.PositiveBigIntegerField()),
                ('testedBefore', models.PositiveBigIntegerField()),
                ('presumedTB', models.PositiveBigIntegerField()),
                ('treatmentTB', models.PositiveBigIntegerField()),
                ('sti', models.CharField(max_length=100)),
                ('rapevictim', models.CharField(max_length=100)),
                ('HIVPrEP', models.CharField(max_length=100)),
                ('y_pred', models.CharField(max_length=30)),
            ],
        ),
    ]
