from keras.layers import Embedding, Dense, LSTM, Dropout
from keras.models import Sequential, load_model
from keras.callbacks import ModelCheckpoint
from keras import regularizers
import re

embedding_dim = 100

model = Sequential()
model.add(Embedding(vocab_size, embedding_dim))
model.add(LSTM(128))
model.add(Dropout(0.1))
model.add(Dense(64, kernel_regularizer=regularizers.l2(0.001), activation='tanh'))
model.add(Dropout(0.1))
model.add(Dense(64, kernel_regularizer=regularizers.l2(0.001), activation='tanh'))
model.add(Dropout(0.1))
model.add(Dense(16, activation='tanh'))
model.add(Dense(1, activation='sigmoid'))

mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(train_sentence, train_labels, epochs=10, callbacks=[mc], batch_size=64, validation_split=0.2)

loaded_model = load_model('best_model.h5')

def sentiment_predict(new_sentence):
  new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
  new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
  new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
  encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
  pad_new = pad_sequences(encoded, maxlen = 15) # 패딩
  score = float(loaded_model.predict(pad_new)) # 예측
  if(score > 0.5):
    print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
  else:
    print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))