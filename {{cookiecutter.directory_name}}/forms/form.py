from wtforms import validators
from wtforms import StringField
from cuppy.forms.content import ContentForm


class AddCustomContent(ContentForm):
    
    custom_attribute = StringField("Custom Attribute", validators=[validators.InputRequired(),
                                            validators.Length(min=10)] )