from django.utils.translation import ugettext_lazy as _
from django import forms
from datetime import date
from cartridge.shop.forms import OrderForm

from cartridge.shop.utils import (make_choices, set_locale, set_shipping,
                                  clear_session)


class WidgetNonameMixin(object):

    # taken from Widget class
    def build_attrs(self, extra_attrs=None, **kwargs):
        "Helper function for building an attribute dictionary."

        if 'name' in kwargs:
          del kwargs['name']

        attrs = dict(self.attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs


class NamelessTextInput(WidgetNonameMixin,forms.TextInput):
  pass

class NamelessSelect(WidgetNonameMixin,forms.widgets.Select):
  pass



class StripeOrderForm(OrderForm):
    """
    Derived order form that implements nameless cc and stripeToken inputs.

    Derived form class for Order model.  
    """
    # "required" is a core Field argument, and is used by the Field.clean method.
    # if required=False, then clean does not raise a ValdationError on empty values.
    # clean raises this error or returns a cleaned value 
    card_number = forms.CharField(label=_("Card number"),required=False, widget = NamelessTextInput(attrs={"data-stripe":"number"}) )

    card_expiry_month = forms.ChoiceField(label=_("Card expiry month"),
        initial="%02d" % date.today().month,
        choices=make_choices(["%02d" % i for i in range(1, 13)]), 
        required=False, 
        widget=NamelessSelect(attrs={"data-stripe":"exp-month"}))

    card_expiry_year = forms.ChoiceField(label=_("Card expiry year"), 
                                         required=False, 
                                         widget=NamelessSelect(attrs={'data-stripe':'exp-year'})
                                         )

    card_ccv = forms.CharField(label=_("CCV"), help_text=_("A security code, "
        "usually the last 3 digits found on the back of your card."), required=False, widget = NamelessTextInput(attrs={"data-stripe":"cvc"}))

    stripeToken = forms.CharField(widget=forms.HiddenInput())

    @classmethod
    def preprocess(cls, data):
        """
        A preprocessor for the order form data, insets stripeToken. 

        The default preprocessor that is called from super handles
        copying billing fields to shipping fields if "same" checked. StripeToken defaults to None.
        """
        data = super(StripeOrderForm,cls).preprocess(data)

        if ("stripeToken" in data) and (len(data["stripeToken"]) == 0):
            data["stripeToken"] = "None"

        return data

