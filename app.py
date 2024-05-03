import streamlit as st
st.title('Hello World ,Welcome to this world.')
st.header('Header ->Hi,Everyone.')
st.subheader('Sub-Header ->Hello')
st.text('My name is Anurag')

st.markdown(' # Hi')
st.markdown('## Hi')
st.markdown('### Hi')

st.markdown('#### Hi')

st.success('Data is Submitted !') #success
st.info('information !,Data is Submitted')      #info
st.warning('Warning !') #warning

st.error('Error') #error

exp =ZeroDivisionError('Division not possible !')
st.exception(exp)

st.help(ZeroDivisionError)

st.write("range(1,10)")
st.write(range(1,10))
st.write("1+2+3")
st.write(1+2+3)

st.code('x =10 \n'
        'for i in range(x): \n'
        '\tprint(i)')

st.checkbox('Male')               #checkbox

if(st.checkbox('Adult')):
    st.write("You are an Adult!")

st.radio('Select: ',('Male','Female','Others'))
radiobutton =st.radio('Select :',('Male','Female','Other'))

if(radiobutton =='Male'):
    st.write("You are a Male.")

elif(radiobutton =='Female'):
    st.write('You are Female.')
elif(radiobutton =='Other'):
    st.write('You are other.')

st.subheader('Select Box')
selectbox =st.selectbox("Data Science :",['Data Analysis','Web Scrapping','Machine Learning','Deep Learning','Image Processing',
'Natural Language Processing'])

st.write("You have selected this one:" ,selectbox)

st.subheader('MultiSelect Box')
MultiSelectBox =st.multiselect("Data Science :",['Data Analysis','Web Scrapping','Machine Learning','Deep Learning','Image Processing',
'Natural Language Processing'])

st.write("You have selected :",len(MultiSelectBox),MultiSelectBox)
st.write("You have selected :",len(MultiSelectBox),'courses')
st.subheader("Button")
st.button('Button')
if(st.button('Click me')):
    st.write('Thanks for clicking.')

st.subheader("Slider")
vol =st.slider('Select the volume',0,100,step=1)
st.write('Volume ',vol)

st.subheader("text Input")
username =st.text_input('Username :')
if(username):
    st.write('Hi ,',username)    #text Input
password =st.text_input('Password :',type ='password')

st.subheader("Text Area")               #Text Area
textArea =st.text_area('Write about yourself in 500 words:',height =20)
st.write(textArea)

st.subheader("Input Number.")              #Input -Number
st.number_input('Select your age',18,110)

st.subheader("Input Date.")               #Input -Date
st.date_input('Date')

st.subheader("Input Time.")               #Input -time
st.time_input('Time')