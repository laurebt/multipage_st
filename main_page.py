import streamlit as st

def hello(name="World"):
  '''
  Simple hello function
  Parameters:
  - name (str) : any string
  Returns:
  - a string
  '''
  return "Hello " + str(name) + ", from the Daisi platform"

def st_ui():
  '''Function to render the Streamlit UI'''

  st.markdown("# Main page 🎈")
  st.sidebar.markdown("# Main page 🎈")

  name = st.text_input('Type your name', value = "Daisi user")
  greeting = hello(name)
  st.header(greeting)

  with st.expander("Summary"):
        st.markdown(get_summary(name))

if __name__ == "__main__":
  st_ui()
