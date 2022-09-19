import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """

"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://logosmarken.com/wp-content/uploads/2020/11/World-Wide-Fund-for-Nature-Logo.png"
st.sidebar.image(logo)

st.title("Analyse")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[47, 7.9], zoom=8)
        cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
        regions = 'https://github.com/jerome-oppliger/wwf_map/blob/590aee1856b45c9b9ad381c1be98fc3a1774238e/data/Gemeinden_CH3.geojson'

        m.add_geojson(regions, layer_name='CH Gemeinden')

        
m.to_streamlit(height=700)
