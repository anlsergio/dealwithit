import decimal

import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def payment(request):
    return render(request, 'payment/payment.html', {'key': settings.STRIPE_PUBLISHABLE_KEY})

@login_required
def charge(request):

    chosen_amount = request.POST.get("dropdown")

    if request.method == 'POST':
        try:
            charge = stripe.Charge.create(
                amount=chosen_amount,
                currency='usd',
                description='Dealwithit store charge',
                source=request.POST['stripeToken'],
                api_key = settings.STRIPE_SECRET_KEY
            )
            # Captures the instance object of the current logged user
            # And adds the chargeable ammount of credit
            # Stripe uses cent type ammount, so that's why we should divide it by 100 to convert it to decimal
            # Which is a more readable ammount type
            current_user = request.user
            current_user.profile.credit += decimal.Decimal(int(chosen_amount)/100)
            current_user.save()
        except stripe.error.CardError as ce:
            return False, ce
        return render(request, 'payment/charge.html')