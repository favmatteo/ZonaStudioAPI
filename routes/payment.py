from fastapi import HTTPException, Request, Header
from fastapi.responses import RedirectResponse
from lib.app import app
import stripe
import json
import os

stripe.api_key = os.getenv("stripe_key")
DOMAIN = "http://127.0.0.1:5500/html/"


@app.post("/create-checkout-session")
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    "price": "price_1P2zpq05695ayY29TQpjD3Ij",
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=DOMAIN + "payment/success.html",
            cancel_url=DOMAIN + "payment/cancel.html",
        )
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Redirect the user to the provided URL
    response = RedirectResponse(checkout_session.url, status_code=303)
    return response
