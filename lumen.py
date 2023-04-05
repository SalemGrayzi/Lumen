import streamlit as st
import pandas as pd


# Create an empty container
placeholder = st.empty()

actual_email = "email"
actual_password = "password"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and email == actual_email and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success(# create the Streamlit app object
st.title("Light Fixtures Dashboard")

# create an expander for the first light fixture
with st.beta_expander('Industrial Lighting'):
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

        edited_Industrial_Lighting = st.experimental_data_editor(Industrial_Lighting, num_rows="dynamic")
)
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    pass





