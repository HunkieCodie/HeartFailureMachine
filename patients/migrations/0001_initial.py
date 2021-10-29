# Generated by Django 3.2.8 on 2021-10-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('anaemia', models.BooleanField(default=False)),
                ('ejection_fraction', models.FloatField()),
                ('creatinine_phosphokinase', models.FloatField()),
                ('diabetes', models.BooleanField(default=False)),
                ('high_blood_pressure', models.BooleanField(default=False)),
                ('platelets', models.FloatField()),
                ('serum_creatinine', models.FloatField()),
                ('serum_sodium', models.FloatField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('smoking', models.BooleanField(default=False)),
                ('time', models.PositiveIntegerField()),
            ],
        ),
    ]