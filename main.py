
import streamlit as st
from streamlit_option_menu import option_menu


selected = option_menu(
    menu_title=None,  # required
    options=["Home", "Image", "Video"],  # required
    icons=["house", "card-image", "camera-video"],
    default_index=0,
    orientation="horizontal",
)

if selected == "Home":
    st.title("Hello everyone :wave:\n I am Komal Goel")


if selected == "Image":
    option = st.selectbox('Please upload an image',
                          ('Upload a file', 'Use Camera'))
    if option == "Upload a file":
        images = st.file_uploader("Please uplaod an image", type=[
                                  "png", "jpg", "jpeg", "gif"], accept_multiple_files=True)
        if images is not None:
            for image in images:
                st.image(image)
    if option == "Use Camera":
        picture = st.camera_input("Take a picture")
        if picture:
            st.image(picture)

    value = st.text_input("Enter a caption", max_chars=90)

if selected == "Video":
    videos = st.file_uploader("Please upload an video",
                              type="mp4", accept_multiple_files=True)
    if videos is not None:
        for video in videos:
            st.video(video)
