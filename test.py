import streamlit as st
import requests
import json

API_KEY = "J5aqNcxD.iqAolOyt2yCo2FLE4PWVA0YVBougtucw"

URL = "https://payload.vextapp.com/hook/B8S2QF5QYH/catch/sample"
headers = {
    "Content-Type": "application/json",
    "Apikey": f"Api-Key {API_KEY}"
}

st.title("Welcome to the Four Seasons' HR Assistant!")

#input form
with st.form("question_form"):
        user_input = st.text_input("What can I help you with today?")
        submit = st.form_submit_button("Enter")

#display response
if submit and user_input.lower() != 'exit':
        data = {"payload": user_input}
        try:
            response = requests.post(URL, headers=headers, json=data, verify=False)

            resp_json = response.json()
            answer_text = resp_json.get("text", "No answer provided.")
            cleaned_text = answer_text.replace("\n\n", "\n")
            st.subheader("Answer:")
            st.markdown(cleaned_text)
   
        except requests.exceptions.RequestException as e:
               st.error(f"Request failed: {e}")
       