import streamlit as st

st.title("📊 Student Performance System")

# Input section
name = st.text_input("Enter student name")
quiz1 = st.number_input("Enter quiz 1 score", min_value=0.0)
quiz2 = st.number_input("Enter quiz 2 score", min_value=0.0)
attendance = st.number_input("Enter attendance rate (%)", min_value=0.0, max_value=100.0)

# Process when button is clicked
if st.button("Generate Report"):
    name = name.upper()
    average = quiz1 + quiz2

    # Decision logic
    if average >= 500 and attendance >= 80:
        status = "EXCELLENT"
    elif average >= 400 and attendance >= 75:
        status = "GOOD"
    else:
        status = "NEEDS IMPROVEMENT"

    # Output section
    st.subheader("📄 STUDENT REPORT")
    st.write("Name:", name)
    st.write("Average Score:", average)
    st.write("Attendance Rate:", str(attendance) + "%")
    st.write("Status:", status)