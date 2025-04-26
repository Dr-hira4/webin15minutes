#project 9 build a python website in 15 minutes with streamlit

import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="student data generator", layout="wide")
st.title("student csv file generator")

names = ["ali", "aisha", "ahmed", "fatima", "usman", "zainab", "junaid", "hira", "hafsa", "sami", "hadia", "hamza", "sara", "tariq", "mehak", "faisal"]

students= []
for i in range(1,16):
    student = {
        "ID": i,
        "name": random.choice(names),
        "age": random.randint(18,25),
        "grade": random.choice(["A","B","C","D","E","F"]),
        "marks": random.randint(40,100),
    }
    students.append(student)

df = pd.DataFrame(students)
st.subheader("generated students data")
st.dataframe(df)

csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("download CSV file", csv_file, "student.csv", "text/csv")
st.success("students record generated successfully!")
