from django.db import models


class Business(models.Model):
    """
    业务线
    xindai
    xiaodai
    p2p
    crm
    cmis
    """
    name = models.CharField(max_length=10, verbose_name="业务线")


class Application(models.Model):
    """
    应用表
    core
    passport
    """
    pass
