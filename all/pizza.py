from fastapi import FastAPI,HTTPException,Path
from pydantic import BaseModel,Field
from typing import List,Annotated,Optional
import json
from fastapi.responses import JSONResponse

app=FastAPI()
class pizza(BaseModel):
    order_id:Annotated[int,Field(...,description="enter your order id ")]
    customer_name:Annotated[str,Field(...,description="fill the customer name")]
    pizza_type:Annotated[str,Field(...,description="chose the pizza type ",example="Margherita")]
    size:str
    toppings:Annotated[List[str],Field(...,description="toppings name in the list",examples=["Extra Cheese","Olives"])]
    quantity:Annotated[int,Field(...,description="how much quantity")]
    price:Annotated[int,Field(...,description="total bill ")]

class customerupdate(BaseModel):
     customer_name:Annotated[Optional[str],Field(description="enter the name",default=None)]
     pizza_type:Annotated[Optional[str],Field(description="enter the pizza type",default=None)]
     size:Optional[str] = None
     toppings:Annotated[Optional[List[str]],Field(description="enter the pizza toppings ",examples=["Extra Cheese","Olives"],default=None)]
     quantity:Annotated[Optional[int],Field(description="how nuch quandity",default=None)]
     price:Annotated[Optional[int],Field(description="total bill",default=None)]
# load_data
def load_data():
    with open("pizzashop.json","r") as f:
        data=json.load(f)
    return data

# save the data
def save_data(data):
    with open("pizzashop.json","w") as f:
        json.dump(data,f)






# get request
@app.get("/")
def home():
    return {"message":"welcome to my pizza store"}

@app.get("/about")
def about():
    return {"message":"all customer detail "}


@app.get("/view")
def view():
    data=load_data()
    return data
@app.get("/customer/{customer_id}")
def view_customer_id(customer_id:int=Path(...,description="enter your order id",example="1")):
    data=load_data()
    for i in data["pizzashop"]:
        if i["order_id"]==customer_id:
            return i
        raise HTTPException(status_code=404,detail="data not found ")
    



# ctreate the data
@app.post("/create")
def create_customer(p:pizza):
    data=load_data()
    for i in data["pizzashop"]:
        if i["order_id"]==p.order_id:
            raise HTTPException(status_code=400,detail="order id already exists")
        data[p.order_id]=p.model_dump(exclude=["order_id"])
        save_data(data)
        return JSONResponse(status_code=201,content={"message":"file is successfuly created"})
    


# update the api details
@app.put("/edit/{order_id}")
def update_customer(order_id:int,update_cus:customerupdate):
    data=load_data()
    for i in data["pizzashop"]:
        if i["order_id"]== order_id:
            update_val=update_cus.model_dump(exclude_unset=True)
            i.update(update_val)
            save_data(data)
            return JSONResponse(status_code=200,content={"message":"data successful update"})


@app.delete("/delete/{order_id}")
def delete_data(order_id:int):
    data=load_data()
    for i in data["pizzashop"]:
        if i["order_id"] ==order_id:
              data["pizzashop"].remove(i)
              save_data(data)
              return JSONResponse(status_code=200,content={"message":"file successfuly delete"})
    raise HTTPException(status_code=404,detail="file not found")


