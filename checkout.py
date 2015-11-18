import stripe
from cartridge.shop import checkout
from cartridge.shop.models import Order
from project import settings

def stripe_payment_handler(request, order_form, order):
    """
    This payment handler is called when the final step of the
    checkout process with payment information is submitted. Implement
    your own and specify the path to import it from via the setting
    ``SHOP_HANDLER_PAYMENT``. This function will typically contain
    integration with a payment gateway. Raise
    cartridge.shop.checkout.CheckoutError("error message") if payment
    is unsuccessful.
    """

    stripe.api_key = settings.STRIPE_SECRET

    request.session["order"]["stripeToken"] = "transacted" # not sure if this persists

    token = order_form["stripeToken"].value() # obtain the Stripe token

    total = int(order.total*100)  # Stripe takes payments in cents 
    currency = "AUD"

    # for Stripe metadata:
    email = order.billing_detail_email
    order_id = order.id

    error_msg = None   
    try:
      charge = stripe.Charge.create(amount=total,
                                   currency=currency,
                                   source=token,
                                   description="Example charge",
                                   metadata = {"order_id":order_id,"email":email}
      )

    except stripe.error.CardError, e:
      # Since it's a decline, stripe.error.CardError will be caught
      body = e.json_body
      err  = body['error']

      print "Status is: %s" % e.http_status
      print "Type is: %s" % err['type']
      print "Code is: %s" % err['code']
      # param is '' in this case
      print "Param is: %s" % err['param']
      print "Message is: %s" % err['message']

      error_msg = "A card error has occurred. %s"%err['message']

    except stripe.error.RateLimitError, e:
      # Too many requests made to the API too quickly
      error_msg = "Too many requests. Try again after a short while."
  
    except stripe.error.InvalidRequestError, e:
      # Invalid parameters were supplied to Stripe's API
      error_msg = "Invalid parameters were supplied."
  
    except stripe.error.AuthenticationError, e:
      # Authentication with Stripe's API failed
      # (maybe you changed API keys recently)
      error_msg = "Authentication failed. Contact site admin."
     
    except stripe.error.APIConnectionError, e:
      # Network communication with Stripe failed
      error_msg = "A network problem occurred."

    except stripe.error.StripeError, e:
      # Display a very generic error to the user, and maybe send
      # yourself an email
      error_msg = "A technical problem occurred."

    except stripe.error.InvalidRequestError as e:
      # Display a very generic error to the user, and maybe send
      # yourself an email
      error_msg = "A technical problem occurred."

    except Exception, e:
      # Something else happened, completely unrelated to Stripe
      error_msg = "A technical problem occurred."

    else:
        if charge["paid"] is False:
            error_msg = "Payment did not succeed."

    if error_msg is not None:
        raise checkout.CheckoutError(error_msg)

    print charge

    return charge["id"]

