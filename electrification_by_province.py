import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt

st.title("Electrification by Province")
st.markdown(" ## Build python functions that can analyse Eskom data")

# Load in data 

ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.set_index("Financial Year (1 April - 30 March)")
st.write(ebp_df.head())

province_tuple= ("Limpopo",	"Mpumalanga", "North west",	"Free State", "Kwazulu Natal", "Eastern Cape",	"Western Cape", "Northern Cape", "Gauteng")

province_name=st.selectbox("Select a province name ", province_tuple )

# Change the province names 

for item in province_tuple:
    if province_name == item: 
        province = ebp_df[item].astype(float).to_list()


def dictionary_of_metrics(province):
    dict_metrics={}
    arr= np.array(province)
    dict_metrics['mean']= round(np.mean(arr), 2)
    dict_metrics['median']= round(np.median(arr),2)
    dict_metrics['std']=round(np.std(arr, ddof=1),2)
    dict_metrics['var']=round(np.var(arr, ddof=1),2)
    dict_metrics['max']=round(np.max(arr),2)
    dict_metrics['min']=round(np.min(arr),2)

    
    return dict_metrics

st.write(dictionary_of_metrics(province))

# User input of a list to get the statistics metrics

def five_num_summary(items):
    dict_five_num_summary= {}

    arr= np.array(items)
    dict_five_num_summary['max']= round(np.max(arr),2)
    dict_five_num_summary['min']= round(np.min(arr),2)
    dict_five_num_summary['median']= round(np.median(arr),2)
    dict_five_num_summary['q1']= round(np.quantile((arr),.25),2)
    dict_five_num_summary['q3']= round(np.quantile((arr),.75),2)

    return dict_five_num_summary

(ebp_df['Financial Year (1 April - 30 March)'], list(province_tuple),  linewidth=2, markersize=12)
plt.show()
