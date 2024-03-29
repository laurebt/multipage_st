import streamlit as st

st.markdown("# API call")
st.sidebar.markdown("# API call")

def get_summary(name = "Daisi user"):
    text = '''
    This Daisi is a simple endpoint to a *Hello World* function, with a straightforward
    Streamlit app.
    Call the `hello()` endpoint in Python with `pydaisi`:
    ```python
    import pydaisi as pyd
    print_hello_app = pyd.Daisi("Print Hello App")
    greetings = print_hello_app.hello("'''
    text += name + '''").value
    print(greetings)
    ```
    '''

    return text

name = st.text_input('Type your name', value = "Daisi user")
st.markdown(get_summary(name))

