# Generated by Django 3.0.5 on 2020-04-30 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=100)),
                ('calories', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
