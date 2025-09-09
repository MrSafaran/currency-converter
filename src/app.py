import streamlit as st
from constants import CURRENCIES
from main import convert_currency, get_exchange_rate


st.title(":dollar: Currency Converter 💱")
st.caption("Rates are fetched in real-time from the API.")

st.text("Hello, This miniapp will let you to convert between currencies quickly and instantly!")
st.text("Enter the amount and choose the currencies to see the result.😇")

st.title("Choose the currencies 🎯")

base_currency = st.selectbox("Base currency:", CURRENCIES)
target_currency = st.selectbox("Target currency:", CURRENCIES, index = 66)

amount = st.number_input("The amount to convert:", min_value = 0.0)
st.caption("🔍 Please input positive values only.")


if amount > 0 and base_currency and target_currency :
    with st.spinner("Fetching live exchange rate... 🔄"):
        exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        st.success(f"✅ Exchange Rate: {exchange_rate:.2f}")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value=f"{amount:.2f} {base_currency}")
        col2.markdown("<h1 style='text-align: center; margin: 0; color: #90EE90'>&#10230;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")
        
    else:
        st.error('Error fetching exchange rate.')

st.markdown("____________")
st.markdown("### ℹ️ About This Tool")
st.markdown("""
This interactive web app allows users to convert one currency into another in real-time using up-to-date exchange rates. With a clean and intuitive interface powered by Streamlit, users can:
- 🔢 Enter the amount to convert
- 🌐 Select source and target currencies from dropdown menus
- 📊 See the converted value instantly
- 🔄 Refresh to get the latest exchange rates (if connected to an API)
Built with Python and Streamlit, the app is lightweight and runs entirely in the browser—perfect for educational demos, financial dashboards, or personal productivity tools
""")
