from keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(train_sentence)
train_sentence = tokenizer.texts_to_sequences(train_sentence)

# labels를 따로 분리
train_labels = np.array(train_data['Emotion'])
train_labels = train_labels.astype('float32')

# 빈 값으로 이루어져있는 샘플 제거
drop_train = [index for index, sentence in enumerate(train_sentence) if len(sentence) < 1]

train_sentence = np.delete(train_sentence, drop_train, axis=0)
train_labels = np.delete(train_labels, drop_train, axis=0)

from keras.preprocessing.sequence import pad_sequences

train_sentence = pad_sequences(train_sentence, maxlen = 15)