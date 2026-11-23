import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config & Custom CSS Styling
st.set_page_config(
    page_title="Retail Sales Analytics",
    layout="wide"
)

# Custom Styling for Metric Cards & Layout
st.markdown("""
    <style>
    .metric-card {
        background-color: #1E222D;
        border: 1px solid #2E3440;
        border-radius: 10px;
        padding: 15px 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .metric-label {
        font-size: 14px;
        color: #A0AEC0;
        margin-bottom: 5px;
    }
    .metric-value {
        font-size: 26px;
        font-weight: bold;
        color: #ECEFF4;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Header Section
st.markdown("""
    <div style="text-align: center; margin-bottom: 25px;">
        <h1 style="margin-bottom: 5px;">Retail Sales & Analytics Dashboard</h1>
        <p style="color: #A0AEC0; font-size: 16px;">Real-time operational insights, revenue distributions, and product performance analysis.</p>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")

# 3. Load & Cache Data
@st.cache_data
def load_data():
    df = pd.read_csv('data/Cleaned_dataset.csv')
    if 'Total_Amount' not in df.columns:
        df['Total_Amount'] = df['Price Per Unit'] * df['Quantity']
    return df

df = load_data()

# 4. Sidebar Filters
st.sidebar.header("Dashboard Filters")

selected_categories = st.sidebar.multiselect(
    "Select Categories:",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

# Filter Data
filtered_df = df[df['Category'].isin(selected_categories)]

# 5. Top KPI Metric Cards
col1, col2, col3, col4 = st.columns(4)

total_rev = filtered_df['Total_Amount'].sum()
total_orders = len(filtered_df)
avg_order = filtered_df['Total_Amount'].mean()
total_units = filtered_df['Quantity'].sum() if 'Quantity' in filtered_df.columns else 0

with col1:
    st.markdown(f'''
        <div class="metric-card">
            <div class="metric-label">Total Revenue</div>
            <div class="metric-value">${total_rev:,.2f}</div>
        </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
        <div class="metric-card">
            <div class="metric-label">Total Orders</div>
            <div class="metric-value">{total_orders:,}</div>
        </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
        <div class="metric-card">
            <div class="metric-label">Avg Order Value</div>
            <div class="metric-value">${avg_order:,.2f}</div>
        </div>
    ''', unsafe_allow_html=True)

with col4:
    st.markdown(f'''
        <div class="metric-card">
            <div class="metric-label">Units Sold</div>
            <div class="metric-value">{total_units:,}</div>
        </div>
    ''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Primary Interactive Dark Theme Charts (Plotly)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Revenue by Product Category")
    cat_df = filtered_df.groupby('Category')['Total_Amount'].sum().reset_index()
    cat_df = cat_df.sort_values(by='Total_Amount', ascending=True)

    fig_cat = px.bar(
        cat_df, 
        x='Total_Amount', 
        y='Category', 
        orientation='h',
        color='Total_Amount',
        color_continuous_scale='Viridis',
        labels={'Total_Amount': 'Revenue ($)', 'Category': ''}
    )
    fig_cat.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        coloraxis_showscale=False,
        margin=dict(l=10, r=10, t=10, b=10)
    )
    st.plotly_chart(fig_cat, use_container_width=True)

with chart_col2:
    st.subheader("Top 10 Best-Selling Items")
    item_df = filtered_df.groupby('Item')['Total_Amount'].sum().nlargest(10).reset_index()
    item_df = item_df.sort_values(by='Total_Amount', ascending=True)

    fig_item = px.bar(
        item_df, 
        x='Total_Amount', 
        y='Item', 
        orientation='h',
        color='Total_Amount',
        color_continuous_scale='Blues',
        labels={'Total_Amount': 'Revenue ($)', 'Item': ''}
    )
    fig_item.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        coloraxis_showscale=False,
        margin=dict(l=10, r=10, t=10, b=10)
    )
    st.plotly_chart(fig_item, use_container_width=True)

# 6.5 Secondary Row of Charts (Payment Methods & Location Distribution)
st.markdown("---")
chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.subheader("Revenue by Payment Method")
    if 'Payment Method' in filtered_df.columns:
        pay_df = filtered_df.groupby('Payment Method')['Total_Amount'].sum().reset_index()
        fig_pay = px.pie(
            pay_df, 
            values='Total_Amount', 
            names='Payment Method', 
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_pay.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=10, r=10, t=10, b=10)
        )
        st.plotly_chart(fig_pay, use_container_width=True)

with chart_col4:
    st.subheader("Revenue by Location Channel")
    if 'Location' in filtered_df.columns:
        loc_df = filtered_df.groupby('Location')['Total_Amount'].sum().reset_index()
        fig_loc = px.bar(
            loc_df, 
            x='Location', 
            y='Total_Amount', 
            color='Location',
            color_discrete_sequence=px.colors.qualitative.Bold,
            labels={'Total_Amount': 'Revenue ($)', 'Location': 'Sales Channel'}
        )
        fig_loc.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            margin=dict(l=10, r=10, t=10, b=10)
        )
        st.plotly_chart(fig_loc, use_container_width=True)

# 7. Raw Data Table
st.markdown("---")
with st.expander("View Data Table Preview", expanded=False):
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)