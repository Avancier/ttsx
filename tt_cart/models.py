# coding=utf-8
from django.db import models

from tt_user.models import UserInfo
from product.models import GoodsInfo


# Create your models here.

class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
