# Generated by Django 3.1.1 on 2020-10-20 02:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ExpenseManagement', '0006_auto_20201019_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('payDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('recursive', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('recursiveFrequency', models.CharField(choices=[('Weekly', 'Weekly'), ('BiWeekly', 'BiWeekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Semiannually', 'Semiannually'), ('Annually', 'Annually')], max_length=15, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
