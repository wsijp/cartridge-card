// Based on code created by Larry Ullman (April 14, 2015), www.larryullman.com, @LarryUllman
// that is posted as part of the series "Processing Payments with Stripe"
// http://www.larryullman.com/series/processing-payments-with-stripe/

// This page is intended to be stored in a public "js" directory.

// This function is just used to display error messages on the page.
// Assumes there's an element with an ID of "payment-errors".
function reportError(msg) {
	// Show the error in the form:
	$('#payment-errors').text(msg).addClass('alert alert-error');
	// re-enable the submit button:
	$('.btn-primary').prop('disabled', false);
	return false;
}

// Assumes jQuery is loaded!
// Watch for the document to be ready:
$(document).ready(function() {

        // payment errors div is added from javascript:
        $(".checkout-form").prepend("<span id='payment-errors'></div>");

	// Watch for a form submission via the "Next" button:
	$("input[value=Next]").click(function(event) {

		// Flag variable:
		var error = false;

		// disable the submit button to prevent repeated clicks:
		$('.btn-primary').attr("disabled", "disabled");

		// Get the values:
		var ccNum = $('#id_card_number').val(), cvcNum = $('#id_card_ccv').val(), expMonth = $('#id_card_expiry_month').val(), expYear = $('#id_card_expiry_year').val();

		// Validate the number:
		if (!Stripe.card.validateCardNumber(ccNum)) {
			error = true;
		
			reportError('The credit card number appears to be invalid.');
		}

		// Validate the CVC:
		if (!Stripe.card.validateCVC(cvcNum)) {
			error = true;
			reportError('The CVC number appears to be invalid.');
		}

		// Validate the expiration:
		if (!Stripe.card.validateExpiry(expMonth, expYear)) {
			error = true;
			reportError('The expiration date appears to be invalid.');
		}

		// Validate other form elements, if needed!

		// Check for errors:
		if (!error) {
                    
			// Get the Stripe token:
			Stripe.card.createToken({
				number: ccNum,
				cvc: cvcNum,
				exp_month: expMonth,
				exp_year: expYear
			}, stripeResponseHandler);

		}
		
		// Prevent the form from submitting:
		return false;

	}); // Form submission

}); // Document ready.

// Function handles the Stripe response:
function stripeResponseHandler(status, response) {


	
	// Check for an error:
	if (response.error) {

		reportError(response.error.message);

	} else { // No errors, submit the form:

	  	var f = $(".checkout-form");

	  // Token contains id, last4, and card type:
	  	var token = response['id'];

	  // Insert the token into the form so it gets submitted to the server
	  // f.append("<input type='hidden' name='stripeToken' value='" + token + "' />");
		$("input[name=stripeToken]").val(token);

	  // Submit the form:
	  	f.get(0).submit();   
          
	}

} // End of stripeResponseHandler() function.
