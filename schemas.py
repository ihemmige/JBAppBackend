from marshmallow import Schema, fields

class JobSchema(Schema):
  company = fields.Str()
  title = fields.Str()
  location = fields.Str()
  salary = fields.Int()