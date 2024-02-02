# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
  
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    
    st.write("# Welcome to Streamlit! 👋")
    
    st.sidebar.success("Select a demo above.")
    st.title('อ่านและแสดงข้อมูลจากไฟล์ CSV')
    uploaded_file = st.file_uploader("อัปโหลดไฟล์ CSV ของคุณที่นี่", type=["csv"])

    if uploaded_file is not None:
    
       df = pd.read_csv(uploaded_file) 
       st.write("ข้อมูลจากไฟล์ CSV:")
       st.dataframe(df)
        
       column_options = df.columns.tolist()
       x_axis = st.selectbox('เลือกคอลัมน์สำหรับแกน X:', column_options, index=0)
       y_axis = st.selectbox('เลือกคอลัมน์สำหรับแกน Y:', column_options, index=1)

  
       plt.figure(figsize=(10, 4))
       plt.plot(df[x_axis], df[y_axis], marker='o')
       plt.title('กราฟเส้นจากข้อมูล CSV')
       plt.xlabel(x_axis)
       plt.ylabel(y_axis)
       st.pyplot(plt)

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - TEST22 [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
