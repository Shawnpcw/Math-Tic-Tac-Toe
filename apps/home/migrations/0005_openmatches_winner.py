# Generated by Django 2.1 on 2018-08-23 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
        ('home', '0004_auto_20180823_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='openmatches',
            name='winner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='winner_id', to='login_reg.User'),
        ),
    ]