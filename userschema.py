from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    title = fields.String(required=True)
    year = fields.Integer(required=True)
    genre = fields.String(required=True)

