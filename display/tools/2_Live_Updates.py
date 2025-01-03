import pandas as pd
import requests
from datetime import datetime, timedelta, timezone
import streamlit as st

endtime = datetime.now(timezone.utc)
startime = endtime - timedelta(days=1)

startime_str = startime.strftime("%Y-%m-%dT%H:%M:%S")
endtime_str = endtime.strftime("%Y-%m-%dT%H:%M:%S")

def converttime(linuxtime):
    timestamp_ms = linuxtime
    timestamp_s = timestamp_ms / 1000
    readable_time = datetime.utcfromtimestamp(timestamp_s)
    return readable_time

print(startime_str, endtime_str)

@st.cache_data(ttl="1d")
def createDataFrame():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": startime_str,
        "endtime": endtime_str,
        "minmagnitude": 2.0,
        "orderby": "time"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        features = data.get("features", [])  # Correctly access the "features" key
        
        # Create a DataFrame
        earthquake_data = pd.DataFrame([
            {
                "title": feature["properties"]["title"],
                "longitude": feature["geometry"]["coordinates"][0],
                "latitude": feature["geometry"]["coordinates"][1],
                "time": converttime(feature["properties"]["time"]),
                "magnitude": feature["properties"]["mag"],
                "place": feature["properties"]["place"],
                "url": feature["properties"]["url"],
            }
            for feature in features
        ])
        print(earthquake_data)
        return earthquake_data

    else:
        print(f"Failed to fetch data! Status code: {response.status_code}")

if "earthquake_data" not in st.session_state:
    st.session_state.earthquake_data = pd.DataFrame() # Empty dataframe to start with.

st.sidebar.markdown('''
# Sections
<a href="#latest-sorted-by-date-asc" style="
    display: inline-block;
    background: linear-gradient(135deg, #FFA726, #FB8C00);
    color: #FFF;
    padding: 5px;
    text-align: center;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
    margin-right: 10px;
    box-sizing: border-box;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    ">Live Updates</a>
<a href="#downloadable-datasets-location-mapping" style="
    display: inline-block;
    background: linear-gradient(135deg, #FFA726, #FB8C00);
    color: #FFF;
    padding: 5px;
    text-align: center;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
    margin-right: 10px;
    box-sizing: border-box;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    ">Location Map</a>
''', unsafe_allow_html=True)

st.title("Earthquake Live Updates [Last 30 days] & Mapping")
st.caption("Refreshed Daily")
st.divider()

st.markdown("### Latest sorted by date (asc)")
earthquake_data = createDataFrame()
st.session_state.earthquake_data = earthquake_data
for _,row in earthquake_data.iterrows():
    with st.expander(f"{row['time']} - {row['title']} - {row['magnitude']}"):
        st.markdown(f"""
            ### {row['title']}
            - **Location:** {row['place']}
            - **Magnitude:** {row['magnitude']}
            - **Coordinates:** {row['latitude']}, {row['longitude']}
            - **Time:** {row['time']}
            - [View More Details]({row['url']})
        """)

st.divider()

st.markdown("### Downloadable datasets & Location Mapping")

st.dataframe(earthquake_data)
print(st.session_state.earthquake_data)
st.map(st.session_state.earthquake_data, latitude="latitude", longitude="longitude", size=100000,color="#FFA50080")