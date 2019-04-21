from pyramid.view import view_config
from {{cookiecutter.project_slug}}.models import CustomContent

@view_config(route_name="custom", renderer="cuppy:templates/derived/dashboard/page.mako", permission="add")
def custom(request):
    """ This view lists all the pages/contents on the site"""
    
    custom = request.dbsession.query(CustomContent).filter(CustomContent.parent==None).all()
    return dict(custom = custom)