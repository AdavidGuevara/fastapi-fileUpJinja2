from fastapi import APIRouter
from fastapi import Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

upload = APIRouter()

templates = Jinja2Templates(directory="./templates")


@upload.get("/file-upload", response_class=HTMLResponse)
def get_basic_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@upload.post("/file-upload", response_class=HTMLResponse)
async def post_basic_form(
    request: Request,
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    file: UploadFile = File(...),
):
    print(f"email: {email}")
    print(f"username: {username}")
    print(f"password: {password}")
    print(f"Filename: {file.filename}")

    # save the file
    with open(f"images/{file.filename}", "wb") as my_file:
        contents = await file.read()
        my_file.write(contents)
        my_file.close()

    return templates.TemplateResponse("form.html", {"request": request})
