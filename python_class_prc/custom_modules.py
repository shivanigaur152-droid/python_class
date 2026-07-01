import streamlit as st
st.set_page_config(page_title="number additon",page_icon="➕",layout="centered")
st.title(" Addition of two number ")
st.caption(" Enter two number and it will return addition of them")

form=st.form("add_form")
num1=form.number_input("first number")
num2=form.number_input("second number")
submitted=form.form_submit_button("calculate sum")

if submitted:
  result=num1+num2
  st.divider()
  st.metric(label="result",value=result)

for i in range(1,11):
    st.write("2 X",i,"=",{2*i})

    