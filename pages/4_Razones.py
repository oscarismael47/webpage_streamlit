import streamlit as st

st.header("💝 Razones Por Las Que Te Amo")
reasons = [
    "Tu hermosa sonrisa",
    "La forma en que me haces reír",
    "Tu fuerza y determinación",
    "Cómo haces que cada día sea especial",
    "Tu inteligencia y creatividad",
    "La forma en que me apoyas en mis metas",
    "La forma en que me miras",
    "Tu capacidad para hacerme sentir seguro",
    "La forma en que compartimos momentos simples",
    "Tu ternura y cariño incondicional",
]

for reason in reasons:
    st.markdown(f"- ✨ {reason}")