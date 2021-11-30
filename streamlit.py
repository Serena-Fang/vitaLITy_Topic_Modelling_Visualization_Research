import streamlit as st
import pandas as pd
import json

with open('repre_list.json') as json_file:
    docs = json.load(json_file)

with open('full.json') as json_file:
    full = json.load(json_file)

topics = list(docs.keys())
papers = list(docs.values())
fulls = list(full.values())

st.write("Hello")

sel_col, disp_col = st.columns(2)
word = sel_col.text_input("Enter the topic you interested in")

def find_repre(word):
  for i in range(len(topics)):
    keywords = topics[i].split('_')[1:]
    if word in keywords:
        st.write('Representative papers about "' + word + '":')
        for paper in papers[i]:
            st.write(paper)
        click = st.button('Abstracts')
        if click:
            for full in fulls[i]:
                text = full.replace('[SEP]', '\n\n')
                st.write(text)


find_repre(word)

