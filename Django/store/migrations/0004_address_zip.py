# Generated by Django 4.0.4 on 2022-06-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.PositiveBigIntegerField(max_length=6, null=True),
        ),
    ]
