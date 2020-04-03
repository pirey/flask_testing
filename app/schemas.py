from marshmallow import Schema, fields as f, ValidationError, EXCLUDE

class ItemSchema(Schema):
    id = f.Integer()
    name = f.String(required=True)
    salary = f.Decimal(required=True, as_string=True)
