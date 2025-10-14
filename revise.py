from pydantic import BaseModel
from typing import List,Dict 

class student(BaseModel):
    name:str
    age:int
    mob:Dict[str,int]
def details(student:student):
    print(student.name)
    print(student.age)
    print(student.mob)
info_detail={"name":"md firdosh","age":20,"mob":{"phone":8980999}}
s=student(**info_detail)
details(s)
print("-----------------------------------")




print()
from pydantic import BaseModel,Field, EmailStr,AnyUrl
from typing import List,Dict,Annotated,Optional

class student(BaseModel):
    name:Annotated[str,Field(description="type the name is maximum 50 length ",examples=["firdosh"],title="enter the name ")]
    age:Annotated[int,Field(gt=0,lt=120)]
    mob:Dict[str,int]
    game_name:Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    email: EmailStr
def details(student:student):
    print(student.name)
    print(student.age)
    print(student.mob)
    print(student.game_name)
    print(student.email)
    
info_detail={"name":"md firdosh","age":20,"mob":{"phone":8980999},"game_name":["crickel,football"],"email":"md@gmail.com"}
s=student(**info_detail)
details(s)


