# Generated by Django 4.2.1 on 2023-06-05 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_tbl_donar'),
        ('Recipient', '0007_delete_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('from_donar', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_donar', to='Guest.tbl_donar')),
                ('from_recipient', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_recipient', to='Guest.tbl_recipient')),
                ('to_donar', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_donar', to='Guest.tbl_donar')),
                ('to_recipient', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_recipient', to='Guest.tbl_recipient')),
            ],
        ),
    ]
