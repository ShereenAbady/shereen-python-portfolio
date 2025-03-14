from flask import current_app as app, request, render_template
from flask_restful import Api, Resource

from app.controllers.ClassController import ClassController
from app.controllers.TeachersController import TeachersController
from app.controllers.ClientController import ClientController


class Router:
    """Basic Routes Handler"""

    def init_app_routes(self):
        api = Api(app)
        api.add_resource(App,
                        "/test",
                        "/get/teachers",
                        "/classes/requestClass",
                        "/teachers/add",
                        "/teachers/edit",
                        "/teachers/delete",
                        "/clients/withdraw"
                         )

        @app.route("/admin")
        def admin_panel():
            return render_template("admin.html")   


class App(Resource):
    """Application Requests Routes Handler"""

    def get(self):
        
        route = request.path  
        teachers_controller = TeachersController()

        if route == "/get/teachers":
            return teachers_controller.get_teachers()

        return {"error": "Invalid route"}, 404

    def post(self):
        route = request.path  
        class_details_controller = ClassController()
        teachers_controller = TeachersController()
        client_actions_controller = ClientController()

        # Handle routes correctly
        if route == "/classes/requestClass":
            return class_details_controller.join_class_controller()
        elif route == "/teachers/add":
            return teachers_controller.add_teacher_controller()
        elif route == "/teachers/edit":
            return teachers_controller.edit_teacher_controller()
        elif route == "/teachers/delete":
            return teachers_controller.delete_teacher_controller()
        elif route == "/clients/withdraw":
            return client_actions_controller.withdraw_client_controller()

        return {"error": "Invalid route"}, 404  # Default response for unknown routes
