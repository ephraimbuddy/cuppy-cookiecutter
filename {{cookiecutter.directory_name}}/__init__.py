# -*- coding: utf-8 -*-

"""
Created on {% now 'local', '%Y-%m-%d' %}
:author: {{cookiecutter.full_name}} ({{cookiecutter.email}})
"""
from pyramid.security import Allow
from pyramid.security import Authenticated
from pyramid.security import ALL_PERMISSIONS
from pyramid.httpexceptions import HTTPNotFound

from {{cookiecutter.project_slug}}.models import CustomContent
from cuppy.security import SITE_ACL

def cuppy_extender(settings):
    """ Add a line like this to your .ini file::

            cuppy.extenders =
                {{cookiecutter.project_slug}}.cuppy.extender

        to enable the ``{{cookiecutter.project_slug}}`` add-on.

    :param settings: cuppy configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' {{cookiecutter.project_slug}}'
    settings['cuppy.fanstatic.view_needed'] += ' {{cookiecutter.project_slug}}.fanstatic.css_and_js'
    settings['cuppy.content_config.add_content_options'] += ' {{cookiecutter.project_slug}}.content_config.add_content_options'
    


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``cuppy_extender`` above to your ``cuppy.extenders`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """
    
    config.add_route('add_custom_content', 'custom/create*parent_id', pregenerator = pregen)
    config.add_route("edit_custom_content", 'custom/*slug', factory=custom_factory)
    config.add_route("delete_custom_content", 'delete-custom/*slug', factory=custom_factory)
    config.add_route("view_custom_content", 'custom/*slug', factory=custom_factory)
    config.add_static_view('static-{{cookiecutter.project_slug}}', '{{cookiecutter.project_slug}}:static')

    config.scan(__name__)


def custom_factory(request):
    slug = request.matchdict['slug']
    slug = '/'.join(slug)
    customcontent = CustomContent.get_by_slug(slug)
    if customcontent is None:
        raise HTTPNotFound()
    return CustomContentResource(customcontent)
    

class CustomContentResource(object):
    def __init__(self,object):
       self.obj = object
        
    def __acl__(self):
        acl = SITE_ACL
        acl.append((Allow, str(self.obj.user.id),('edit','state_change')))
        return acl

def pregen(request, elements, kw):
    kw.setdefault('parent_id', '')
    return elements, kw