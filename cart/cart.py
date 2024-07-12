class Cart():
    def __init__(self, request):
        self.session = request.session

        # get current id if it already exists
        cart = self.session.get('session_id')

        # create id if it doesn't exist
        if 'session_id' not in request.session:
            cart = self.session['session_id'] = {} 

        # make cart available on all pages of site
        self.cart = cart