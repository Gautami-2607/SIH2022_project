import streamlit as st
import pyrebase
from streamlit_option_menu import option_menu
def lgin():
    firebaseConfig = {
    'apiKey': "AIzaSyD8WxalSRDzcrVh2D94xv2crhh-llF5Ckk",
    'authDomain': "test-firestore-streamlit-2e7f6.firebaseapp.com",
    'databaseURL': "https://test-firestore-streamlit-2e7f6-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "test-firestore-streamlit-2e7f6",
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
    st.sidebar.title("Your credentials")

    # Authentication
    choice = st.sidebar.selectbox('Login/Signup', ['Login', 'Sign up'])

    # Obtain User Input for email and password
    email = st.sidebar.text_input('Enter your email address')
    password = st.sidebar.text_input('Enter your password',type='password')

    if choice == 'Sign up':
     fname = st.sidebar.text_input('Enter your first name')
     lname = st.sidebar.text_input('Enter your last name')
     handle = st.sidebar.selectbox('Enter your user type', ['Teacher','Parent','Student','EDO_National',
     'EDO_State','EDO_District',''],index= 6) # handle = user type
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
        login = st.sidebar.button('Login')
        if login:
            user = auth.sign_in_with_email_and_password(email,password)
            '''st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            bio = st.radio('Jump to',['Home','Workplace Feeds', 'Settings'])'''
            fname = db.child(user['localId']).child("First Name").get().val()
            handle = db.child(user['localId']).child("Handle").get().val()
            st.title('Hello  ' + fname )

            




            

    # SETTINGS PAGE 
'''            if bio == 'Settings':  
                # CHECK FOR IMAGE
                nImage = db.child(user['localId']).child("Image").get().val()    
                # IMAGE FOUND     
                if nImage is not None:
                    # We plan to store all our image under the child image
                    Image = db.child(user['localId']).child("Image").get()
                    for img in Image.each():
                        img_choice = img.val()
                        #st.write(img_choice)
                    st.image(img_choice)
                    exp = st.beta_expander('Change Bio and Image')  
                    # User plan to change profile picture  
                    with exp:
                        newImgPath = st.text_input('Enter full path of your profile imgae')
                        upload_new = st.button('Upload')
                        if upload_new:
                            uid = user['localId']
                            fireb_upload = storage.child(uid).put(newImgPath,user['idToken'])
                            a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens']) 
                            db.child(user['localId']).child("Image").push(a_imgdata_url)
                            st.success('Success!')           
                # IF THERE IS NO IMAGE
                else:    
                    st.info("No profile picture yet")
                    newImgPath = st.text_input('Enter full path of your profile image')
                    upload_new = st.button('Upload')
                    if upload_new:
                        uid = user['localId']
                        # Stored Initated Bucket in Firebase
                        fireb_upload = storage.child(uid).put(newImgPath,user['idToken'])
                        # Get the url for easy access
                        a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens']) 
                        # Put it in our real time database
                        db.child(user['localId']).child("Image").push(a_imgdata_url)
    # HOME PAGE
            elif bio == 'Home':
                col1, col2 = st.columns(2)
                
                # col for Profile picture
                with col1:
                    nImage = db.child(user['localId']).child("Image").get().val()         
                    if nImage is not None:
                        val = db.child(user['localId']).child("Image").get()
                        for img in val.each():
                            img_choice = img.val()
                        st.image(img_choice,use_column_width=True)
                    else:
                        st.info("No profile picture yet. Go to Edit Profile and choose one!")
                    
                    post = st.text_input("Let's share my current mood as a post!",max_chars = 100)
                    add_post = st.button('Share Posts')
                if add_post:   
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")              
                    post = {'Post:' : post,
                            'Timestamp' : dt_string}                           
                    results = db.child(user['localId']).child("Posts").push(post)
                    st.balloons()

                # This coloumn for the post Display
                with col2:
                    
                    all_posts = db.child(user['localId']).child("Posts").get()
                    if all_posts.val() is not None:    
                        for Posts in reversed(all_posts.each()):
                                #st.write(Posts.key()) # Morty
                                st.code(Posts.val(),language = '') 
    # WORKPLACE FEED PAGE
            else:
                all_users = db.get()
                res = []
                # Store all the users handle name
                for users_handle in all_users.each():
                    k = users_handle.val()["Handle"]
                    res.append(k)
                # Total users
                nl = len(res)
                st.write('Total users here: '+ str(nl)) 
                
                # Allow the user to choose which other user he/she wants to see 
                choice = st.selectbox('My Collegues',res)
                push = st.button('Show Profile')
                
                # Show the choosen Profile
                if push:
                    for users_handle in all_users.each():
                        k = users_handle.val()["Handle"]
                        # 
                        if k == choice:
                            lid = users_handle.val()["ID"]
                            
                            handlename = db.child(lid).child("Handle").get().val()             
                            
                            st.markdown(handlename, unsafe_allow_html=True)
                            
                            nImage = db.child(lid).child("Image").get().val()         
                            if nImage is not None:
                                val = db.child(lid).child("Image").get()
                                for img in val.each():
                                    img_choice = img.val()
                                    st.image(img_choice)
                            else:
                                st.info("No profile picture yet. Go to Edit Profile and choose one!")
    
                            # All posts
                            all_posts = db.child(lid).child("Posts").get()
                            if all_posts.val() is not None:    
                                for Posts in reversed(all_posts.each()):
                                    st.code(Posts.val(),language = '')'''


        # ---- HIDE STREAMLIT STYLE ----
'''     hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)'''








































    #Config Key
'''firebaseConfig = {
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
    st.sidebar.title("Your Credentials")

    # Authentication
    choice = st.sidebar.selectbox('Login/Signup', ['Login', 'Sign up'])

    # Obtain User Input for email and password
    email = st.sidebar.text_input('Please enter your email address')
    password = st.sidebar.text_input('Please enter your password',type = 'password')

    if choice == 'Sign up':
      fname = st.sidebar.text_input('Enter your first name')
      lname = st.sidebar.text_input('Enter your last name')
      handle = st.sidebar.selectbox('Enter your user type', ['Teacher','Parent','Student','EDO_National',
      'EDO_State','EDO_District',''],index= 6) # handle = user type
      submit = st.sidebar.button('Create my account')

      if submit:
       user = auth.create_user_with_email_and_password(email, password)
       st.success('Your account is created successfully!')
       st.balloons()

       # Sign in
       user = auth.sign_in_with_email_and_password(email,password)
       db.child(user['localId']).child("Handle").set(handle) 
       db.child(user['localId']).child("ID").set(user['localId'])  
       db.child(user['localId']).child("First Name").set(fname)
       db.child(user['localId']).child("Last Name").set(lname)
       st.title('Welcome' + fname)
       
    # Login Block
    if choice == 'Login':
        login = st.sidebar.button('Login')
        if login:
            user = auth.sign_in_with_email_and_password(email,password)
            #st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            #bio = st.radio('Jump to',['Home','Workplace Feeds', 'Settings'])



        # ---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)'''