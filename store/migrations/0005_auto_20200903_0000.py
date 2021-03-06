# Generated by Django 3.0.8 on 2020-09-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='BookLanguage',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ISBN',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='PublicationCountry',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Publisher',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
