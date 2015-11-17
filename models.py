

# uncomment the following the add a separate model and table containing returned stripe data

#from mezzanine.core.models import SiteRelated
#from django.db import models
#from cartridge.shop.models import Order

#from django.utils.translation import (ugettext, ugettext_lazy as _,
#                                      pgettext_lazy as __)

#class StripeOrder(SiteRelated):

#    order_id = models.ForeignKey(Order)
#    amount = models.IntegerField(blank=True, null=True)
#    stripe_id = models.CharField(_("Stripe ID"), max_length=100)

#    currency = models.CharField(_("Currency"), max_length=4)
#    paid = models.BooleanField()
