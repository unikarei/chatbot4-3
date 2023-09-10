import streamlit as st
import os
import threading

time_limit = 8  # application time limit.

#def shutdown():
#    os._exit(0)

#def close_streamlit_after_delay():
#    threading.Timer(time_limit, shutdown).start()

def main():
    st.title("TEST")

#    close_streamlit_after_delay()

if __name__ == "__main__":
    main()
    
