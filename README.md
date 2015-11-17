# cartridge-card
Stripe integration for Mezzanine Cartridge based on the [Stripe tutorial by Larry Ullman](http://www.larryullman.com/series/processing-payments-with-stripe/)

Install instructions
--------------------

Add "cartridge-card" to INSTALLED_APPS in settings.py

Add to settings.py:

* STRIPE_SECRET = "your Stripe secret key"
* STRIPE_PUBLISHABLE = "your publishable key"
* SHOP_HANDLER_PAYMENT = "cartridge-cart.checkout.stripe_payment_handler"
* SHOP_CHECKOUT_FORM_CLASS = "cartridge-card.forms.StripeOrderForm"

Completion of the Cartridge checkout buying pages triggers the sending of e-mails. In development, to avoid errors and debug e-mails, add to settings.py:

* EMAIL_FAIL_SILENTLY = False
* EMAIL_HOST = "localhost"
* EMAIL_PORT = 1025

Also, running a simple debugging e-mail server from the command line helps avoid errors: 

python -m smtpd -n -c DebuggingServer localhost:1025
