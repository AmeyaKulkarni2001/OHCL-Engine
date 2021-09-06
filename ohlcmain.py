import json_to_csv as jc
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import streamlit as st
import company_gen as cg
import graph_gen as gg
import pyEX as p
import api


jc.conv()
st.title("OHLC Chart Engine")
c = p.Client(api_token=api.IEX_API_TOKEN, version='stable')

x = st.text_input("Enter Company Symbol ")
if len(x) != 0:
    x = x.upper()
    file1 = open("MyFile.txt", "a")
    file1.write(x+"\n")
    file1.close()
    count = cg.symbol_gen(x)
    if(count == 0):
        st.write("NO COMAPNY FOUND!")
    else:
        original_list = ['Candle', 'OHLC', 'Vertex Line',
                         'Colored Bar', 'Hollow Candlestick']
        result = st.selectbox('Select a graph type', original_list)

        if len(result) != 0:
            if(result == "Candle"):
                fig = gg.candle_gen()
                st.plotly_chart(fig)
            elif(result == "OHLC"):
                fig = gg.ohlc_gen()
                st.plotly_chart(fig)
            elif(result == "Colored Bar"):
                fig = gg.colored_bar()
                st.plotly_chart(fig)
            elif(result == "Vertex Line"):
                fig = gg.vertex_line()
                st.plotly_chart(fig)
            elif(result == "Hollow Candlestick"):
                fig = gg.hollow_gen()
                st.plotly_chart(fig)

company_data_symbol = st.sidebar.text_input(
    "Want to know more about a company?")

if len(company_data_symbol) != 0:
    d = c.company(symbol=company_data_symbol)
    st.sidebar.write("Company Name - " + d['companyName'])
    st.sidebar.write("Web - " + d['website'])
    st.sidebar.write("Primary Exchange - " + d['exchange'])
    st.sidebar.write("CEO - " + d['CEO'])
    st.sidebar.write("Address - " + d['city'] + ", " + d['country'])
