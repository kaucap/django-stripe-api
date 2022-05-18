from django.views import generic
from app_shop.models import Item
import stripe
from django.urls import reverse
from django.http import JsonResponse
from decouple import config

stripe.api_key = config('STRIPE_SECRET_KEY')


class MainPage(generic.ListView):
    model = Item
    template_name = 'site/main_page.html'
    context_object_name = 'items'


def buy_item(request, pk):
    item = Item.objects.get(id=pk)
    site = "http://127.0.0.1:8000"
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.get_currency_display(),
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price * 100
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=site + reverse('success'),
        cancel_url=site + reverse('cancel'),
    )

    return JsonResponse({'session_id': session.id})


class ItemDetail(generic.DetailView):
    model = Item
    template_name = 'site/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = config('STRIPE_PUBLIC_KEY')
        return context


class SuccessView(generic.TemplateView):
    template_name = "site/success.html"


class CancelView(generic.TemplateView):
    template_name = "site/cancel.html"
