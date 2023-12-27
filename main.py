import streamlit as st
from mongodb import *
from googleapiclient.discovery import build
import pandas as pd

st.title("YOUTUBE HARVESTING")

channel_name = st.text_input("Enter channel name..",type="password")

api_service_name = "youtube"
api_version = "v3"
api_key = "AIzaSyBnnwC19hM5Kl1cdWIi3zNoXB3iSCrSBL8"

youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.search().list(
    part="snippet",
    maxResults=25,
    q= channel_name
)
response = request.execute()

if st.button("Get detail"):
    if response is not None:
        st.write(connect_mongo(response))