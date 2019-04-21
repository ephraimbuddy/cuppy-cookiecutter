from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound
from cuppy.models import ObjectInsert
from {{cookiecutter.project_slug}}.models import CustomContent
from {{cookiecutter.project_slug}}.forms import AddCustomContent


@view_config(route_name="add_custom_content", renderer="{{cookiecutter.project_slug}}:templates/add_customcontent.mako", permission="add")
def add_customcontent(request):
    
    parent_id = request.matchdict['parent_id']
    if parent_id:
        parent_id = parent_id[0]
        parent = CustomContent.get_by_id(parent_id)
        if not parent:
            return HTTPNotFound()
    # If we have parent_id value, we are now sure that it's valid
    form=AddCustomContent(request.POST, meta={'csrf_context':request.session})
    if request.POST and form.validate():
        appstruct = form.data
        appstruct.pop('csrf_token')
        content= CustomContent(**appstruct)
        request.dbsession.add(content)
        event = ObjectInsert(CustomContent, request, parent_id)
        request.registry.notify(event)
        return HTTPFound(location = request.route_url('custom'))
    return dict(form=form, action_url= request.route_url('add_custom_content', parent_id=parent_id))


@view_config(route_name="edit_custom_content", renderer="{{cookiecutter.project_slug}}:templates/edit_customcontent.mako", permission="edit")
def edit_custom_content(request):
    custom_content = request.context.obj
    if not custom_content:
        return HTTPNotFound()
    form = AddCustomContent(request.POST, meta={'csrf_context':request.session}, obj=custom_content)
    
    if request.POST and form.validate():
        appstruct = form.data
        appstruct.pop("csrf_token")
        appstruct['slug'] = custom_content.change_slug(appstruct['slug'])
        for k, v in appstruct.items():
            setattr(custom_content, k, v)
        request.dbsession.merge(custom_content)
        event = ObjectUpdate(custom_content, request, parent_id=custom_content.parent_id)
        request.registry.notify(event)
        return HTTPFound(location = request.route_url('custom'))
    return dict(form=form, action_url=request.route_url("edit_custom_content", slug=doc.get_slug()), doc=doc)


@view_config(route_name="delete_custom_content", permission='edit')
def delete_custom_content(request):
    custom_content = request.context.obj
    if not custom_content:
        return HTTPNotFound()
    request.dbsession.delete(custom_content)
    event = ObjectDelete(custom_content, request,doc.parent_id)
    request.registry.notify(event)
    return HTTPFound(location = request.route_url('custom'))