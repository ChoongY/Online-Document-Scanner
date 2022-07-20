import streamlit as st
import numpy as np
import cv2 
from PIL import Image
import Scanner
import OCR
import sendMail

st.set_page_config(
     page_title="🖨Online Document Scanner",
     page_icon="🖨🖨",
     layout="wide",
     initial_sidebar_state="expanded",
 )


imageSide = Image.open(r"C:\Users\kahch\Downloads\document scanner-logos_black.png")
homeImage = Image.open(r"C:\Users\kahch\Downloads\document scanner-logos.jpeg")

'''
# Online Document Scanner
'''
#Tutorial video
video_file = open(r'D:\video souce\clutch or fail 2.0.mp4', 'rb')
video_bytes = video_file.read()

#Sidebar
st.sidebar.image(imageSide)
st.sidebar.title("Navigation bar")
selectbox = st.sidebar.radio(
    "Select the page you would like the to go",
    ["Home", "Tutorial", "Main application","Reference"]
)
if selectbox == "Home":# Home Page
    st.header("🏡Home Page")
    st.image(homeImage, width =  400)
    st.subheader("This system is made for the final year project")
    st.subheader("This application is used to scan the document in the image and detect the text of the image. In the system, I am using multiple libraries to create the application")


elif selectbox == "Tutorial":# Tutorial page
    st.header("🎈🎈Welcome to Online Document Scanner🎈🎈")

    st.subheader("Below are an video that how to use the application")
    st.video(video_bytes)
    st.caption("The video above show how does the application work")

elif selectbox == "Main application": # Application feature page
    st.header("Choose your image that you wanted to upload")
    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
    if image_file is not None:
        # To View Uploaded Image
        st.image(image_file, caption= 'Uploaded Image')
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, 1)
        st.subheader("Document after scanned")
        # scan the image to allocate the document
        scanned_file=Scanner.scanner(frame)
        st.image(scanned_file,caption="scanned image") # In here apply the document scanner.
        st.write("download your scanned image here") # provide an button for download.
        cv2.imwrite("image.png",scanned_file)
        st.download_button(label="Download scanned image", data="image.png")
        # apply the text detection.
        st.subheader("text file that you detected in the image") 
        imgToS=cv2.imread("image.png")
        text = OCR.textScanner(imgToS) # using the text Scanner function from the OCR file to detect the text in the iamge
        st.write(text)
        st.write("download the text file") # create an text file for the text detected.
        st.download_button('Download some text', text)
        with open("Output.txt", "w") as txtfile:
            print("{}".format(text), file=txtfile)
        emel=st.text_input("Please enter your email address")
        if st.button(label = "Send"):
            sendMail.sendEmail(emel)
            st.write("Your file have been sent to the email you entered")


elif selectbox == "Reference": #reference page
    st.header("References")# list out the reference used(Streamlit, github code, webside)
    st.write("The compiler i used to code on is **_Visual_ Studio**")
