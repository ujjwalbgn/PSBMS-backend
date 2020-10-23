# Generated by Django 3.1.2 on 2020-10-23 00:09

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('reminderDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('createDateTime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PayCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('payDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('recursive', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('recursiveFrequency', models.CharField(choices=[('Weekly', 'Weekly'), ('BiWeekly', 'BiWeekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Semiannually', 'Semiannually'), ('Annually', 'Annually')], max_length=15, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('dateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
        migrations.CreateModel(
            name='BillMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dueDateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('recursive', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True)),
                ('recursiveFrequency', models.CharField(choices=[('Weekly', 'Weekly'), ('BiWeekly', 'BiWeekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Semiannually', 'Semiannually'), ('Annually', 'Annually')], max_length=15, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
