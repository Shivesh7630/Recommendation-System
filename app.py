# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 13:17:36 2025

@author: beaut
"""

import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Load data
df = pd.read_csv("rating_short.csv")

# Create mappings for users and products
user_codes = pd.Categorical(df['userid']).codes
product_codes = pd.Categorical(df['productid']).codes

# Build sparse matrix
sparse_matrix = csr_matrix((df['rating'], (user_codes, product_codes)))

# Calculate item-item similarity
item_similarity = cosine_similarity(sparse_matrix.T, dense_output=False)

# Mappings
prod_index = dict(enumerate(pd.Categorical(df['productid']).categories))
id_to_index = {v: k for k, v in prod_index.items()}

# Recommend function
def recommend(product_id, n=5):
    if product_id not in id_to_index:
        return []
    idx = id_to_index[product_id]
    scores = item_similarity[idx].toarray().ravel()
    top = scores.argsort()[-n-1:][::-1]
    return [prod_index[i] for i in top if i != idx][:n]

# Streamlit App
st.title("Product Recommendation System")

# Product selection
product_ids = df['productid'].unique()
selected_product = st.selectbox("Select a product", product_ids)

# Recommendation
if st.button("Get Recommendations"):
    recommendations = recommend(selected_product, n=5)
    st.write("Recommended products:")
    for product in recommendations:
        st.write(product)







