from fastapi.staticfiles import StaticFiles


from fastapi import FastAPI


from src.routers import main_router
from src.routers.routes import routes_router
from src.templates import jinja_templates

# Setup App, static directory and routes
app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(main_router)


