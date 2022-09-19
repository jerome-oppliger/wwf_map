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
        regions = 'https://github.com/jerome-oppliger/wwf_map/blob/b4cdcd287dd860097da82dae9262ef6fc4238e9e/data/Gemeinden_CH3.geojson'

        m.add_geojson(regions, layer_name='Gemeinden_CH3')
        m
        
m.to_streamlit(height=700)
