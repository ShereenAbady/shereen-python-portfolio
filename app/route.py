
from flask import current_app as app, request
from flask_restful import Api, Resource

from app.controllers.ClassController import ClassController
from app.controllers.TeachersController import TeachersController
from app.controllers.ClientController import ClientController


class Router:
    """Basic Routes Handler"""

    def init_app_routes(self):
        api = Api(app)
        api.add_resource(
            App,

            "/test",
            "/classes/requestClass",
            "/teachers/add",
            "/teachers/edit",
            "/teachers/delete",
            "/clients/withdraw"
          
        )

        
class App(Resource):
    """Application Requests Routes Handler"""


    def post(self):
        route = request.url_rule.rule
        
        class_details_controller = ClassController()
        teachers_controller = TeachersController()
        client_actions_controller = ClientController()
        
        # Handle routes 
        if route == "/classes/requestClass":
            return class_details_controller.join_class()
        if route == "/teachers/add":
            return teachers_controller.add_teacher()
        if route == "/teachers/edit":
            return teachers_controller.edit_teacher()
        if route == "/teachers/delete":
            return teachers_controller.delete_teacher()
        if route == "/clients/withdraw":
            return client_actions_controller.withdraw_client()
        
        return {"error": "Invalid route"}, 404  # Default response for unknown routes
