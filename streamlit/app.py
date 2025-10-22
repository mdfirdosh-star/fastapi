import streamlit as st
import requests
import json

st.title("welcome to my TechNova Solutions Pvt Ltd company")
st.image("https://content3.jdmagicbox.com/comp/indore/b5/0731px731.x731.220903214353.h9b5/catalogue/technovaa-software-and-hardware-solution-pvt-ltd-indore-software-companies-d0k3pnrr75.jpg")
st.sidebar.title("all options for user.choise the currect options ")
options=st.sidebar.radio("chose the options",["Home","About","View","View_employee","creat_details","update_details"])
url="http://127.0.0.1:8000/"


if options =="Home":
    st.header("welcome to my Home page")
    responce=requests.get(f"{url}/")
    if responce.status_code==200:
        st.info(responce.json()["message"])
    else:
        raise ValueError("file is not found")
elif options=="About":
    st.header("welcome to my about page ")
    responce=requests.get(f"{url}/about")
    if responce.status_code==200:
        st.info(responce.json()["message"])
    else:
         raise ValueError("file is not found")
    
elif options=="View":
    st.header("welcome to my view page ")
    responce=requests.get(f"{url}/view")
    if responce.status_code==200:
        data=responce.json()
        st.json(data)
    else:
       raise ValueError("file is not found")
    
elif options=="View_employee":
    st.header("welcome to my view_employee page. in this page view the all employee enter employee id ")
    employee_id=st.number_input("Enter Patient ID (e.g. P001)")
    responce=requests.get(f"{url}/employee/{employee_id} ")
    if responce.status_code==200:
       data=responce.json()
       st.json(data)
      

# create the post

elif options=="creat_details":
    st.header("welcome to create page in api")
    emp_id = st.number_input("Enter Employee ID",)
    name = st.text_input("Enter Employee Name")
    age = st.number_input("Enter Employee Age", min_value=18, max_value=70)
    gender=st.text_input("Enter Employee gender")
    position = st.text_input("Enter Department Name")
    department = st.text_input("Enter Department Name")
    salary = st.number_input("Enter Employee Salary", min_value=1000)
    is_active = st.selectbox("Employee status", ["True", "False"])
    if st.button("Create Employee"):
       if emp_id and name and department:
           employee_data = {
                "id": emp_id,
                "name": name,
                "age": age,
                "gender":gender,
                "position": position,
                "department": department,
                "salary": salary,
                "is_active": is_active
            }
       responce=requests.post("/create",json=employee_data)
       if responce.status_code in [200 , 201]:
          st.json(responce.json())