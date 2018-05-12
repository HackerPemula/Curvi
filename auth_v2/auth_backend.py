from auth_v2.auth_model import User
import logging
from importlib import import_module
from django.conf import settings
import uuid
import hashlib
 
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    
class AuthBackend(object):
    @staticmethod
    def authenticate(username, password):
        try:
            param = []
            param.append(username)
            param.append(hash_password(password))
            
            user = User.objects.exec_sp_tosingle('jh_Curvi_DoLogin', param)
            
            result = ""

            if user:
                result = User(StaffName=user[1], StaffUsername=user[2])
            
            return result

        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None