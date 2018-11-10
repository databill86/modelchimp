# Generated by Django 2.0.6 on 2018-07-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelchimp', '0025_machinelearningmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinelearningmodel',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'In Process'), (2, 'Completed')], default=2, max_length=5, null=True),
        ),
    ]