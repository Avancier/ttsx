# coding=utf-8
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import TypeInfo, GoodsInfo


# Create your views here.

def index(request):
    type_list = TypeInfo.objects.all()
    list = []
    for typeinfo in type_list:
        list.append({
            'type': typeinfo,
            'list_new': typeinfo.goodsinfo_set.order_by('-id')[0:4],
            'list_check': typeinfo.goodsinfo_set.order_by('-gclick')[0:3]
        })
    context = {'title': '首页', 'cart': '1', 'list': list}
    return render(request, 'tt_product/index.html', context)


def list_product(request, type_id, page_index, order_by):
    typeinfo = TypeInfo.objects.get(pk=type_id)
    #    order_by = request.GET.get('order_by',1)
    order_bystr = '-id'
    if order_by == '2':
        order_bystr = 'gprice'
    elif order_by == '3':
        order_bystr = '-gclick'

    list = typeinfo.goodsinfo_set.order_by(order_bystr)
    list_new = typeinfo.goodsinfo_set.order_by('-id')[0:3]

    paginator = Paginator(list, 10)

    page_index = int(page_index)
    if page_index <= 0:
        page_index = 1
    if page_index >= paginator.num_pages:
        page_index = paginator.num_pages

    page = paginator.page(int(page_index))

    plist = paginator.page_range
    if paginator.num_pages > 5:
        if page_index <= 2:
            plist = range(1, 6)
        elif page_index >= paginator.num_pages - 1:
            plist = range(paginator.num_pages - 4, paginator.num_pages + 1)
        else:
            plist = range(page_index - 2, page_index + 3)

    context = {'title': '列表页', 'cart': 1,
               'type': typeinfo, 'page': page, 'pindex_list': plist,
               'order_by': order_bystr, 'list_new': list_new}
    return render(request, 'tt_product/list.html', context)


def detail(request, gid):
    try:
        goods = GoodsInfo.objects.get(pk=gid)

        goods.gclick += 1
        goods.save()

        list_new = goods.gtype.goodsinfo_set.order_by('-id')[0:2]

        context = {'title': '详细页', 'cart': '1', 'goods': goods, 'list_new': list_new}
        return render(request, 'tt_product/detail.html', context)
    except:
        return render(request, '404.html')


from haystack.generic_views import SearchView


class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['title'] = '搜索结果'
        context['cart'] = '1'
        context['isleft'] = '0'
        return context
