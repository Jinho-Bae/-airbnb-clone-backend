# Generated by Django 4.1.3 on 2022-12-02 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('price_per_night', models.PositiveIntegerField(help_text='Positive Numbers only', verbose_name='Price')),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=140)),
                ('pets_allowed', models.BooleanField(default=True, help_text='Does this house allow pets?', verbose_name='Pets Allowed?')),
            ],
        ),
    ]
