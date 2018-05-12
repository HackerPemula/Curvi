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
    def authenticate(binusianid, password):
        try:
            param = []
            param.append(binusianid)
            param.append(hash_password(password))
            
            user = User.objects.exec_sp_tosingle('bn_Warehouse_DoLogin', param)
            
            result = ""

            if user:
                result = User(BinusianId=user[0], Name=user[1], RoleId=user[2])
            
            return result

        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None