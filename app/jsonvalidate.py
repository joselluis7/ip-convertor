
from jsonschema import validate

ip_schema = {
        "title": "Login",
        "type": "object",
        "required": [ "ipValue", "maskValue" ],
        "properties": {
            "ipValue": {
                "type": "string"
            },
            "maskValue": {
                "type": "string"
            }
          }
        }

def validate_data(data):
    if not validate(data, ip_schema):
        return False

    return True