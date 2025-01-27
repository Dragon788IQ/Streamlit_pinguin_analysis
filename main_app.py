import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def load_data(url : str):
    try:
        df = pd.read_csv(url)
        return df
    except:
        print("Error loading the file :c")

def pinguin_mesures_graph(df):
    pinguins_types = df["species"].unique()
    culmen_l_means = [] 
    culmen_d_means = []
    flipper_means = []
    for pinguin in pinguins_types:
        culmen_l_means.append(df.loc[df["species"] == pinguin, "culmen_length_mm"].mean())
        culmen_d_means.append(df.loc[df["species"] == pinguin, "culmen_depth_mm"].mean())
        flipper_means.append(df.loc[df["species"] == pinguin, "flipper_length_mm"].mean())
    
    hist_data = [culmen_l_means, culmen_d_means, flipper_means]
    df_mesures = pd.DataFrame()
    df_mesures["species"] = pinguins_types
    df_mesures["culmen_length_mm_mean"]= culmen_l_means
    df_mesures["culmen_depth_mm_mean"]= culmen_d_means
    df_mesures["flipper_length_mm_mean"]= flipper_means
    fig = px.bar(
        df_mesures,
        x="species",
        y=["culmen_length_mm_mean", "culmen_depth_mm_mean", "flipper_length_mm_mean"],
        barmode="group")
    
    return fig

def pie_chart(df):
    pinguins_types = df["species"].unique()
    number = []
    for pinguin in pinguins_types:
        number.append(len(df[df["species"] == pinguin]))
    
    df_pcounts = pd.DataFrame()
    df_pcounts["spieces"] = pinguins_types
    df_pcounts["No. of pinguins"] = number
    # st.write(df_pcounts)
    fig = px.pie(
        df_pcounts,
        values="No. of pinguins",
        names="spieces",
        hole=.5
    )
    fig.update_traces(textinfo= "value+percent")
    return fig

df = load_data("Resource/penguins_size.csv")

st.title("Pinguin size analysis 🐧")

with st.sidebar:
    st.write("This is a side bar")

st.dataframe(df, hide_index=True)

pinguins_types = df["species"].unique()

select_pinguin = st.selectbox(
    "Select a pinguin species",
    pinguins_types,
    None
)

st.write(select_pinguin) 

colum_1, colum_2, colum_3, colum_4 = st.columns([1,1,1,1], gap="small")
colum_5, colum_6 = st.columns([1,1], gap="small")
df_select_pinguin = df[df["species"] == str(select_pinguin)]


with colum_1:
    st.metric("No. total of Pinguins",df["species"].count(), border=True)
with colum_2:
    st.metric(f"No. of {pinguins_types[0]}", len(df[df["species"] == pinguins_types[0]]), border=True)
with colum_3:
    st.metric(f"No. of {pinguins_types[1]}", len(df[df["species"] == pinguins_types[1]]), border=True)
with colum_4:
    st.metric(f"No. of {pinguins_types[2]}", len(df[df["species"] == pinguins_types[2]]), border=True)
with colum_5:
    hist_mesures = pinguin_mesures_graph(df)
    st.plotly_chart(hist_mesures)
with colum_6:
    pie_numbers = pie_chart(df)
    st.plotly_chart(pie_numbers)



