# Generated by Django 4.2.1 on 2023-06-14 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donar', '0005_tbl_appointments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_paymentrecord',
        ),
    ]
