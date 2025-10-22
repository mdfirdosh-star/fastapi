import json
from pydantic import BaseModel,Field
from typing import Annotated,Optional
from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse

app=FastAPI()


def load_data():
    with open ("ice_cream_shop.json","r") as f:
        data=json.load(f)
    return data
def save_data(data):
     with open ("ice_cream_shop.json","w") as f:
             json.dump(data,f)

class ice_cream_shop(BaseModel):
    id:Annotated[int,Field(...,description="enter the ice_cream id ")]
    name:Annotated[str,Field(...,description="enter the ice_creame name",example="Vanilla bliss" )]
    flavor:Annotated[str,Field(...,description="enter the ice_creame name",example="Vanilla")]
    price:Annotated[int,Field(...,description="enter the ice_cream price ")]
    stock:Annotated[int,Field(...,description="all ice_cream stock  ")]
    category:Annotated[str,Field(...,description="enter the ice_creame name",example="Cup")]


class icecreamupdate(BaseModel):
    name:Annotated[Optional[str],Field(description="enter the ice cream name",default=None,example="Vanilla bliss")]
    flavor:Annotated[Optional[str],Field(description="enter the ice cream flaver",default=None,example="Vanilla")]
    price:Annotated[Optional[int],Field(description="enter the ice cream price ",default=None)]
    stock:Annotated[Optional[int],Field(description="enter the ice cream stock ",default=None)]
    category:Annotated[Optional[str],Field(description="enter the category",default=None,example="Cup")]



@app.get("/")
def home():
    return {"message":"welcome to my ice_cream shop "}

    

@app.get("/about")
def about():
    return {"message":" all ice_cream datail after in view "}


@app.get("/view")
def view():
    data=load_data()
    return data 

@app.get("/view/{i_id}")
def view_id(i_id:int):
    data=load_data()
    for i in data["icecream_shop"]:
        if i["id"]==i_id:
            return i
    raise HTTPException(status_code=404,detail="file not found ")



#post
@app.post("/create")
def create_api(ice:ice_cream_shop):
    data=load_data()
    if any(i["id"]==ice.id for i in data["icecream_shop"]):
        raise HTTPException(status_code=400,detail="id already in database") 
    data["icecream_shop"].append(ice.model_dump())
    save_data(data)
    return JSONResponse(status_code=201,content={"message":"file successful create "})


# put(update the ice cream details )

@app.put("/edit{ice_id}")
def update(ice_id:int,u:icecreamupdate):
    data=load_data()
    for i in data["icecream_shop"]:
        if i["id"]==ice_id:
            update_val=u.model_dump(exclude_unset=True)
            i.update(update_val)
            save_data(data)
            return JSONResponse(status_code=200,content={"message":"file successful update "})
    

# delete the details 
@app.delete("/delete/{id}")
def delete_details(id:int):
    data=load_data()
    for i in data["icecream_shop"]:
        if i["id"]==id:
            data["icecream_shop"].remove(i)
            save_data(data)
            return JSONResponse(status_code=200,content={"message":"file successful delete"})