# Product Recommendation System

This project is a Product Recommendation System built using Python and Machine Learning. It recommends similar products based on user ratings using item-based collaborative filtering and cosine similarity. The project also includes an interactive web interface developed with Streamlit.

---

## Project Description
The system analyzes user-product ratings to identify similarities between products. When a user selects a product, the model recommends the most similar products based on cosine similarity scores. Sparse matrices are used for better performance and scalability.

---

## Features
- Item-based collaborative filtering
- Cosine similarity for recommendations
- Interactive Streamlit web application
- Efficient computation using sparse matrices

---

## Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- SciPy  
- Streamlit  

---

## Dataset
The dataset (`rating_short.csv`) contains:
- `userid` – User identifier  
- `productid` – Product identifier  
- `rating` – Rating given by the user  

---

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/your-username/Product-Recommendation-System.git
```

2. Navigate to the project directory:
```bash
cd Product-Recommendation-System
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

---

## Output
Users can select a product from the dropdown menu and receive a list of recommended similar products.

---

## Future Enhancements
- Add user-based recommendations
- Improve UI/UX
- Deploy the application online
- Add evaluation metrics

---

## Author
Shivesh Mishra  
B.Tech in Artificial Intelligence & Data Science
