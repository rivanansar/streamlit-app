#import library 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Load the dataset
data_2019 = pd.read_csv('2019.csv')

# Streamlit App
st.title("Combined Data Visualizations of the 2019 World Happiness Report")

# Bar Chart: Peringkat kebahagiaan negara berdasarkan skor kebahagiaan mereka
st.subheader("Happiness Score by Country")
fig1 = px.bar(data_2019, x='Country or region', y='Score', title='Happiness Score by Country',
              labels={'Score': 'Happiness Score', 'Country or region': 'Country'},
              hover_data=['GDP per capita', 'Social support', 'Healthy life expectancy'])
fig1.add_annotation(x=data_2019['Country or region'][0], y=data_2019['Score'][0],
                    text="Top Country", showarrow=True, arrowhead=1)
fig1.update_traces(marker_color='lightblue')
st.plotly_chart(fig1)

# Line Chart: Tren kebahagiaan beberapa negara dari tahun ke tahun
st.subheader("Happiness Score Trend")
countries = ["Finland", "Denmark", "Norway", "Iceland", "Netherlands"]
line_data = data_2019[data_2019['Country or region'].isin(countries)]
fig2 = px.line(line_data, x='Country or region', y='Score', title='Happiness Score Trend',
               labels={'Score': 'Happiness Score', 'Country or region': 'Country'},
               markers=True)
fig2.add_annotation(x=countries[0], y=line_data['Score'].iloc[0],
                    text="Finland's Score", showarrow=True, arrowhead=1)
st.plotly_chart(fig2)

# Scatter Plot: Hubungan antara GDP per capita dengan skor kebahagiaan
st.subheader("GDP per Capita vs Happiness Score")
fig3 = px.scatter(data_2019, x='GDP per capita', y='Score', text='Country or region',
                  title='GDP per Capita vs Happiness Score', labels={'Score': 'Happiness Score', 'GDP per capita': 'GDP per Capita'},
                  hover_data=['Social support', 'Healthy life expectancy', 'Freedom to make life choices'])
top_gdp_country = data_2019.loc[data_2019['GDP per capita'].idxmax()]
fig3.add_annotation(x=top_gdp_country['GDP per capita'], y=top_gdp_country['Score'],
                    text="Highest GDP per Capita", showarrow=True, arrowhead=1)
fig3.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')),
                   selector=dict(mode='markers'))
st.plotly_chart(fig3)

# Heatmap: Distribusi skor kebahagiaan berdasarkan wilayah geografis
st.subheader("Happiness Score by Country (Heatmap)")
fig4 = go.Figure(data=go.Choropleth(
    locations=data_2019['Country or region'],
    z=data_2019['Score'],
    locationmode='country names',
    colorscale='Blues',
    colorbar_title='Happiness Score',
))
fig4.update_layout(
    title_text='Happiness Score by Country',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
)
fig4.add_annotation(x=-60, y=10, text="Top Country: Finland", showarrow=False)
fig4.add_annotation(x=120, y=-20, text="Lowest Country: South Sudan", showarrow=False)
st.plotly_chart(fig4)
