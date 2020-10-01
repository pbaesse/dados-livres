from wtforms.validators import ValidationError


class Unique(object):
    def __init__(self, Model, field, message=u'Este elemento já existe.'):
        self.message = message
        self.Model = Model
        self.field = field

    def __call__(self, wtforms, field):
        check = self.Model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)
