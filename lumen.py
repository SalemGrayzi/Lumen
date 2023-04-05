import streamlit as st
import pandas as pd

# create the Streamlit app object
st.title("Light Fixtures Dashboard")

# create an expander for the first light fixture
with st.expander('Industrial Lighting'): ##with st.beta_expander('Industrial Lighting'):
    # add the selectbox for the brands
    st.image('https://nvcuk.net/_panel/public/site-panel/products-subcategories/12/id12-image_1630478538.png', use_column_width=True)
    if st.checkbox('Show Brands'):
        Industrial_Lighting = pd.DataFrame(
        [
            {"Brand": "Ledvance", "Link": 'https://www.ledvance.asia'},
            {"Brand": "Prilux", "Link": 'https://www.prilux.es'},
            {"Brand": "Trevos", "Link": "https://trevos.eu"},
            {"Brand": "NVC", "Link": 'https://www.nvc-international.com/product_list.php?x=10'},
            {"Brand": "Frater", "Link": 'https://fraterlighting.com'},
            {"Brand": "Tryka", "Link": "https://tryka.com/products"},
            {"Brand": "Gewis", "Link": 'https://www.gewiss.com/ww/en/'},
            {"Brand": "Dextra", "Link": 'https://www.dextragroup.co.uk/dextra-lighting/'},
            {"Brand": "Trilux", "Link": "https://www.trilux.com/en/"},
            {"Brand": "Intra Lighting", "Link": 'https://www.intra-lighting.com'},
            {"Brand": "Stahl", "Link": "https://r-stahl.com/en/global/products/"},
            {"Brand": "Cooper Lighting", "Link": "https://www.cooperlighting.com/global/search?#tab=products"},
            {"Brand": "Ikizler", "Link": "https://www.ikizlerlighting.com"},
            {"Brand": "Bartec", "Link": "https://www.bartec.de/en/products/control-and-connection-equipment/lighting-technology/"},
            {"Brand": "Eaton", "Link": "https://www.eaton.com/gb/en-gb/products.html"},

            ]
        )

        st.dataframe(Industrial_Lighting)##edited_Industrial_Lighting = st.experimental_data_editor(Industrial_Lighting, num_rows="dynamic")

# create an expander for the first light fixture
with st.expander('Downlight/Spotlight/Tracklights/LED Panel'): ##with st.beta_expander('Downlight/Spotlight/Tracklights'):
    # add the selectbox for the brands
    st.image('https://storage.googleapis.com/tryka-dev.appspot.com/Products/Downlights/Abner%203/Renders/Abner%203_R_White.webp', use_column_width=True)
    if st.button('Show Brands '):
        Downlight_Spotlight_Tracklights = pd.DataFrame(
        [
            {"Brand": "Ledvance", "Link": 'https://www.ledvance.asia'},
            {"Brand": "Prilux", "Link": 'https://www.prilux.es'},
            {"Brand": "NVC", "Link": 'https://www.nvc-international.com/product_list.php?x=10'},
            {"Brand": "Frater", "Link": 'https://fraterlighting.com'},
            {"Brand": "Tryka", "Link": "https://tryka.com/products"},
            {"Brand": "Gewis", "Link": 'https://www.gewiss.com/ww/en/'},
            {"Brand": "Dextra", "Link": 'https://www.dextragroup.co.uk/dextra-lighting/'},
            {"Brand": "Trilux", "Link": "https://www.trilux.com/en/"},
            {"Brand": "Intra Lighting", "Link": 'https://www.intra-lighting.com'},
            {"Brand": "Delta Light", "Link": 'https://deltalight.com/en/products?perPage=12&filters[collection]=14b97380-4974-11ed-a67a-00505693bd3f&filters[location]=7a8f0b24-2f76-11ed-9132-00505693b57f&sorting=newest'},
            {"Brand": "Cooper Lighting", "Link": "https://www.cooperlighting.com/global/search?#tab=products"},
            {"Brand": "Ikizler", "Link": "https://www.ikizlerlighting.com"},
            ]
        )

        st.dataframe(Downlight_Spotlight_Tracklights)##edited_Downlight_Spotlight = st.experimental_data_editor(Downlight_Spotlight_Tracklights, num_rows="dynamic")


# create an expander for the first light fixture
with st.expander('Wall-Mount'): ##with st.beta_expander('Wall-Mount'):
    # add the selectbox for the brands
    st.image('https://storage.googleapis.com/tryka-dev.appspot.com/Products/Architectural%20Accent/Tuba%204%20UpDown/Renders/Tuba%204%20UpDown_R_Grey.webp', use_column_width=True)
    if st.button('Show Brands  '):
        Wall_Mount = pd.DataFrame(
        [
            {"Brand": "Tryka", "Link": "https://tryka.com/products"},
            {"Brand": "Dextra", "Link": 'https://www.dextragroup.co.uk/dextra-lighting/'},
            {"Brand": "Trilux", "Link": "https://www.trilux.com/en/"},
            {"Brand": "Delta Light", "Link": 'https://deltalight.com/en/products?perPage=12&filters[collection]=14b97380-4974-11ed-a67a-00505693bd3f&filters[location]=7a8f0b24-2f76-11ed-9132-00505693b57f&sorting=newest'},
            {"Brand": "Cooper Lighting", "Link": "https://www.cooperlighting.com/global/search?#tab=products"},
            {"Brand": "Heper Lighting", "Link": "https://heperlighting.com/products/"},
            {"Brand": "Light34/Light Solution(Oman)", "Link": "https://www.light34.com/en/outdoor-lighting-15"},
            ]
        )

        st.dataframe(Wall_Mount)##edited_Wall_Mount = st.experimental_data_editor(Wall_Mount, num_rows="dynamic")

# create an expander for the first light fixture
with st.expander('HighBay/FloodLights'): ##with st.beta_expander('HighBay/Flood'):
    # add the selectbox for the brands
    st.image('https://www.trilux.com/products/asset/GroupImageMedium/Ondo_T_TB_LED_03_DB_WEB', use_column_width=True)
    if st.button('Show Brands   '):
        HighBay_Flood_Lights = pd.DataFrame(
        [
            {"Brand": "Ledvance", "Link": 'https://www.ledvance.asia'},
            {"Brand": "Prilux", "Link": 'https://www.prilux.es'},
            {"Brand": "NVC", "Link": 'https://www.nvc-international.com/product_list.php?x=10'},
            {"Brand": "Frater", "Link": 'https://fraterlighting.com'},
            {"Brand": "Gewis", "Link": 'https://www.gewiss.com/ww/en/'},
            {"Brand": "Dextra", "Link": 'https://www.dextragroup.co.uk/dextra-lighting/'},
            {"Brand": "Trilux", "Link": "https://www.trilux.com/en/"},
            {"Brand": "Stahl", "Link": "https://r-stahl.com/en/global/products/"},
            {"Brand": "Cooper Lighting", "Link": "https://www.cooperlighting.com/global/search?#tab=products"},
            {"Brand": "Ikizler", "Link": "https://www.ikizlerlighting.com"},
            {"Brand": "Bartec", "Link": "https://www.bartec.de/en/products/control-and-connection-equipment/lighting-technology/"},
            {"Brand": "Eaton", "Link": "https://www.eaton.com/gb/en-gb/products.html"},
            {"Brand": "Heper Lighting", "Link": "https://heperlighting.com/products/"},
            {"Brand": "Light34/Light Solution(Oman)", "Link": "https://www.light34.com/en/outdoor-lighting-15"},
            {"Brand": "MGL Lighting", "Link": "http://www.mgl-led.com/commercial-lighting"},
            ]
        )

        st.dataframe(HighBay_Flood_Lights)##edited_Industrial_Lighting = st.experimental_data_editor(HighBay_Flood_Lights, num_rows="dynamic")


# create an expander for the first light fixture
with st.expander('Street Light/Poles'): ##with st.beta_expander('Street Light/Poles'):
    # add the selectbox for the brands
    st.image('https://d7rh5s3nxmpy4.cloudfront.net/CMP1303/prilux-versa-xl.png', use_column_width=True)
    if st.button('Show Brands    '):
        Street_Light_Poles = pd.DataFrame(
        [
            {"Brand": "Ledvance", "Link": 'https://www.ledvance.asia'},
            {"Brand": "Prilux", "Link": 'https://www.prilux.es'},
            {"Brand": "Frater", "Link": 'https://fraterlighting.com'},
            {"Brand": "Gewis", "Link": 'https://www.gewiss.com/ww/en/'},
            {"Brand": "Dextra", "Link": 'https://www.dextragroup.co.uk/dextra-lighting/'},
            {"Brand": "Cooper Lighting", "Link": "https://www.cooperlighting.com/global/search?#tab=products"},
            {"Brand": "Ikizler", "Link": "https://www.ikizlerlighting.com"},
            {"Brand": "Heper Lighting", "Link": "https://heperlighting.com/products/"},
            {"Brand": "Light34/Light Solution(Oman)", "Link": "https://www.light34.com/en/outdoor-lighting-15"},
            ]
        )

        st.dataframe(Street_Light_Poles)##edited_Industrial_Lighting = st.experimental_data_editor(Street_Light_Poles, num_rows="dynamic")

# create an expander for the first light fixture
with st.expander('Emergency'): ##with st.beta_expander('Emergency'):
    # add the selectbox for the brands
    st.image('https://trevos.eu/upload/produkty/HELIOS-LED/HELIOS-LED/fotogalerie/HELIOS-LED_01.jpg', use_column_width=True)
    if st.button('Show Brands     '):
        Emergency = pd.DataFrame(
        [
            {"Brand": "Trevos", "Link": "https://trevos.eu"},
            {"Brand": "Frater", "Link": 'https://fraterlighting.com'},
            {"Brand": "Dextra", "Link": 'https://www.dextragroup.co.uk/dextra-lighting/'},
            {"Brand": "Stahl", "Link": "https://r-stahl.com/en/global/products/"},
            {"Brand": "Cooper Lighting", "Link": "https://www.cooperlighting.com/global/search?#tab=products"},
            {"Brand": "Ikizler", "Link": "https://www.ikizlerlighting.com"},
            {"Brand": "Bartec", "Link": "https://www.bartec.de/en/products/control-and-connection-equipment/lighting-technology/"},
            {"Brand": "Eaton", "Link": "https://www.eaton.com/gb/en-gb/products.html"},
            ]
        )

        st.dataframe(Emergency)##edited_Industrial_Lighting = st.experimental_data_editor(Emergency, num_rows="dynamic")

