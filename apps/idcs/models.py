from django.db import models
from django.contrib.auth.models import User


class Idcs(models.Model):
    """
    Idc模型
    """
    name = models.CharField(max_length=10, unique=True, verbose_name="IDC名称")
    person = models.ForeignKey(to=User)


class Cabinet(models.Model):
    """
    机柜模型
    """
    pass


