from app.helpers import ResponseHandler
from app.helpers import RequestValidator
from app.models import clients




class ClientController:
    def withdraw_client_controller(self,request_data):
        try:
            # Validate data
            RequestValidator.validate_withdraw_client(request_data)

            # Process client withdrawal
            result = clients.withdraw_client(request_data)

        except Exception as e:
            return ResponseHandler.error(str(e))
        else:
            return {"Result": result}
        
