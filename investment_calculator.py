import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def investment_growth():
    st.header("Investment Growth Calculator")

    # Inputs
    initial_investment = st.number_input("Initial Investment", value=10000)
    monthly_contribution = st.number_input("Monthly Contribution", value=500)
    annual_return = st.slider("Expected Annual Return (%)", 0.0, 15.0, value=5.0)
    investment_duration = st.slider("Investment Duration (years)", 1, 50, value=30)

    # Calculations
    monthly_return = annual_return / 100 / 12
    months = investment_duration * 12
    balance = initial_investment
    balances = []

    for i in range(int(months)):
        balance += monthly_contribution
        balance *= (1 + monthly_return)
        balances.append(balance)

    st.write(f"Total Balance after {investment_duration} years: ${balance:.2f}")

    # Plot growth over time
    st.subheader("Investment Growth Over Time")
    fig, ax = plt.subplots()
    ax.plot(np.arange(1, months + 1), balances, label="Investment Value")
    ax.set_xlabel("Month")
    ax.set_ylabel("Investment Value")
    st.pyplot(fig)
