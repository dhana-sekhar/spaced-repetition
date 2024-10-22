# import streamlit as st
# import time

# # Simulate load
# def heavy_computation():
#     with st.spinner('Processing...'):
#         time.sleep(15)  # Simulates heavy computation

# st.title("Kubernetes Load Balancer Test")
# st.write("Increase load on the pods to test replication and failover.")

# if st.button("Start Heavy Load"):
#     heavy_computation()
#     st.success('Computation completed!')


import streamlit as st
import time
import os
import signal

# Simulate load
def heavy_computation():
    with st.spinner('Processing...'):
        time.sleep(25)  # Simulate heavy computation

# Function to crash the Streamlit app
def crash_streamlit():
    st.write("Stopping the Streamlit server after this request...")
    os.kill(os.getpid(), signal.SIGTERM)  # Sends a termination signal to the Streamlit process

st.title("Kubernetes Load Balancer Test")
st.write("This app will crash after processing one request.")

if st.button("Start Heavy Load"):
    heavy_computation()
    st.success('Computation completed!')
    crash_streamlit()  # Terminate Streamlit after the request
