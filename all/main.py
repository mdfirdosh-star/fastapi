# use path 
from fastapi import FastAPI,Path,HTTPException,Query
import json

app = FastAPI()
# joson function load 
def load_data():
    with open("patients.json","rb") as f:
       data= json.load(f)
    return data


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
    raise HTTPException(status_code=404 ,detail="patient not found" )
    # use query parameter 
@app.get('/sort')
def sort_patient(sort_by:str=Query(...,description="sort on the basic of higest,weight ,bmi "),order:str=Query("asc"),description="sort by assinding and desciending order"):
     valid_field=["hight","weight","bmi"]
     if sort_by not in valid_field:
         raise HTTPException(status_code=400,detail=f"invalid felid select from valid {valid_field}")
     if order not in["asc","desc"]:
         raise HTTPException(status_code=400,detail="invalid felid select from valid : select 'asc',and 'desc' ")
     data=load_data()
     sort_order = True if order=='desc' else False
     sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
     return sorted_data
     