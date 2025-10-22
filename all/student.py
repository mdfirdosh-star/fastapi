from fastapi import FastAPI,HTTPException,Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Annotated,Dict,Literal
import json

app=FastAPI()
class student(BaseModel):
    id:Annotated[int,Field(...,description="student id/roll_no/sid")]
    name:Annotated[str,Field(...,description="name of the students",max_length=50)]
    age:Annotated[int,Field(...,description="Age of the student",gt=0,lt=100)]
    gender:Annotated[str,Field(...,description="student gender 'male','female' ",examples=["Male"])]
    course:Annotated[str,Field(...,description="student course name ")]
    year:Annotated[str,Field(...,description="Student just started the course",examples=["2nd year"])]
    marks:Dict[str,int]
    attendance_percentage:Annotated[int,Field(...,description="student attendance_percentage ",gt=0,lt=100)]
    city:Annotated[str,Field(...,description="city name where student live ")]


def load_data():
    with open ("student.json","r") as f:
        data=json.load(f)
    return data
def save_data(data):
    with open("student.json","w") as f:
        json.dump(data,f)

@app.get("/")
def home():
    return {"message":"welcome to my api project"}
@app.get("/about")
def about():
    return {"message":"all student detils in my api"}
@app.get("/view")
def view():
     data=load_data()
     return data
@app.get("/student/{student_id}")
def view_student(student_id:int=Path(...,description="student id/roll_no/sid",example=1)):
    data=load_data()
    for i in data["students"]:
        if i["id"]==student_id:
            return i
        raise HTTPException(status_code=404,detail="file not found")
    



# post request 
@app.post("/create")
def create_student(student:student):
    data=load_data()
    if any(p["id"] == student.id for p in data["students"]):  
         # for p in data["products"]:
         # if p["id"] == product.id :
         # any(...) built in function 
           raise HTTPException(status_code=400,detail="product is is already exist")
    
    data[student.id]=student.model_dump(exclude=["id"])
    save_data(data)
    return JSONResponse(status_code=201,content={"message":"file successfuly created"})
