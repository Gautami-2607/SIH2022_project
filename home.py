import streamlit as st
import json
import requests
from mycode import National6
from mycode import State6
from mycode import District6
from mycode import Student6
from mycode import School6
from mycode import login
from streamlit_lottie import st_lottie
import pyrebase
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Home Page",page_icon=":blue_book:",
                   layout="wide")
from streamlit_option_menu import option_menu
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''
global a

st.markdown("""<h1><center> LAKSHYA </center></h1>""", unsafe_allow_html= True)
selected =option_menu(
        menu_title=None,
        options=["LOGIN/ SIGNUP","ABOUT US","FEEDBACK","LOGOUT"],
orientation="horizontal")

def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
def load_lottieurl(url:str):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_h9rxcjpi.json")
st_lottie(lottie_coding,height=500,width=500)

if selected=="LOGOUT":
   st.write("You have sucessfully logged out")
  #  pass
        
if selected=="LOGIN/ SIGNUP":
    #login.lgin()
    firebaseConfig = {
    'apiKey': "AIzaSyD8WxalSRDzcrVh2D94xv2crhh-llF5Ckk",
    'authDomain': "test-firestore-streamlit-2e7f6.firebaseapp.com",
    'databaseURL': "https://test-firestore-streamlit-2e7f6-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "test-firestore-streamlit-2e7f6",
    'storageBucket': "test-firestore-streamlit-2e7f6.appspot.com",
    'messagingSenderId': "853700405528",
    'appId': "1:853700405528:web:7dc0134e277fd19d13166d",
    'measurementId': "G-R7776ETSRE"#
    };

    # Firebase Authentication
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    # Database
    db = firebase.database()
    storage = firebase.storage()
    st.sidebar.title("Your credentials")

    # Authentication
    choice = st.sidebar.selectbox('Login/Signup', ['Login', 'Sign up'])

    # Obtain User Input for email and password
    email = st.sidebar.text_input('Enter your email address')
    password = st.sidebar.text_input('Enter your password',type='password')

    if choice == 'Sign up':
     fname = st.sidebar.text_input('Enter your first name')
     lname = st.sidebar.text_input('Enter your last name')
     handle = st.sidebar.selectbox('Enter your user type', ['Teacher','Parent','Student','School','EDO_National',
     'EDO_State','EDO_District',''],index= 7) # handle = user type
     submit = st.sidebar.button('Create my account')

     if submit:
      user = auth.create_user_with_email_and_password(email, password)
      st.success('Your account is created successfully!')
      st.balloons()

      # Sign in
      user = auth.sign_in_with_email_and_password(email, password)
      db.child(user['localId']).child("ID").set(user['localId'])
      db.child(user['localId']).child("Handle").set(handle)   
      db.child(user['localId']).child("First Name").set(fname)
      db.child(user['localId']).child("Last Name").set(lname)
      st.title('Welcome ' + fname )
      #st.info('Login via login drop down selection')


    # Login Block
    if choice == 'Login':
        login = st.sidebar.checkbox('Login')
        if login:
            user = auth.sign_in_with_email_and_password(email,password)
            fname = db.child(user['localId']).child("First Name").get().val()
            a = " "+fname
            st.title('Hello  ' + fname )
            hndl = db.child(user['localId']).child("Handle").get().val()
            #st.title(hndl)

            slctd = st.selectbox("",['DASHBOARD'])
            #st.title(slctd)

            if slctd == 'DASHBOARD' : 
                if hndl == 'EDO_National':
                    #st.write("This is National level dashboard")
                    National6.national()
                if hndl == 'EDO_State':
                    #st.write("This is State level dashboard")
                    State6.state()
                if hndl == 'EDO_District':
                    #st.write("This is District level dashboard")
                    District6.district()
                if hndl == 'School':
                    #st.write("This is School level dashboard")
                    School6.school()
                if hndl == 'Student':
                    #st.write("This is Student level dashboard")
                    Student6.student()    

#st.write("Welcome"+a)
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
 footer {visibility: hidden;}
 header {visibility: hidden;}
 </style>
 """
st.markdown(hide_st_style, unsafe_allow_html=True)

