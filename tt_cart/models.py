from django.db import models

from tt.user.models import UserInfo
from tt.product.models import GoodsInfo
# Create your models here.

class CartInfo(models.Model):
	user = models.ForeginKey(UserInfo)
	goods = models.ForeginKey(GoodsInfo)
	count = models.IntegerField()

