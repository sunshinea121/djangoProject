# Generated by Django 3.1.4 on 2020-12-27 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idcs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='IDC名称')),
                ('phone', models.CharField(db_index=True, max_length=11, verbose_name='联系电话')),
                ('address', models.CharField(max_length=30, verbose_name='地址')),
                ('remark', models.CharField(blank=True, max_length=100, verbose_name='备注')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='联系人')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='机柜名称')),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idcs.idcs', verbose_name='所属IDC')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
