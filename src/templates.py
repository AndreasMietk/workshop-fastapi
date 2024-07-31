from fastapi.templating import Jinja2Templates
from fastapi import Request

jinja_templates = Jinja2Templates(directory="templates")


def render_template(template_name: str, request: Request, **context):
    """
    Helper to render templates from /templates directory with jinja
    """
    return jinja_templates.TemplateResponse(name=template_name, context={"request": request, **context})
