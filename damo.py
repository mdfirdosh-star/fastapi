from fastapi import FastAPI,Path,HTTPException
import json


def load_data():
    with open ("data.json","rb") as f:
       data=json.load(f)
    return data

app=FastAPI()
@app.get("/")
def home():
    return {"message":"welcome to my labtop shop"}


@app.get("/about")
def about():
    return {"mseeage":"all laptop detail with custumer id "}

@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/customer/{customer_id}")
def view_customer(customer_id:str=Path(...,description="all customer detail in view "),exaple="101"):
    data=load_data()
    for i in data["products"]:
        if i["id"]==customer_id:
            return i
    raise HTTPException(status_code=404,detail="file not found ")

    



