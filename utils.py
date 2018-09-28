from uuid import UUID
from flask import abort
import json
def arg2jsonstr(**kwargs):
    return json.dumps(kwargs)

def validate_uuid(uuid_string,ver):
    try:
        val = UUID(uuid_string, version=ver)
    except ValueError:
        # If it's a value error, then the string 
        # is not a valid hex code for a UUID.
        return False
    return val.hex == uuid_string.replace('-','')

def uuid_error(objstr, field):
    message = "{}.{} should be validated uuid".format(objstr, field)
    return abort(501, message)