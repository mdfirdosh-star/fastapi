import streamlit as st
import requests

st.set_page_config(page_title="🏥 Hospital Patient Viewer", page_icon="💉")

st.title("🏥 Hospital Patient Viewer (FastAPI + Streamlit)")

# ---- FastAPI Base URL ----
API_URL = "http://127.0.0.1:8000/"   # 👈 apna FastAPI backend URL

# ---- Sidebar Navigation ----
st.sidebar.title("🔍 Navigation")
option = st.sidebar.radio(
    "Select Page",
    ["Home", "About", "View All Patients", "Search Patient by ID"]
)

# ---- Home Page ----
if option == "Home":
    st.header("Welcome Page")
    response = requests.get(f"{API_URL}/")
    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("API se response nahi aaya ❌")

# ---- About Page ----
elif option == "About":
    st.header("About This App")
    response = requests.get(f"{API_URL}/about")
    if response.status_code == 200:
        st.info(response.json()["message"])
    else:
        st.error("API error")

# ---- View All Patients ----
elif option == "View All Patients":
    st.header("👨‍⚕️ All Patient Details")
    response = requests.get(f"{API_URL}/view")
    if response.status_code == 200:
        data = response.json()
        st.json(data)
    else:
        st.error("Data load nahi hua 😢")

# ---- Search Patient by ID ----
elif option == "Search Patient by ID":
    st.header("🔎 Search Patient by ID")
    patient_id = st.text_input("Enter Patient ID (e.g. P001)")
    
    if st.button("Search"):
        if patient_id.strip() == "":
            st.warning("Please enter a valid Patient ID.")
        else:
            response = requests.get(f"{API_URL}/patient/{patient_id}")
            if response.status_code == 200:
                st.success("Patient Found ✅")
                st.json(response.json())
            else:
                st.error("❌ Patient not found or API error.")
