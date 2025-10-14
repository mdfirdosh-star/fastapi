import streamlit as st
import requests

st.title("welcome to my hospital webside")
st.image("https://viewlinez.com/wp-content/uploads/2025/06/hospital_pick_up_lines-1024x538.webp")
st.subheader("all detail of patient ")
url_add="http://127.0.0.1:8000/"


# create the options on sidebar 
st.sidebar.title("Negivatior")
options=st.sidebar.radio("chose the api pages",["Home","About","View","Docs"])
if options=="Home":
    st.header("welcome to my home page")
    response=requests.get(f"{url_add}/")
    if response.status_code==200:
        st.success(response.json()['message'])
    else:
        st.error("api ages is not exists")
elif options =="About":
    st.header(" welcome About page ")
    response=requests.get(f"{url_add}/about")
    if response.status_code==200:
        st.success(response.json()["message"])
    else:
        st.error("page not found ")
elif options=="View":
    st.header("welcome to view page ")
    response=requests.get(f"{url_add}/view")
    if response.status_code==200:
        data=response.json()
        st.json(data)
    else:
        st.error("page is not found ")
elif options=="Docs":
    st.header('welcome to my documentation')
    response=requests.get(f"{url_add}/docs")
    if requests.status_codes==200:
        data=response.json()
        st.json(response.json(data))
    else:
        st.error({"page not found"})




