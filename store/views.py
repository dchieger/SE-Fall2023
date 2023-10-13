from django.shortcuts import render
from .models import Order


def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    context = {'order': order}
    return render(request, 'order.html', context)