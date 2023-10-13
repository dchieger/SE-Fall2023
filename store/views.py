from django.utils import timezone
from django.shortcuts import render
from .models import Order, OrderItem

from django.shortcuts import render, redirect, reverse
from .models import Order, User, Product



def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    context = {'order': order}
    return render(request, 'order.html', context)

def create_order(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        user = User.objects.get(id=user_id)
        product_ids = request.POST.getlist('products')
        products = Product.objects.filter(id__in=product_ids)
        address_line1 = request.POST.get('address_line1')
        address_line2 = request.POST.get('address_line2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        country = request.POST.get('country')

        order = Order.objects.create(
            user=user,
            date_ordered=timezone.now(),
            complete=False,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            zip=zip,
            country=country,
        )

        return redirect(reverse('order_detail', args=[order.id]))

    else:
        users = User.objects.all()
        products = Product.objects.all()
        return render(request, 'create_order.html', {'users': users, 'products': products})