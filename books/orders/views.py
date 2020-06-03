import stripe
from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersPageView(TemplateView):

    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':

        customer = stripe.Customer.create(
        name='Jenny Rosen',
        address={
            'line1': '510 Townsend St',
            'postal_code': '98140',
            'city': 'San Francisco',
            'state': 'CA',
            'country': 'US',
        },
        )
                
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken'],
            customer = stripe.Customer.create(
                name='Jenny Rosen',
                address={
                    'line1': '510 Townsend St',
                    'postal_code': '98140',
                    'city': 'San Francisco',
                    'state': 'CA',
                    'country': 'US',
        },
        )
            
        )
        return render(request,'orders/charge.html')

