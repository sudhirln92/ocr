# Generated by Django 2.2.5 on 2021-06-25 16:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20210625_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete='models.CASCADE', to='poll.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
