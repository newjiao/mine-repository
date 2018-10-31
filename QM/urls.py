from django.conf.urls import url, include
from django.core.paginator import Paginator
from django.shortcuts import render

import xadmin as admin
import api

from content.models import Category, Book


def to_index(request):
    # 查询一级分类
    cates = Category.objects.filter(parent__isnull=True).all()

    # 获取cid分类id
    cate_id = int(request.GET.get('cid', 0))
    if cate_id:
        books = Book.objects.filter(category__parent_id=cate_id).all()
    else:
        books = Book.objects.filter().all()

    paginator = Paginator(books, per_page=4)  # 分页器

    # 获取page参数值
    pager = paginator.page(request.GET.get('page', 1))  # 获取第一页

    return render(request, 'index.html', locals())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^book/', include('content.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(api.router.urls)),
    url(r'', to_index),
]
