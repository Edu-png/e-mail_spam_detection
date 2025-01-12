import pickle

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

model = pickle.lead(open('model.pkl', 'rb'))

st.title('E-mail/SMS Spam Classifier')

input_sms = st.text_input('Enter the message')

if st.button('Predict'): 
  # 1. Preprocess
  transformed_sms = transform_text(input_sms)

  # 2. Vectorize
  vector_input = tfidf.transform([transformed_sms])

  # 3. Predict
  result = model.predict(vector_input)[0]

  # 4. Display
  if result == 1:
      st.header("Spam")
  else:
      st.header("Not Spam")
