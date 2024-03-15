import streamlit as st
from PIL import Image
import pickle
from roboflow import Roboflow

# Load the model
filename = "veera.pkl"
loaded_model = pickle.load(open(filename, 'rb'))

# Predefined username and password
PREDEFINED_USERNAME = "admin"
PREDEFINED_PASSWORD = "admin"

# Function to get or create session state
def get_session_state():
    if 'is_logged_in' not in st.session_state:
        st.session_state['is_logged_in'] = False
    return st.session_state

# Function to clear session state
def clear_session_state():
    st.session_state.clear()

# Function to check if the user is logged in
def is_logged_in():
    return get_session_state()['is_logged_in']

# Custom login page
def custom_login():
    st.title('Login')
    username = st.text_input('Username', value="")
    password = st.text_input('Password', type='password', value="")
    if st.button('Login'):
        if username == PREDEFINED_USERNAME and password == PREDEFINED_PASSWORD:
            get_session_state()['is_logged_in'] = True
            st.success('Logged in as {}'.format(username))
        else:
            st.error('Invalid username or password.')

# Main function
def main():
    if not is_logged_in():
        custom_login()
    else:
        st.title('Human Bone Fracture Detection')
        st.write('Logged in as {}'.format(PREDEFINED_USERNAME))
        if st.button('Logout'):
            get_session_state()['is_logged_in'] = False
            st.success('Logged out.')
        uploaded_image = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            image = image.convert('RGB')
            image.save('uploaded_image.jpg')
            result_image = loaded_model.predict('uploaded_image.jpg', confidence=40, overlap=30)
            result_image.save('result_image.jpg')
            if st.button('Show Result'):
                st.image('result_image.jpg', caption='Fracture Detection Result', use_column_width=True)

if __name__ == '__main__':
    main()
