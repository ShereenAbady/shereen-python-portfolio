from app.helpers import ResponseHandler
from app.helpers import RequestValidator
from app.models import classes

class ClassController:
    def join_class_controller(self, request_data):
        try:
            # Validate data
            RequestValidator.validate_join_class(request_data)

            # Process joining class
            result = classes.join_class(request_data)

        except Exception as e:
            return ResponseHandler.error(str(e))
        else:
            return {"Result": result}

