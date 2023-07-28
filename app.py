import streamlit as st
import hebrew as hb

def main():
    st.write("hello")
    st.markdown("""
        <style>
        input {
        unicode-bidi:bidi-override;
        direction: RTL;
        }
        </style>
            """, unsafe_allow_html=True)

    input = st.text_input("Write the line in hebrew here:")
    line = hb.Hebrew(input)
    st.write(line)
    # st.write('value 1: "', i1, '"')


if __name__ == '__main__':
    main()