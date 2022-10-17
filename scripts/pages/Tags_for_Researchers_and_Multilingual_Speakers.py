import streamlit as st

st.title("NLP researcher? Or just language savvy? Either way, add a little more flair to your topic tags.") # i.e., Multilingual/Research-oriented Users

# Start of 'Instructions' section #################
st.header("Instructions", anchor=None)

st.text("Fill in 'Instructions' section here!!!")
# End of 'Instructions' section #################

# input user text
st.text_area(
"Paste your text below:", value="",
height=None,
max_chars=None,
key=None,
help=None,
on_change=None,
args=None,
kwargs=None,
placeholder=None,
disabled=False,
label_visibility="visible")

if st.button('Submit'):
    st.write('Please wait...processing text... finding optimal tags...')

    # Fetch data and feed thru model

    # Output results below

# Start of 'Stats for Nerds' section #################
st.header("Stats for Nerds", anchor=None)

# text here
st.text("Fill in 'Stats for Nerds' section here!!!")

# End of 'Stats for Nerds' section #################
