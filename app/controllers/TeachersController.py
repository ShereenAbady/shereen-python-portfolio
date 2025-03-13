from flask import request, jsonify
from app.helpers import ResponseHandler, RequestValidator
from app.models.teacher import Teacher


class TeachersController:
    def get_teachers(self):
        try:
            tech_model = Teacher()
            print('heree')
            teachers = tech_model.get_all_teachers()
            return ({"teachers": teachers})
        except Exception as e:
            return ResponseHandler.error(str(e))

    def add_teacher_controller(self):
        try:
            request_data = request.get_json()  
            RequestValidator.validate_add_teacher(request_data)

            tech_model = Teacher()
            result = tech_model.add_new_teacher(request_data)

            return jsonify({"Result": result})
        except Exception as e:
            return ResponseHandler.error(str(e))

    def edit_teacher_controller(self):
        try:
            request_data = request.get_json()  # ✅ Fix: Get JSON from request
            RequestValidator.validate_edit_teacher(request_data)

            tech_model = Teacher()
            result = tech_model.edit_teacher(request_data)

            return jsonify({"Result": result})
        except Exception as e:
            return ResponseHandler.error(str(e))

    def delete_teacher_controller(self):
        try:
            request_data = request.get_json()  # ✅ Fix: Get JSON from request
            RequestValidator.validate_delet_teacher(request_data)

            tech_model = Teacher()
            result = tech_model.delete_teacher(request_data)

            return jsonify({"Result": result})
        except Exception as e:
            return ResponseHandler.error(str(e))
