import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import joblib

from sklearn.datasets import fetch_20newsgroups

dataset = fetch_20newsgroups(subset='train', categories=['rec.autos', 'sci.med'], remove=('headers', 'footers', 'quotes'))

df = pd.DataFrame({'text': dataset.data, 'label': dataset.target})

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

joblib.dump(model, "automobile_or_medicine_model.pkl")

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
