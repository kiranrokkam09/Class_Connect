# Generated by Django 3.2.8 on 2023-03-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20230315_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='placed',
            field=models.CharField(max_length=100, null=True, verbose_name='placed'),
        ),
    ]