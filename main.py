from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse,FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.user import user
from routes.products import products

app = FastAPI()

# Routers
app.include_router(user)
app.include_router(products)

# Archivos estaticos
app.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory="./templates")

#@app.get("/", response_class=HTMLResponse)
#def root(req: Request):
#  return template.TemplateResponse("index.html", {"request": req})
  
@app.get("/", response_class=HTMLResponse)
def raiz():
    html = "./templates/index.html"
    return FileResponse(html, status_code=200)