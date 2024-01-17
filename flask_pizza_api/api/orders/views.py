from flask_restx import Resource,Namespace


order_namespace=Namespace('order',description="namespace for order")


@order_namespace.route('/orders')
class OrderGetCreate(Resource):

    def get(self):
        """
            Get all orders
        """
        pass


    def post(self):
        """
           Place a new order
        """
        pass


@order_namespace.route('/order/<int:order_id>')

class GetUpdateDelete(Resource):

    def get(self,order_id):
        """
           Update an order with id
        """
        pass
    
    def delete(self,order_id):
        """
           Delete an order with id 
        """
        pass

@order_namespace.route('/order/<int:user_id>/order/<int:order_id>/')
class GetSpecificOrderByUser(Resource):
    def get(self,user_id,order_id):
        """
           Get user's specific order
        """
        pass

@order_namespace.route('/user/<int:user_id>/orders')
class UserOrderByUser(Resource):

    def get(self,user_id):
        """
           Get all orders by a specific
        """

        pass

@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):

    def patch(self,order_id):
        """
           update an order's status
        """

        pass


                       
