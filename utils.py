from uuid import UUID
from flask import abort, jsonify
import json
def arg2jsonstr(**kwargs):
    return json.dumps(kwargs)

def validate_uuid(uuid_string,ver):
    try:
        val = UUID(uuid_string.replace('-', ''), version=ver)
    except ValueError:
        # If it's a value error, then the string 
        # is not a valid hex code for a UUID.
        return False
    return val.hex == uuid_string.replace('-','')

def uuid_notvalidate(objstr, field):
    msg = "{}.{} should be validated uuid".format(objstr, field)
    return jsonify(message=msg), 501

def uuid_notfound(objstr, field):
    msg = "it can not find {} by uuid{}.".format(objstr, field)
    return jsonify(message=msg), 404

def already_exist(objstr, field):
    msg = "{} with ID{} already exist.".format(objstr, field)
    return jsonify(message=msg), 409
