import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def loan_calculator():
    st.header("Loan Calculator")

    # Inputs
    loan_amount = st.number_input("Loan Amount", value=10000)
    interest_rate = st.slider("Interest Rate (%)", 0.0, 20.0, value=5.0, step=0.1)
    loan_term = st.slider("Loan Term (years)", 1, 30, value=10)

    # Calculations
    monthly_rate = interest_rate / 100 / 12
    num_payments = loan_term * 12
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)

    st.write(f"Monthly Payment: ${monthly_payment:.2f}")

    # Generate amortization table
    balance = loan_amount
    balances = []
    for i in range(int(num_payments)):
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        balance -= principal
        balances.append(balance)

    # Plot balance over time
    st.subheader("Amortization Schedule")
    fig, ax = plt.subplots()
    ax.plot(np.arange(1, num_payments + 1), balances, label="Remaining Balance")
    ax.set_xlabel("Month")
    ax.set_ylabel("Remaining Loan Balance")
    st.pyplot(fig)

