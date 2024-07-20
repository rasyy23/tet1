import streamlit as st
import pandas as pd

kontol=pd.DataFrame({"column 1": [1,2,3,4,5,6,7], "column 2": [11,12,13,14,15,16,17]})

st.markdown("""
<style>
.css-d1b1ld.edgvbvh6
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.title("ini title")
st.header("ini header")
st.subheader("ini subheader")
st.text("ini text")
st.text("lorem ipsum dolot")
st.markdown("ini markdown")
st.markdown("[rasya gg anjay slebewww](https://www.instagram.com/kurai_nogomi?igsh=cmM0YTY5YW1neng3) mark down bisa untuk hyperlink dan juga untuk menggunakan code yg ada di html contoh h1 h2 dll")
st.markdown("---")
st.caption("ini caption")
st.latex(r"\begin{bmatrix}asu & bgst \\cicak & dongok\end{bmatrix}")
json={"a":"1,2,3","b":"4,5,6" "       test json gess"}
st.json(json)
code="""
print("hello world")
def funct():
    return 0;
print('test stcode')"""
st.code(code,language="python")
st.code(code)
st.code('for i in range(8): foo()')

st.write("## H2")
st.write("### H3")
st.write(['st', 'is <', 3])

st.metric(label="heart beat when i see kobo", value="103bpm²", delta="-lower in case ",)##arrow look down if u add (-) ,and if u not add anything the arrow look at top
st.table(kontol[0:10])
st.dataframe(kontol)

st.image('goblin.jpeg', caption="dicari suka maling bh", width=100)
st.audio('LaguDanceChina(1).mp3')
st.video('y2mate.com - Lirik Imase  Night Dancer Penari Malam Terjemahan music video RomKanIndo_720pFHR.mp4')

# Three columns with different widths
col1, kontol, col3 = st.columns([3,1,2])#membuat jarak column
# col1 is wider
col1.write('hello boy')
kontol.write('gelooooo')
col3.write('anjay kelas')

# Using 'with' notation:
with col1:
    st.write('ini kolom 1')
    st.write('ini kolom 2')
    st.write('ini kolom 3')
with kontol:
    st.write('anjay')
    st.write('mabar')
    st.write('propesonal')
with col3:
    st.write('none')
    st.write('none')
    st.write('none')

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("mini tab anying")
tab2.write("make life easier")

# You can also use "with" notation:
with tab1:
  st.radio('Select one:', [1, 2])
    
# Stop execution immediately:
#st.stop()
# Rerun script immediately:
#st.experimental_rerun()

# Group multiple widgets:
with st.form(key='my_form'):
  username = st.text_input('Username')
  password = st.text_input('Password')
  st.form_submit_button('Login')

# Show different content based on the user's email address.
#if st.username.email == 'jane@email.com':
#   display_jane_content()
#elif st.user.email == 'adam@foocorp.io':
#   display_adam_content()
#else:
#   st.write("your account not registed yet!")

st.checkbox('Check me out') #checkbox
state=st.checkbox("hello button", value=True)
if state:
    st.write('hi')
else: 
    pass

def change():
    print(st.session_state.checker)
state=st.checkbox("yes", value=True, on_change=change, key="checker")

st.radio('Pick one:', ['nose','ear']) #pilih2an bentuk bulat
#radio_btn=st.radio("in which country do you live?", options=("US","UK","Canada","Indonesia",""))
#print(radio_btn)

st.button('Hit me') #tombol
def btn_click():
    print("button clicked")
btn=st.button("click me", on_click=btn_click)

st.selectbox('Select', [1,2,3]) # pilihan

 
st.multiselect('Multiselect', [1,2,3])#pilihan tapi bisa pilih lebih dari 1
st.slider('Slide me', min_value=0, max_value=10) #slider kayak rating ig
st.select_slider('Slide to select', options=[1,'2']) #??
st.text_input('Enter some text') # untuk masukin text cocok untk data nama
st.number_input('Enter a number')
st.text_area('Area for textual entry')


