import streamlit as st
import pandas as pd


# Create an empty container
placeholder = st.empty()

actual_email = ""
actual_password = ""

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### For Lumen Employees Only")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")
    url = "https://lumen.ae"
    st.write("[Visit Our Website](%s)" % url)

if submit and email == actual_email and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("Login successful")
    st.title("Light Fixtures Dashboard")
        with st.beta_expander('Industrial Lighting'):
    # add the selectbox for the brands
        st.image('https://nvcuk.net/_panel/public/site-panel/products-subcategories/12/id12-image_1630478538.png', use_column_width=True)
        #if st.button('Show Brands'):
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
        edited_Industrial_Lighting = st.experimental_data_editor(Industrial_Lighting, num_rows="dynamic")

# create an expander for the first light fixture
    with st.beta_expander('Downlight/Spotlight/Tracklights/LED Panel'):
    # add the selectbox for the brands
        st.image('https://storage.googleapis.com/tryka-dev.appspot.com/Products/Downlights/Abner%203/Renders/Abner%203_R_White.webp', use_column_width=True)
        #if st.button('Show Brands '):
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
        edited_Downlight_Spotlight = st.experimental_data_editor(Downlight_Spotlight_Tracklights, num_rows="dynamic")


# create an expander for the first light fixture
    with st.beta_expander('Wall-Mount'):
    # add the selectbox for the brands
        st.image('https://storage.googleapis.com/tryka-dev.appspot.com/Products/Architectural%20Accent/Tuba%204%20UpDown/Renders/Tuba%204%20UpDown_R_Grey.webp', use_column_width=True)
        #if st.button('Show Brands  '):
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
        edited_Wall_Mount = st.experimental_data_editor(Wall_Mount, num_rows="dynamic")

# create an expander for the first light fixture
    with st.beta_expander('HighBay/FloodLights'):
    # add the selectbox for the brands
        st.image('https://www.trilux.com/products/asset/GroupImageMedium/Ondo_T_TB_LED_03_DB_WEB', use_column_width=True)
        #if st.button('Show Brands   '):
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
        edited_HighBay_Flood_Lights = st.experimental_data_editor(HighBay_Flood_Lights, num_rows="dynamic")

            # create an expander for the first light fixture
    with st.beta_expander('Street Light/Poles'):
    # add the selectbox for the brands
        st.image('https://d7rh5s3nxmpy4.cloudfront.net/CMP1303/prilux-versa-xl.png', use_column_width=True)
        #if st.button('Show Brands    '):
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
        edited_Street_Light_Poles = st.experimental_data_editor(Street_Light_Poles, num_rows="dynamic")

# create an expander for the first light fixture
    with st.beta_expander('Emergency'):
    # add the selectbox for the brands
        st.image('https://trevos.eu/upload/produkty/HELIOS-LED/HELIOS-LED/fotogalerie/HELIOS-LED_01.jpg', use_column_width=True)
        #if st.button('Show Brands     '):
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
                {"Brand": "Gulf Safety ", "Link": "https://gulfsafety.com"},

                ]
            )
        edited_Emergency = st.experimental_data_editor(Emergency, num_rows="dynamic")

elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    pass


#            {"Brand": "Ledvance", "Link": 'https://www.ledvance.asia'},
#            {"Brand": "Prilux", "Link": 'https://www.prilux.es'},
#            {"Brand": "Trevos", "Link": "https://trevos.eu"},
#            {"Brand": "NVC", "Link": 'https://www.nvc-international.com/product_list.php?x=10'},
#            {"Brand": "Frater", "Link": 'https://fraterlighting.com'},
#            {"Brand": "Gewis", "Link": 'https://www.gewiss.com/ww/en/'},
#            {"Brand": "Dextra", "Link": 'https://www.dextragroup.co.uk/dextra-lighting/'},
#            {"Brand": "Trilux", "Link": "https://www.trilux.com/en/"},
#            {"Brand": "Stahl", "Link": "https://r-stahl.com/en/global/products/"},
#            {"Brand": "Cooper Lighting", "Link": "https://www.cooperlighting.com/global/search?#tab=products"},
#            {"Brand": "Ikizler", "Link": "https://www.ikizlerlighting.com"},
#            {"Brand": "Bartec", "Link": "https://www.bartec.de/en/products/control-and-connection-equipment/lighting-technology/"},
#            {"Brand": "Eaton", "Link": "https://www.eaton.com/gb/en-gb/products.html"},
#            {"Brand": "Heper Lighting", "Link": "https://heperlighting.com/products/"},
#            {"Brand": "Light34/Light Solution(Oman)", "Link": "https://www.light34.com/en/outdoor-lighting-15"},
#            {"Brand": "Yente", "Link": "https://www.yente.com/en/light-poles"},
#            {"Brand": "Al Babtain", "Link": "http://www.al-babtain.com.sa/our-facility/pole-and-high-mast/"},
#            {"Brand": "MGL Lighting", "Link": "http://www.mgl-led.com/commercial-lighting"},
#            {"Brand": "Gulf Safety ", "Link": "https://gulfsafety.com"},


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://github.com/SalemGrayzi/Lumen/blob/main/diamond.jpg?raw=true");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

