import streamlit as st

st.header("💝 Reasons Why I Love You")
reasons = [
    "Your beautiful smile",
    "Your kindness towards others",
    "The way you make me laugh",
    "Your strength and determination",
    "How you make every day special",
]


for reason in reasons:
    st.markdown(f"- ✨ {reason}")