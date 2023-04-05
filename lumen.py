import streamlit as st
import pandas as pd
from streamlit.hashing import _CodeHasher
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server
import SessionState

# create the Streamlit app object
st.title("Light Fixtures Dashboard")

# create a session state object
session_state = SessionState.get(email="", password="", logged_in=False)

# define actual login credentials
actual_email = "email"
actual_password = "password"

# create a function to hash passwords
def hash_password(password):
    hasher = _CodeHasher()
    return hasher.hash(password)

# create a function to log in
def login():
    if session_state.email == actual_email and hash_password(session_state.password) == hash_password(actual_password):
        session_state.logged_in = True
        return True
    else:
        return False

# create an empty container
placeholder = st.empty()

# insert a login form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    session_state.email = st.text_input("Email", session_state.email)
    session_state.password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

# log in if the form is submitted and the credentials are correct
if submit:
    if login():
        # if the login is successful, clear the form and display a success message
        placeholder.empty()
        st.success("Login successful")
    else:
        # if the login fails, display an error message
        st.error("Invalid email or password")

# if the user is not logged in, display the login form and return
if not session_state.logged_in:
    st.stop()
