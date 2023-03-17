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
    st.image('https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.trevos.eu%2Fupload%2Fprodukty%2FFUTURA%2FFUTURA-HE%2FFUTURA-HE_hlavni.jpg&tbnid=cngV7viJBA6aEM&vet=12ahUKEwi6w4_T9-L9AhV3picCHXk7AwIQMygEegUIARD2AQ..i&imgrefurl=https%3A%2F%2Fwww.trevos.eu%2Fen%2F&docid=j6dIsKJHgjvmaM&w=1200&h=800&q=trevos&client=opera-gx&ved=2ahUKEwi6w4_T9-L9AhV3picCHXk7AwIQMygEegUIARD2AQ')
    # add the selectbox for the brands
    brand_name = st.selectbox('Select a brand', list(brands.keys()))
    # display the website for the selected brand
    st.write(f'The website for {brand_name} is {brands[brand_name]}.')

# create an expander for the second light fixture
with st.beta_expander('Light Fixture 2'):
    # add the image
    st.image('https://example.com/image2.jpg')
    # add the selectbox for the brands
    brand_name = st.selectbox('Select a brand', list(brands.keys()))
    # display the website for the selected brand
    st.write(f'The website for {brand_name} is {brands[brand_name]}.')

# create an expander for the third light fixture
with st.beta_expander('Light Fixture 3'):
    # add the image
    st.image('https://example.com/image3.jpg')
    # add the selectbox for the brands
    brand_name = st.selectbox('Select a brand', list(brands.keys()))
    # display the website for the selected brand
    st.write(f'The website for {brand_name} is {brands[brand_name]}.')

