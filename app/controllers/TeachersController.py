from app.helpers import ResponseHandler 
from app.helpers import RequestValidator
 

from app.models.teacher import Teacher

class TeachersController:
    def add_teacher_controller(self, request_data):
        try:
           
            # Validate data
            RequestValidator.validate_add_teacher(request_data)

            # Add teacher
            result = Teacher.add_new_teacher(request_data)
        
        except Exception as e:
            return ResponseHandler.error(str(e))
        else:
            return {"Result": result}

    def edit_teacher_controller(self,request_data):
        try:
           
            # Validate data
            RequestValidator.validate_edit_teacher(request_data)

            # Add teacher
            result = Teacher.edit_teacher(request_data)
        
        except Exception as e:
            return ResponseHandler.error(str(e))
        else:
            return {"Result": result}

    def delete_teacher_controller(self,request_data):
        try:
           
            # Validate data
            RequestValidator.validate_delet_teacher(request_data)

            # Add teacher
            result = Teacher.delete_teacher(request_data)
        
        except Exception as e:
            return ResponseHandler.error(str(e))
        else:
            return {"Result": result}

