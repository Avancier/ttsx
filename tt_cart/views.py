from django.shortcuts import render
from django.http import JsonResponse

from .models import CartInfo
# Create your views here.
def add(request):
	dict=request.GET
	gid=dict.get('gid')

	cart=CartInfo()
	cart.user_id=request.session.get('uid')
	cart.goods_id=int()

	cart.save()

	return

