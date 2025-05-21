
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Lead Volume Analysis", layout="wide")

st.title("📊 Lead Volume Breakdown")

# Load the data
utm_df = pd.read_csv("utm_summary.csv")
region_df = pd.read_csv("region_summary.csv")

# Sidebar filters
st.sidebar.header("Filters")
selected_categories = st.sidebar.multiselect(
    "Select Lead Categories",
    options=["Qualified", "Unqualified", "Pending"],
    default=["Qualified", "Unqualified", "Pending"]
)

def filter_df(df):
    return df[["UTM_Campaign"] + selected_categories] if "UTM_Campaign" in df.columns else df[["Region"] + selected_categories]

# UTM Campaign Chart
st.subheader("Leads by UTM Campaign")
filtered_utm = filter_df(utm_df)
utm_melted = filtered_utm.melt(id_vars=["UTM_Campaign"], var_name="Category", value_name="Count")
fig1 = px.bar(
    utm_melted,
    x="UTM_Campaign",
    y="Count",
    color="Category",
    title="Lead Volume by UTM Campaign",
    labels={"UTM_Campaign": "UTM Campaign", "Count": "Number of Leads"},
    barmode="stack"
)
fig1.update_layout(xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig1, use_container_width=True)

# Region Chart
st.subheader("Leads by Region")
filtered_region = filter_df(region_df)
region_melted = filtered_region.melt(id_vars=["Region"], var_name="Category", value_name="Count")
fig2 = px.bar(
    region_melted,
    x="Region",
    y="Count",
    color="Category",
    title="Lead Volume by Region",
    labels={"Region": "Region", "Count": "Number of Leads"},
    barmode="stack"
)
fig2.update_layout(xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig2, use_container_width=True)
