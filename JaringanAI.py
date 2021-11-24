import random
import json
import pickle
import numpy as np

import nltk  # punkt, wordnet
#nltk.download('punkt')
#nltk.download('wordnet')

import telegram
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD


def train(update, context):
    update.message.reply_text("*Bot sedang dilatih untuk mempelajari percakapan mengunakan AI*\n\nMohon tunggu", parse_mode=telegram.ParseMode.MARKDOWN_V2)

    lemmatizer = WordNetLemmatizer()

    maksud = json.loads(open('Sampel AI/DataKalimat.json').read())

    # ======================== Memasukkan data Latihan AI ============================

    katakata = []
    classes = []
    dokumen = []
    kata_yang_diabaikan = ['?', '!', '.', ',']

    for intent in maksud['maksud']:
        for pola in intent['pola']:
            daftar_kata = nltk.word_tokenize(pola)
            katakata.extend(daftar_kata)
            dokumen.append((daftar_kata, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    # ==================== Pengolahan Data Training AI ========================================

    katakata = [lemmatizer.lemmatize(kata) for kata in katakata if kata not in kata_yang_diabaikan]
    katakata = sorted(set(katakata))

    classes = sorted(set(classes))

    pickle.dump(katakata, open('Sampel AI/katakata.pkl', 'wb'))
    pickle.dump(classes, open('Sampel AI/classes.pkl', 'wb'))

    training = []
    output_kosong = [0] * len(classes)

    for document in dokumen:
        bag = []
        pola_kata = document[0]
        pola_kata = [lemmatizer.lemmatize(kata.lower()) for kata in pola_kata]
        for kata in katakata:
            bag.append(1) if kata in pola_kata else bag.append(0)

        output_row = list(output_kosong)
        output_row[classes.index(document[1])] = 1
        training.append([bag, output_row])

    random.shuffle(training)
    training = np.array(training)

    train_x = list(training[:, 0])
    train_y = list(training[:, 1])

    # ======================= Jaringan Model AI =============================================

    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(len(train_y[0]), activation='softmax'))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    update.message.reply_text("Epoch = 200\nModel = Sequential\nTraining started")

    hasil = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
    model.save('Sampel AI/ICA_AIModel.h5', hasil)

    update.message.reply_text("Pelatihan bot selesai")
