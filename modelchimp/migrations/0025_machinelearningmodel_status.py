# Generated by Django 2.0.6 on 2018-07-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelchimp', '0024_auto_20180702_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinelearningmodel',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'In Process'), (2, 'Completed')], default='', max_length=5, null=True),
        ),
    ]