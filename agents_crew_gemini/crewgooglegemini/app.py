import streamlit as st
from crew import call_llm
st.title("BLOG Creator")

user_input=st.text_input(label="Enter you blog disctption here : ")

submit_btn=st.button(label="submit")
    
if submit_btn:
        result=call_llm(user_input)
        st.markdown(result)