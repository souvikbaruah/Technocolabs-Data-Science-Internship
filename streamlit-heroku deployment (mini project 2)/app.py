# Importing all necessary libraries
import streamlit as st
import pickle
import numpy as np


page_bg_img = '''
<style>
body {
background-image: url("https://image.cnbcfm.com/api/v1/image/106210419-1572366832669gettyimages-1137376687.jpg?v=1572366860&w=740&h=416");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Loading the saved Model
model = pickle.load(open("model.pkl", "rb"))



def predict_default(features):

    features = np.array(features).astype(np.float64).reshape(1,-1)
    
    prediction = model.predict(features)
    probability = model.predict_proba(features)

    return prediction, probability


def main():
        
    html_temp = """
        <div style = "background-color: salmon; padding: 5px; font-family:monospace; font-weight:800;">
            <center><h1>Credit Card Default Predictor</h1></center>
        </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    LIMIT_BAL = st.text_input("Limited Balance (in New Taiwanese (NT) dollar)")
    
    education_status = ["University", "Graduate School", "High school", "Others"]
    marital_status = ["Single","Married", "Others"]

    payment_status = [
        "Account started that month with a 0 balance and never used any credit",
        "Account that had a balance that was paid in full",
        "Account that had minimum payment but the entire balance was not paid",
        "Payment delay for 1 month",
        "Payment delay for 2 months",
        "Payment delay for 3 months",
        "Payment delay for 4 months",
        "Payment delay for 5 months",
        "Payment delay for 6 months",
        "Payment delay for 7 months",
        "Payment delay for 8 months",   
    ]

    EDUCATION = education_status.index(st.selectbox(
        "Education",
        tuple(education_status)
    )) + 1
    
    MARRIAGE = marital_status.index(st.selectbox(
        "Marital Status",
        tuple(marital_status)
    )) + 1
    
    AGE = st.text_input("Age (in years)")

    PAY_1 = payment_status.index(st.selectbox(
        "Last Month Payment Status",
        tuple(payment_status)
    )) - 2

    html_temp = """
        <div style = "background-color: salmon; padding: 1px; font-family:monospace; font-size : 60%;">
            <center><h1>Bill Amount (Past 6 Months)</h1></center>
        </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    BILL_AMT1 = st.text_input("Last month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT2 = st.text_input("2nd last month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT3 = st.text_input("3rd last month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT4 = st.text_input("4th last month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT5 = st.text_input("5th last month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT6 = st.text_input("6th lasth month Bill Amount (in New Taiwanese (NT) dollar)")

    html_temp = """
        <div style = "background-color: salmon; padding: 1px; font-family:monospace; font-size : 2.5em;">
            <center><h1>Amount Paid (Past 6 Months)</h1></center>
        </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    PAY_AMT1 = st.text_input("Amount Paid in last month (in New Taiwanese (NT) dollar)")
    PAY_AMT2 = st.text_input("Amount Paid in 2nd last month (in New Taiwanese (NT) dollar)")
    PAY_AMT3 = st.text_input("Amount Paid in 3rd last month (in New Taiwanese (NT) dollar)")
    PAY_AMT4 = st.text_input("Amount Paid in 4th last month (in New Taiwanese (NT) dollar)")
    PAY_AMT5 = st.text_input("Amount Paid in 5th last month (in New Taiwanese (NT) dollar)")
    PAY_AMT6 = st.text_input("Amount Paid in 6th last month (in New Taiwanese (NT) dollar)")

    if st.button("PREDICT"):
        
        features = [LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]
        prediction, probability = predict_default(features)
        
        if prediction[0] == 1:
       

            st.success("This account will be defaulted with a probability of {}%.".format(round(np.max(probability)*100, 2)))

        else:
            st.success("This account will not be defaulted with a probability of {}%.".format(round(np.max(probability)*100, 2)))




if __name__ == '__main__':
    main()
