from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from cuppy.models import Document


class CustomContent(Document):

    " CustomContent adds custom_attribute to content"
    __tablename__ = 'customcontent'
    id = Column(Integer, ForeignKey('documents.id'), primary_key=True)
    custom_attribute = Column(Unicode)

    def __init__(self, custom_attribute='', **kwargs):

        super().__init__(**kwargs)

        self.custom_attribute = custom_attribute


    @property
    def add_route_name(self):
        return "add_custom_content"
    
    @property
    def edit_route_name(self):
        return "edit_custom_content"
    
    @property
    def delete_route_name(self):
        return "delete_custom_content"

    @property
    def verbose_name(self):
        return "CustomContent"   
