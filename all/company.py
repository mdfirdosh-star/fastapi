from pydantic import BaseModel,Field
from typing import Dict,List,Annotated,Optional
from fastapi import FastAPI,HTTPException
from datetime import date,datetime,time
import json
from fastapi.responses import JSONResponse

app=FastAPI()
# pydantic use the data validatins and data_type validations 
class employee(BaseModel):
    id:Annotated[int,Field(...,description="all employees id and all employees id are unique")]
    name:Annotated[str,Field(...,description="employees name")]
    age : Annotated[int,Field(...,description="age of employees",gt=18,lt=61)]
    gender:Annotated[str,Field(...,description="chose the gender 'Male','female' ")]
    position:Annotated[str,Field(...,description="all employees position ",example="Software Engineer")]
    department:Annotated[str,Field(...,description="all employees department ",example="IT")]
    salary:Annotated[int,Field(...,description="all employees salary ")]
    is_active: bool 

class updateemployee(BaseModel):
    name:Annotated[Optional[str],Field(description="all employee name ",default=None)]
    age : Annotated[Optional[int],Field(description="all employee age ",default=None)]
    gender:Annotated[Optional[str],Field(description="all employee gender ",default=None)]
    position:Annotated[Optional[str],Field(description="all employee possitions",example="Software Engineer",default=None)]
    department:Annotated[Optional[str],Field(description="all employee daparment",example="IT",default=None)]
    salary:Annotated[Optional[int],Field(description="all employee possitions",default=None)]
    is_active:Annotated[Optional[bool],Field(default=True)]

def load_data():
    with open("employees.json","r") as f:
        data=json.load(f)
    return data
def save_data(data):
    with open("employees.json","w") as f:
         json.dump(data, f)


@app.get("/")
def home() :
    return {"message":"welcome to my TechNova Solutions Pvt Ltd"}
@app.get("/about")
def about():
    return {"message":"all employees detalis "}
@app.get("/view")
def view():
    data=load_data()
    return data
@app.get("/employee/{employee_id}")
def view_employee(employee_id:int):
    data=load_data()
    for i in data["employees"]:
        if i["id"]==employee_id:
            return i
    raise HTTPException(status_code=404,detail="file not found ")
     




#create the post api

@app.post("/create")
def create_company(c:employee):
    data=load_data()
    for i in data["employees"]:
        if i["id"]==c.id:
         # for p in data["products"]:
         # if p["id"] == product.id :
         # any(...) built in function 
             raise HTTPException(status_code=400,detail="product is is already exist")
    
        data[c.id]=c.model_dump(exclude=["id"])
        save_data(data)
        return JSONResponse(status_code=201,content={"message":"file successfuly created"})
    
# update the data 
@app.put("/edit/{employee_id}")
def update_emp(employee_id:int,employee_update:updateemployee):
    data=load_data()
    for i in data["employees"]:
        if i["id"] == employee_id:
           update_val = employee_update.model_dump(exclude_unset=True)
           i.update(update_val)
           save_data(data)
           return JSONResponse(status_code=200,content={"message":"data successfully update"})

        

        
