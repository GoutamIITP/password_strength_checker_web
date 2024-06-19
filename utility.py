import numpy as np
import pickle
 
# Load the pre-trained vectorizer from a pickle file
def load_vectorizer():
    with open("tfidf_password_strength.pickle", 'rb') as file:
        saved_vectorizer = pickle.load(file)
    return saved_vectorizer


# Load the pre-trained model from a pickle file
def load_model():
    with open("final_model.pickle", 'rb') as file:
        final_model = pickle.load(file)
    return final_model


 
def check_password_strength(exampleInputPassword1, saved_vectorizer, final_model):
    # password = np.array([password_chars])
    password = np.array([exampleInputPassword1])
    vectorized_password = saved_vectorizer.transform(password)
    prediction = final_model.predict(vectorized_password)
    return prediction


 