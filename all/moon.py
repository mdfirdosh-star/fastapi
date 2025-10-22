from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class customer(BaseModel):
    name:str
    age:int
    email:str
def customer_insert(customer:customer):
    print(customer.name)
    print(customer.age)
    print(customer.email)
customer_detail={"name":"md firdosh alam","age":20,"email":"mdfirdoshalam851202@gmail.com"}

p=customer(**customer_detail)
customer_insert(p)

print()
print("----------------------------------------")




# from pydantic import BaseModel,EmailStr,AnyUrl
# from typing import List,Dict

# class patient(BaseModel):
#     name:str
#     age:int
#     email:EmailStr
#     weight:float
#     married:bool
#     allergies:List[str]# is ko use karnay ky ley ham typing module sy list import kartay hai 
#     contact_details:Dict[str,str]
# def insert_patient(patient:patient):
    
#     print(patient.name)
#     print(patient.age)
#     print(patient.email)
#     print(patient.weight)
#     print(patient.married)
#     print(patient.allergies)
#     print(patient.contact_details)
#     print("insert data in database ")
   
# patient_info={"name":"firdosh","age":90,"email":"md@gamil.com","weight":75.5,"married":True,"allergies":["khasi","jukham"],"contact_details":{"mob":"78787"}}

# # distnuary always unpacked 
# p_2=patient(**patient_info)
# insert_patient(p_2)
# print()
# print()












from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated 
class patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="name of the patient",description="name char is less then 50 ",examples=["firdosh"])]
    age:Annotated[int,Field(gt=0 ,lt=120 )]
    email:EmailStr
    weight:Annotated[float,Field(gt=0)]
    married:Annotated[bool,Field(default=None)]
    allergies:Annotated[Optional[List[str]],Field(max_length=5)]
    contact_details:Dict[str,str]
    # linkdin_url=AnyUrl
def insert_patient(patient:patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    # print(patient.linkdin_url)
    print("insert data in database ")
   
patient_info={"name":"firdosh","age":90,"email":"md@gamil.com","weight":75.5,"married":True,"allergies":["khugli"],"contact_details":{"mob":"78787"}}

# distnuary always unpacked 
p_2=patient(**patient_info)
insert_patient(p_2)
print("----------------------")
print()





# use of field validator 
from pydantic import BaseModel,EmailStr,field_validator
from typing import List,Dict

class patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    mob:Dict[str,int]
    # use of field_validator 
    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        valid_detali=["hdfc.com","icici.com"]
        user_email=value.split("@")[-1]
        if user_email  not in valid_detali:
            raise ValueError("not a valid")
        return value
    

    @field_validator("name")
    @classmethod
    def name_validator(cls,value):
         return value.title()
def insert_value(patient:patient):
        print(patient.name)
        print(patient.age)
        print(patient.email)
        print(patient.mob)
info_detail={"name":"md firdosh alam","age":20,"email":"md@hdfc.com","mob":{"mob":90898788}}
p=patient(**info_detail)
insert_value(p)
print()
print()



from pydantic import BaseModel,EmailStr,field_validator,model_validator
from typing import List,Dict

class patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    mob_details:Dict[str,int]
    # use of model_validator
    @model_validator(mode="after")
    @classmethod
    def validator_emergency_contact(cls,model):
        if model.age >50 and "emergency" not in model.mob_details:
             raise ValueError("patient older then 60 must an emergency contact")
        return model

def insert_value(patient:patient):
        print(patient.name)
        print(patient.age)
        print(patient.email)
        print(patient.mob_details)
info_detail={"name":"md firdosh alam","age":65
             ,"email":"md@hdfc.com","mob_details":{"mob":90898788,"emergency":29202020}}
p=patient(**info_detail)
insert_value(p)