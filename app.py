import streamlit as st

# -----------------------------
# ترجمه‌ها
# -----------------------------
LANG = st.session_state.get("LANG", "EN")

T = {
    "FA": {
        "title": "مقایسه نرخ تبدیل ارز",
        "ex_sek_eur": "کرون به یورو (EX)",
        "amount_sek": "مقدار کرون",
        "amount_eur": "مقدار یورو",
        "sek_to_toman": "هر کرون به تومان (EX1)",
        "rate_ex1": "نرخ EX1",
        "eur_to_toman": "هر یورو به تومان (EX2)",
        "rate_ex2": "نرخ EX2",
        "calculate": "محاسبه",
        "toggle": "تغییر حالت",
        "lang": "FA / EN",
        "invalid": "خطا در ورودی‌ها",

        "result_line1": "هر یورو معادل (EX) {v} SEK است",
        "result_line2": "مقدار کرون → (EX1) {v} T",
        "result_line3": "مقدار یورو → (EX2) {v} T",
        "result_more": "بیشتر: {v}",
        "result_diff": "اختلاف: {v} T",
    },

    "EN": {
        "title": "Currency Exchange Comparator",
        "ex_sek_eur": "SEK to EUR (EX)",
        "amount_sek": "Amount in SEK",
        "amount_eur": "Amount in EUR",
        "sek_to_toman": "SEK to Toman (EX1)",
        "rate_ex1": "EX1 Rate",
        "eur_to_toman": "EUR to Toman (EX2)",
        "rate_ex2": "EX2 Rate",
        "calculate": "Calculate",
        "toggle": "Toggle Theme",
        "lang": "EN / FA",
        "invalid": "Invalid input",

        "result_line1": "Each Euro equals (EX) {v} SEK",
        "result_line2": "Amount in SEK → (EX1) {v} T",
        "result_line3": "Amount in EUR → (EX2) {v} T",
        "result_more": "Higher value: {v}",
        "result_diff": "Difference: {v} T",
    }
}

# -----------------------------
# Helper
# -----------------------------
def fmt(x):
    try:
        return f"{x:,.0f}".replace(",", ".")
    except:
        return x

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="Currency App", layout="centered")

st.title(T[LANG]["title"])

# Language switch
if st.button(T[LANG]["lang"]):
    LANG = "EN" if LANG == "FA" else "FA"
    st.session_state["LANG"] = LANG
    st.rerun()

# Theme toggle
if st.button(T[LANG]["toggle"]):
    if "theme" not in st.session_state:
        st.session_state["theme"] = "light"
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"
    st.rerun()

# -----------------------------
# Inputs
# -----------------------------
st.subheader(T[LANG]["ex_sek_eur"])
kron1 = st.number_input(T[LANG]["amount_sek"], min_value=0.0, step=1.0)
euro_rate = st.number_input(T[LANG]["amount_eur"], min_value=0.0, step=0.1)

st.subheader(T[LANG]["sek_to_toman"])
ex1 = st.number_input(T[LANG]["rate_ex1"], min_value=0.0, step=1.0)

st.subheader(T[LANG]["eur_to_toman"])
ex2 = st.number_input(T[LANG]["rate_ex2"], min_value=0.0, step=1.0)

# -----------------------------
# Calculate
# -----------------------------
if st.button(T[LANG]["calculate"]):
    try:
        euro_result = kron1 / euro_rate if euro_rate else 0
        toman1 = kron1 * ex1
        toman2 = euro_rate * ex2
        diff = toman1 - toman2

        result_text = (
            f"{T[LANG]['result_line1'].format(v=fmt(euro_result))}<br>"
            f"{T[LANG]['result_line2'].format(v=fmt(toman1))}<br>"
            f"{T[LANG]['result_line3'].format(v=fmt(toman2))}<br>"
            f"-----------------------------<br>"
            f"{T[LANG]['result_more'].format(v=('SEK' if toman1 > toman2 else 'EUR'))}<br>"
            f"{T[LANG]['result_diff'].format(v=fmt(abs(diff)))}<br><br>"
            f"<span style='font-size:14px;opacity:0.7;'>Created by M.Sadeghi💻</span>"
        )

        st.markdown(
            f"<div style='background:#1e1e1e;padding:15px;border-radius:10px;color:white;'>{result_text}</div>",
            unsafe_allow_html=True
        )



    except:
        st.error(T[LANG]["invalid"])
