#imports
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy import text
from data.database import engine

#getting project dir
PROJECT_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = PROJECT_DIR / "frontend"

#creating application
app = FastAPI()
frontend = Jinja2Templates(directory=str(FRONTEND_DIR))
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

#gets count of products
def get_products_count():
    with engine.connect() as connection:
        count = connection.execute(text("SELECT COUNT(*) FROM products")).scalar_one()
    return count

#gets product tuple
def get_products():
    with engine.connect() as connection:
        products = connection.execute(text("SELECT * FROM products"))
        products = products.fetchall()
    return products

def get_one_product(product_id):
    with engine.connect() as connection:
        products = connection.execute(text(f"SELECT * FROM products WHERE id = {product_id}"))
        products = products.fetchall()
    return products

#in product tuple there is: id, name, image url, price, rating, rating count and url page

#main page
@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    products_count = get_products_count()
    products = get_products()
    return frontend.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "products_count": products_count,
                "products": products
                }
            )

@app.get("/products/{name}_{product_id}", response_class=HTMLResponse)
async def product_page(request: Request, name, product_id):     
    product = get_one_product(product_id)
    return frontend.TemplateResponse(
            request=request,
            name="product.html",
            context={
                "product": product
                }
            )

