import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def budget_tracker():
    st.header("Budget Tracker")

    # Inputs for income and expenses
    income = st.number_input("Monthly Income", value=4000)
    expenses_data = {
        "Rent": st.number_input("Rent", value=1000),
        "Groceries": st.number_input("Groceries", value=300),
        "Utilities": st.number_input("Utilities", value=200),
        "Transport": st.number_input("Transport", value=100),
        "Entertainment": st.number_input("Entertainment", value=200),
        "Savings": st.number_input("Savings", value=500),
        "Others": st.number_input("Other Expenses", value=200),
    }

    # DataFrame for expenses
    expenses_df = pd.DataFrame(list(expenses_data.items()), columns=['Category', 'Amount'])

    # Total Expenses and Savings Calculation
    total_expenses = expenses_df['Amount'].sum()
    savings = income - total_expenses

    st.write(f"Total Expenses: ${total_expenses:.2f}")
    st.write(f"Remaining Savings: ${savings:.2f}")

    # Pie chart for expenses distribution
    st.subheader("Expense Distribution")
    fig, ax = plt.subplots()
    ax.pie(expenses_df['Amount'], labels=expenses_df['Category'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
