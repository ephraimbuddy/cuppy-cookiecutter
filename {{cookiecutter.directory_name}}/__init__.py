# -*- coding: utf-8 -*-

"""
Created on {% now 'local', '%Y-%m-%d' %}
:author: {{cookiecutter.full_name}} ({{cookiecutter.email}})
"""


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
    


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``cuppy_extender`` above to your ``cuppy.extenders`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """
    config.add_static_view('static-{{cookiecutter.project_slug}}', '{{cookiecutter.project_slug}}:static')

    config.scan(__name__)