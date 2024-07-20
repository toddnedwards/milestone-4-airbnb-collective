from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle webhooks in stripe """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ handle payment intent.succeeded webhook from stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """ handle payment intent.payment_failed webhook from stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)