import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_monthly(df):
    monthly_df = df.resample(rule='M', on='dteday').agg({
        "cnt": "sum"
    })

    monthly_df.index = monthly_df.index.strftime('%b %Y')
    monthly_df = monthly_df.reset_index()
    monthly_df.rename(columns={
        "cnt": "order_count"
    }, inplace=True)

    return monthly_df



def create_casual_df(df):
    monthly_df = df.resample(rule='M', on='dteday').agg({
        "casual": "sum"
    })

    monthly_df.index = monthly_df.index.strftime('%b %Y')
    monthly_df = monthly_df.reset_index()
    monthly_df.rename(columns={
        "casual": "casual_count"
    }, inplace=True)

    return monthly_df

def create_registered_df(df):
    monthly_df = df.resample(rule='M', on='dteday').agg({
        "registered": "sum"
    })

    monthly_df.index = monthly_df.index.strftime('%b %Y')
    monthly_df = monthly_df.reset_index()
    monthly_df.rename(columns={
        "registered": "registered_count"
    }, inplace=True)

    return monthly_df



def create_temp_df(df):
    monthly_df = df.resample(rule='M', on='dteday').agg({
        "temp": "sum"
    })

    monthly_df.index = monthly_df.index.strftime('%b %Y')
    monthly_df = monthly_df.reset_index()
    monthly_df.rename(columns={
        "temp": "temp_count"
    }, inplace=True)

    return monthly_df


def create_hum_df(df):
    monthly_df = df.resample(rule='M', on='dteday').agg({
        "hum": "sum"
    })

    monthly_df.index = monthly_df.index.strftime('%b %Y')
    monthly_df = monthly_df.reset_index()
    monthly_df.rename(columns={
        "hum": "hum_count"
    }, inplace=True)

    return monthly_df


def create_windspeed_df(df):
    monthly_df = df.resample(rule='M', on='dteday').agg({
        "windspeed": "sum"
    })

    monthly_df.index = monthly_df.index.strftime('%b %Y')
    monthly_df = monthly_df.reset_index()
    monthly_df.rename(columns={
        "windspeed": "windspeed_count"
    }, inplace=True)

    return monthly_df

def create_season_df(df):
    if df["season"].dtype != "object":
        df["season"] = df["season"].apply(lambda x: 
            "Springer" if x == 1 else
            "Summer" if x == 2 else
            "Fall" if x == 3 else 
            "Winter")

    season = df.groupby("season")["instant"].nunique().sort_values(ascending=False).reset_index()

    return season

def create_weathersit_df(df):
    if df["weathersit"].dtype != "object":
        df["weathersit"] = df["weathersit"].apply(lambda x: 
            "Clear, Few Clouds, Partly Cloudy, Partly Cloudy" if x == 1 else
            "Mist + Cloudy, Mist + Broken Clouds, Mist + Few Clouds, Mist" if x == 2 else
            "Light Snow, Light Rain + Thunderstorm + Scattered Clouds, Light Rain + Scattered Clouds" if x == 3 else 
            "Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog")
    
    weathersit = df.groupby("weathersit")["instant"].nunique().sort_values(ascending=False).reset_index()
    
    return weathersit

df = pd.read_csv("Dashboard/main_data.csv")

# df = pd.read_csv("https://github.com/bentolooyomine/project_analysis_data/blob/main/Dashboard/main_data.csv", error_bad_lines=False)
# df = pd.read_csv("https://github.com/bentolooyomine/project_analysis_data/blob/main/Dashboard/main_data.csv")

df.head()

df.info()

df["dteday"] = pd.to_datetime(df["dteday"])

min_date = df["dteday"].min()
max_date = df["dteday"].max()

with st.sidebar:
  
    st.image("data:image/png;base64,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")
    
    
    start_date, end_date = st.date_input(
        label='Jarak Tanggal',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = df[(df["dteday"] >= str(start_date)) & 
                (df["dteday"] <= str(end_date))]

monthly_df = create_monthly(main_df)
season_df = create_season_df(main_df)
weathersit_df = create_weathersit_df(main_df)
casual_df = create_casual_df(main_df)
registered_df = create_registered_df(main_df)
temp_df = create_temp_df(main_df)
hum_df = create_hum_df(main_df)
windspeed_df = create_windspeed_df(main_df)
st.header('Final Project Data Analysis')



## Persewaan  ##





total_orders = monthly_df["order_count"].sum()
st.metric("Jumlah Order", value=f"{total_orders:,}")

total_casual = casual_df["casual_count"].sum()
st.metric("Jumlah Casual", value=f"{total_casual:,}")

total_registered = registered_df["registered_count"].sum()
st.metric("Jumlah Registered", value=f"{total_registered:,}")


total_temp = temp_df["temp_count"].sum() /  temp_df["temp_count"].count() 
st.metric("Rata Rata Temp", value=f"{total_temp:,}")

total_hum = hum_df["hum_count"].sum() /  hum_df["hum_count"].count() 
st.metric("Rata Rata Hum", value=f"{total_hum:,}")

total_windspeed = windspeed_df["windspeed_count"].sum() /  windspeed_df["windspeed_count"].count() 
st.metric("Rata Rata windspeed", value=f"{total_windspeed:,}")

st.subheader("Gowess Analisa Persewaan")
fig, ax = plt.subplots(figsize=(16, 8))

ax.plot(monthly_df['dteday'], monthly_df['order_count'], marker='o', linestyle='-', linewidth=2, color='#441752')

plt.xticks(rotation=45)

st.pyplot(fig)


st.subheader('Data per Bulan')
st.write(monthly_df)


## ==========End================ Bendakudaz ##

## Musim ##
st.subheader("Penyewaan Berdasarkan Musim (Session)")
 


fig, ax = plt.subplots(figsize=(16, 8))
colors = ["#441752", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(
    x="instant", 
    y="season", 
    data=season_df.head(10), 
    palette=colors
)

ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title(
    "Musim Persewaan Terbanyak", 
    loc="center", 
    fontsize=20
)
ax.tick_params(axis ='y', labelsize=15)
 
st.pyplot(fig)

st.subheader('Data per Musim Ter Sedikit')
st.write(season_df)

fig2, ax = plt.subplots(figsize=(16, 8))
sns.barplot(
    x="instant", 
    y="season", 
    data=season_df.sort_values(
        by="instant", 
        ascending=True).head(5), 
    palette=colors
)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.invert_xaxis()
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()
ax.set_title(
    "Musim Persewaan Tersedikit", 
    loc="center", 
    fontsize=20
)
ax.tick_params(axis ='y', labelsize=15)
 
st.pyplot(fig)
## Musim ##



st.subheader('Data per Musim ter Banyak')
st.write(season_df)



## Kondisi Cuaca ##
st.subheader("Penyewaan Berdasarkan Kondisi Cuaca")
 
fig, ax = plt.subplots(figsize=(16, 8))
 
colors = ["#441752", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(
    x="instant", 
    y="weathersit", 
    data=weathersit_df.head(5), 
    palette=colors
)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()
ax.set_title(
    "Paling Banyak Penyewaan", 
    loc="center", 
    fontsize=20
)
ax.tick_params(axis ='y', labelsize=15)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))

sns.barplot(
    x="instant", 
    y="weathersit", 
    data=weathersit_df.sort_values(
        by="instant", 
        ascending=True).head(5), 
    palette=colors
)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.invert_xaxis()
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()
ax.set_title(
    "Paling Sedikit Penyewaan", 
    loc="center", 
    fontsize=20
)
ax.tick_params(axis='y', labelsize=15)
 
st.pyplot(fig)
## Kondisi Cuaca ##

st.subheader('Data per Bulan')
st.write(weathersit_df)


st.caption('Copyright © Benny Danang Kurniawan with Partner Dicoding 2024')
