# Generated by Django 4.2.1 on 2023-06-14 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_adminlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
