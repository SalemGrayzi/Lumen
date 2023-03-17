import streamlit as st

# create a dictionary with the brand names and their websites
brands = {
    'Ledvance': 'https://www.ledvance.com',
    'Prilux': 'https://www.prilux.es',
    'Trevos': 'https://trevos.eu',
}

# create the Streamlit app object
st.title("Light Fixtures Dashboard")

# create an expander for the first light fixture
with st.beta_expander('Industrial Lighting'):
    # add the image
    st.image('data:image/jpeg;base64,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')
    # add the selectbox for the brands
    if st.button(''):
        brand_name = st.selectbox('Select a brand', list(brands.keys()))
        st.write(f'The website for {brand_name} is {brands[brand_name]}.')
    st.image('data:image/jpeg;base64,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', use_column_width=True)
    
    
    #brand_name = st.selectbox('Select a brand', list(brands.keys()))
    # display the website for the selected brand
    #st.write(f'The website for {brand_name} is {brands[brand_name]}.')
