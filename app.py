import streamlit as st
st.header("PDD Unit Calculator")
st.subheader("Please Enter Information Below")

money = st.number_input("Enter Amount")

def calc(money):
    if money < 170:
        units = (money/1.69)
    elif money >= 169 and money < 390:
        units = 100 + (money-169)/2.20
    elif money >= 389 and money < 1049:
        units = 100 + 220 + (money-389)/3.30
        
    return units

calc(money)

st.write("Number of Units : ", calc(money))
        

        
