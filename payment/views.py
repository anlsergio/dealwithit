import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



@login_required
def payment(request):
    return render(request, 'payment/payment.html', {'key': settings.STRIPE_PUBLISHABLE_KEY})

@login_required
def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Dealwithit store charge',
            source=request.POST['stripeToken'],
            api_key = settings.STRIPE_SECRET_KEY
        )
        return render(request, 'payment/charge.html')