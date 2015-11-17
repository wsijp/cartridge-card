import stripe
from cartridge.shop import checkout
from cartridge.shop.models import Order
from project import settings

def my_payment_handler(request, order_form, order):
    """
    My payment handler - called when the final step of the
    checkout process with payment information is submitted. Implement
    your own and specify the path to import it from via the setting
    ``SHOP_HANDLER_PAYMENT``. This function will typically contain
    integration with a payment gateway. Raise
    cartridge.shop.checkout.CheckoutError("error message") if payment
    is unsuccessful.
    """

    stripe.api_key = settings.STRIPE_SECRET

    request.session["order"]["stripeToken"] = "transacted"

    token = order_form["stripeToken"].value()

    print request.POST

    total = int(order.total*100)
    currency = "AUD"

    error_msg = None   
    try:
      charge = stripe.Charge.create(amount=total,currency=currency,source=token,description="Example charge")
    except stripe.error.InvalidRequestError as e:
        # can refine error message based on e
#    if ("You cannot use a Stripe token more than once" in "%s"%e):
        error_msg = "An error has occurred. Please retry entering card details in step 2."

    else:
        if charge["paid"] is False:
            error_msg = "Payment did not succeed."

    if error_msg is not None:
        raise checkout.CheckoutError(error_msg)

    return charge["id"]

