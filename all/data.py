from fastapi import FastAPI,HTTPException,Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
import json
from typing import Annotated,Literal,Optional

app=FastAPI()

class patient(BaseModel):
    id:Annotated[str,Field(...,description="id of tha all patient ",examples=["P001"])]
    name:Annotated[str,Field(...,description="name of the patient")]
    ciry:Annotated[str,Field(...,description="city name where patient living")]
    age:Annotated[int,Field(...,gt=0,lt=120,description="patient age ")]
    gender:Annotated[Literal["male","femail","other"],Field(...,description="gender of the patient ")]
    hight:Annotated[float,Field(...,gt=0,description="higest of the patient mts")]
    weight:Annotated[float,Field(...,description="weight of patient kgs")]
    
    
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.hight**2),2)
        return bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return "underweight"
        elif self.bmi <25:
            return "Normal"
        elif self.bmi<30:
            return "Normal"
        else:
            return "obse"

class patientupdate(BaseModel):
     name: Annotated[Optional[str], Field(default=None)]
     city: Annotated[Optional[str], Field(default=None)]
     age: Annotated[Optional[int], Field(default=None, gt=0)]
     gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
     height: Annotated[Optional[float], Field(default=None, gt=0)]
     weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_data():
    with open("patients.json","rb") as f:
       data= json.load(f)
    return data
   
def save_data(data):
    with open("patients.json","w") as f:
        json.dump(data,f)




@app.get('/')
def home():
    return {"message_1": "patient management system "}

@app.get ('/about')
def about():
    return{"message_2":"A fully function api to manage your patient recode "}

@app.get('/view')
def view():
    data=load_data()
    return data
@app.get("/patient/{patient_id}")
def view_patient(patient_id:str=Path(...,description="id of the patient the DB",example="P001")):
    # load all the patient
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    # httpexception use 
    




    
# create the post


@app.post("/create")
def create_patient(patient:patient):
    #load existing data
    data=load_data()
    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400,detail="patient already exist ")
     
    # new patient add to the database
    data[patient.id]=patient.model_dump(exclude=["id"])
    # save to the json file 
    save_data(data)
    return JSONResponse(status_code=201,content={"message":"patient created successfuly"})



# update the value 
@app.put("/edit/{patient_id}")
def update_patient(patient_id:str,patient_update:patientupdate):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="patient detali is not found")
    existing_patient_data=data[patient_id]
    updated_val = patient_update.model_dump(exclude_unset=True)
    for key,value in  updated_val.items():
        existing_patient_data[key] = value
    # existing patient create object
    existing_patient_data["id"]=patient_id
    patient_pydantic_obj_data=patient(**existing_patient_data)

    #pydantic to dict 
    existing_patient_data= patient_pydantic_obj_data.model_dump(exclude="id")
    data[patient_id]=existing_patient_data
    save_data(data)
    return JSONResponse(status_code=200,content={"message":"patient updated"})

# delete the data

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code="404",detail="patient detail is not found")
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200,content={"message":"patient detail is deleted"})