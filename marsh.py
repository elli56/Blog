from marshmallow import Schema, fields


class EntrieSchema(Schema):
    id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    content = fields.Str()
    date = fields.DateTime()



    












