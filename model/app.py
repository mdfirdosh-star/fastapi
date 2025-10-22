import json
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Annotated,Literal
from fastapi.responses import JSONResponse
import pickle 
import pandas as pd
import numpy as np





with open("model (3).pkl","rb") as f:
    model=pickle.load(f)


app=FastAPI()
class userinput(BaseModel):
    gender:Annotated[Literal["Male","Female"],Field(...,description="chose the options")]
    race_ethnicity:Annotated[Literal["group A", "group B", "group C", "group D", "group E"],Field(..., description="choose the option")]
    parental_level_of_education:Annotated[Literal["high school","some high school","some college","bachelor's degree","associate's degree","master's degree"],Field(...,description="chose the options")]
    lunch:Annotated[Literal["standard","free/reduced"],Field(...,description="chose the options")]
    math_score:Annotated[int,Field(...,description="enter your math_score")]
    reading_score:Annotated[int,Field(...,description="enter your reading_score")]
    writing_score:Annotated[int,Field(...,description="enter your writing_score")]


@app.post("/predict")
def predict_primium(data:userinput):
    input_data= pd.DataFrame([{
        "gender":data.gender,
         "race_ethnicity":data.race_ethnicity,
         "parental_level_of_education":data.parental_level_of_education,
         "lunch":data.lunch,
         "math_score":data.math_score,
         "reading_score":data.reading_score,
        "writing_score":data. writing_score
        }])
    prediction=model.predict(input_data)[0]
    if isinstance(prediction, (np.integer, np.floating)):
            prediction = prediction.item()
    return JSONResponse(status_code=200,content={"test preparation course":prediction})