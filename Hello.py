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
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
  
    st.set_page_config(
        page_title="Hii",
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
       if 'time' in df.columns:
           df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.time
           df = df.set_index('time')
           st.line_chart(df)
       else:
           st.error("ไม่พบคอลัมน์ 'time' ในไฟล์ CSV ที่อัปโหลด.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - TTTTTasd [streamlit.io](https://streamlit.io)
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
