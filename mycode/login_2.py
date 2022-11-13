import streamlit as st
from streamlit_option_menu import option_menu
def lgin():
    # Firebase Authentication
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    # Database
    db = firebase.database()
    storage = firebase.storage()
    st.sidebar.title("Our community app")

    # Authentication
    choice = st.sidebar.selectbox('Select login or Signup', ['Login', 'Sign up'])

    # Obtain User Input for email and password
    email = st.sidebar.text_input('Please enter your email address')
    password = st.sidebar.text_input('Please enter your password',type = 'password')

    if choice == 'Sign up':
     handle = st.sidebar.text_input('Please input your app handle name', value='Default')
     submit = st.sidebar.button('Create my account')

     if submit:
      user = auth.create_user_with_email_and_password(email, password)
      st.success('Your account is created successfully!')
      st.balloons()

      # Sign in
      user = auth.sign_in_with_email_and_password(email,password)
      #db.child(user['localId']).child("Handle").set(handle)
      # db.child(user['localId']).child("Id").set(user['localId'])
      st.title('Welcome' + handle)
      st.info('Login via login dropdown selectbox')


        # ---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)


    '''st.text("hi this is login page")
    #r=st.columns(20)
    usernames=[]
    passwords=[]
    reqdict = dict(zip(usernames, passwords))
    hi=option_menu(
        menu_title=None,
        options=["LOGIN", "SIGNUP"],
        orientation="horizontal")
    """with r[10]:
        s=st.selectbox("SignUp")"""
    if(hi=="SIGNUP"):
        username=st.text_input("Enter the user name",type="default")
        password=st.text_input("Enter the Password",type="password")
        usernames.append(username)
        passwords.append(password)
        st.write(passwords)
    if(hi=="LOGIN"):
        username = st.text_input("Enter the user name")
        password = st.text_input("Enter the Password")'

        """if ((username in usernames) and (password in passwords)):
            if(reqdict[username]==password):
                st.text("hi ra this is chandu")
"""
'''

# Modules
import pyrebase
import streamlit as st

# Config Key
firebaseConfig = {
    'apiKey': "AIzaSyD8WxalSRDzcrVh2D94xv2crhh-llF5Ckk",
    'authDomain': "test-firestore-streamlit-2e7f6.firebaseapp.com",
    'projectId': "test-firestore-streamlit-2e7f6",
    'databaseURL': "https://console.firebase.google.com/u/0/project/test-firestore-streamlit-2e7f6/database/test-firestore-streamlit-2e7f6-default-rtdb/data/~2F",
    'storageBucket': "test-firestore-streamlit-2e7f6.appspot.com",
    'messagingSenderId': "853700405528",
    'appId': "1:853700405528:web:7dc0134e277fd19d13166d",
    'measurementId': "G-R7776ETSRE"
};

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()
st.sidebar.title("Our community app")

# Authentication
choice = st.sidebar.selectbox('login/Signup', ['Login', 'Sign up'])

# Obtain User Input for email and password
email = st.sidebar.text_input('Please enter your email address')
password = st.sidebar.text_input('Please enter your password',type = 'password')

if choice == 'Sign up':
  handle = st.sidebar.text_input('Please input your app handle name', value='Default')
  submit = st.sidebar.button('Create my account')

  if submit:
   user = auth.create_user_with_email_and_password(email, password)
   st.success('Your account is created successfully!')
   st.balloons()

   # Sign in
   user = auth.sign_in_with_email_and_password(email,password)
   #db.child(user['localId']).child("Handle").set(handle)
   #db.child(user['localId']).child("Id").set(user['localId'])
   st.title('Welcome' + handle)
   st.info('Login via login dropdown selectbox')


    # ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)