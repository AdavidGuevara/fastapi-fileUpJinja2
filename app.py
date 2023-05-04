from fastapi import FastAPI
from routes.app_routes import upload
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="File upload server",
    description="FastAPI file Upload with jinja2 template",
    version="1.0",
)

app.include_router(upload)
app.mount("/static", StaticFiles(directory="static"), name="static")
