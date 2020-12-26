from django.db import models
from django.contrib.auth.models import User


class Idcs(models.Model):
    """
    Idc模型
    """
    name = models.CharField(max_length=10, unique=True, verbose_name="IDC名称")
    person = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="联系人")
    phone = models.CharField(db_index=True, verbose_name="联系电话")
    address = models.CharField(max_length=30, verbose_name="地址")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Cabinet(models.Model):
    """
    机柜模型
    """
    name = models.CharField(max_length=10, unique=True, verbose_name="机柜名称")
    idc = models.ForeignKey(to=Idcs,on_delete=models.CASCADE, verbose_name="所属IDC")


