import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Analyse klimarelevanter Abstimmungen CH
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://logosmarken.com/wp-content/uploads/2020/11/World-Wide-Fund-for-Nature-Logo.png"
st.sidebar.image(logo)

# Customize page title
st.title("Analyse klimarelevanter Abstimmungen CH")

st.markdown(
    """
    Interaktive Karten der WWF Schweiz Analyse zu folgenden klimarelevanten Abstimmungen:

    - Bundesgesetz über die Verminderung von Treibhausgasemissionen (CO2-Gesetz). Abstimmungsdatum, 13.06.2021
    """
)

st.header("Karte CO2-Gesetz")

markdown = """
1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
