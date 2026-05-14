import numpy as np
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.utils import to_categorical

# Load dataset
with open("../dataset/text_data.txt", "r", encoding='utf-8') as f:
    data = f.read()

# Preprocessing
data = data.lower()
sentences = data.split("\n")

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
total_words = len(tokenizer.word_index) + 1

# Create sequences
input_sequences = []
for line in sentences:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_seq = token_list[:i+1]
        input_sequences.append(n_gram_seq)

# Padding
max_seq_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_seq_len, padding='pre'))

# Split data
X = input_sequences[:, :-1]
y = input_sequences[:, -1]
y = to_categorical(y, num_classes=total_words)

# Model
model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_seq_len-1))
model.add(LSTM(150))
model.add(Dense(total_words, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train
model.fit(X, y, epochs=50, verbose=1)

# Save model & tokenizer
model.save("../backend/next_word_model.h5")

with open("../backend/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("Model trained and saved!")