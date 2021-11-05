from keras.layers import Embedding, Dense, LSTM, Dropout
from keras.models import Sequential, load_model
from keras.callbacks import ModelCheckpoint
from keras import regularizers

embedding_dim = 100

model = Sequential()
model.add(Embedding(10000, embedding_dim))
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(64, kernel_regularizer=regularizers.l2(0.001), activation='tanh'))
model.add(Dropout(0.2))
model.add(Dense(64, kernel_regularizer=regularizers.l2(0.001), activation='tanh'))
model.add(Dropout(0.2))
model.add(Dense(16, activation='tanh'))
model.add(Dense(1, activation='sigmoid'))

mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(train_sentence, train_labels, epochs=10, callbacks=[mc], batch_size=64, validation_split=0.2)

loaded_model = load_model('best_model.h5')