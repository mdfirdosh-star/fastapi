from fastapi import FastAPI,Path,HTTPException
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,Field
from typing import Annotated



app=FastAPI()
class product(BaseModel):
    id:Annotated[int,Field(...,description="product id",examples=[101,102])]
    name:Annotated[str,Field(...,description="name of product ",examples=["Laptop 101"])]
    brand:Annotated[str,Field(...,description="brand name of product",examples=["HP","Samsung"])]
    price:Annotated[int,Field(...,description="product price ")]
    stock:Annotated[int,Field(...,description="stock of product ")]

def load_data():
    with open ("data.json","r") as f:
       data=json.load(f)
    return data

def save_data(data):
     with open ("data.json","w") as f:
         json.dump(data,f)


@app.get("/")
def home():
    return {"message":"welcome to my labtop shop"}


@app.get("/about")
def about():
    return {"mseeage":"all laptop detail with prodict  id "}

@app.get("/view")
def view():
    data=load_data()
    return data


@app.get("/product/{product_id}")
def view_customer_details(product_id:int):
    data=load_data()
    for i in data["products"]:
        if i["id"]==product_id:
            return i
    raise HTTPException(status_code=404,detail="file not found ")

@app.post("/create")
def create_product(product:product):
    data=load_data()
    if any(p["id"] == product.id for p in data["products"]):  
         # for p in data["products"]:
         # if p["id"] == product.id :
         # any(...) built in function 
           raise HTTPException(status_code=400,detail="product is is already exist")
    
    data[product.id]=product.model_dump(exclude=["id"])
    save_data(data)
    return JSONResponse(status_code=201,content={"message":"file successfuly created"})


