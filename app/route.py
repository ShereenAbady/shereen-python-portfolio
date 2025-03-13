
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
        request_data = request.get_json()  # Extract JSON data from request
        
        class_details_controller = ClassController()
        teachers_controller = TeachersController()
        client_actions_controller = ClientController()
        
        # Handle routes 
        if route == "/classes/requestClass":
            return class_details_controller.join_class_controller(request_data)
        if route == "/teachers/add":
            return teachers_controller.add_teacher_controller(request_data)
        if route == "/teachers/edit":
            return teachers_controller.edit_teacher_controller(request_data)
        if route == "/teachers/delete":
            return teachers_controller.delete_teacher_controller(request_data)
        if route == "/clients/withdraw":
            return client_actions_controller.withdraw_client_controller(request_data)
        
        return {"error": "Invalid route"}, 404  # Default response for unknown routes
