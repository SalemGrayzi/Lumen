import streamlit as st
import pandas as pd

# create the Streamlit app object
st.title("Light Fixtures Dashboard")

# create an expander for the first light fixture
with st.beta_expander('Industrial Lighting'):
    # add the selectbox for the brands
    st.image('https://nvcuk.net/_panel/public/site-panel/products-subcategories/12/id12-image_1630478538.png', use_column_width=True)
    if st.button('Show Brands'):

        df = pd.DataFrame(
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
            {"Brand": "Delta Light", "Link": 'https://deltalight.com/en/products?perPage=12&filters[collection]=14b97380-4974-11ed-a67a-00505693bd3f&filters[location]=7a8f0b24-2f76-11ed-9132-00505693b57f&sorting=newest'},
            {"Brand": "Stahl", "Link": "https://r-stahl.com/en/global/products/"},
            {"Brand": "Cooper Lighting", "Link": "https://www.cooperlighting.com/global/search?#tab=products"},
            {"Brand": "Ikizler", "Link": "https://www.ikizlerlighting.com"},
            ]
        )

        edited_df = st.experimental_data_editor(df, num_rows="dynamic")
