from fastapi import FastAPI,Path,HTTPException,Query
import json
import streamlit as st 
import requests
app=FastAPI()

# load the data 
def load_data():
    with open("patients.json","rb") as f:
      data=json.load(f)
    return data

@app.get("/")
def home ():
    return {"message":"welcome to my hospital "}

@app.get("/about")
def about():
    return {"message":"all pitent  delatl in my api"}

@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str=Path(...,description="all patient detail",example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="file not found ")


@app.get("/sort")
def sort_patient_details(sort_by:str=Query(...,description="sort the all detail"),order:str=Query(...,description="sort the value of method asc and desc"))
     
