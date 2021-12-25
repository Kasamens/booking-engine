# Generated by Django 3.1.7 on 2021-12-23 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20211223_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blocked_listing', to='listings.listing')),
            ],
        ),
    ]
