import random
import json
import pickle
import numpy as np

import nltk
from nltk import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()


katakata = pickle.load(open('Sampel AI/katakata.pkl', 'rb'))
classes = pickle.load(open('Sampel AI/classes.pkl', 'rb'))
model = load_model('Sampel AI/ICA_AIModel.h5')

def pembersihkan_kalimat(kalimat):
    text_kalimat = nltk.word_tokenize(kalimat)
    text_kalimat = [lemmatizer.lemmatize(kata) for kata in text_kalimat]
    
    return text_kalimat

def kumpulan_kata(kalimat):
    text_kalimat = pembersihkan_kalimat(kalimat)
    bag = [0] * len(katakata)

    for w in text_kalimat:
        for i, kata in enumerate(katakata):
            if kata == w:
                bag[i] = 1

    return np.array(bag)

def prediksi_kalimat(kalimat):
    tas = kumpulan_kata(kalimat)
    prediksi = model.predict(np.array([tas]))[0]

    batasan_error = 0.25

    hasil = [[i, r] for i, r in enumerate(prediksi) if r > batasan_error]
    hasil.sort(key=lambda x: x[1], reverse=True)

    daftar_hasil = []
    for r in hasil:
        daftar_hasil.append({'maksud1': classes[r[0]], 'kemungkinan': str(r[1])})

    return daftar_hasil

def dapatkan_balasan(maksudkata, maksudkata_json):
    tag = maksudkata[0]['maksud1']
    daftar_maksud = maksudkata_json['maksud']
    for i in daftar_maksud:
        if i['tag'] == tag:
            text_balasan = random.choice(i['balasan'])
    return text_balasan

def sample_responses(input_text, namauser):
    maksud = json.loads(open('Sampel AI/DataKalimat.json').read())

    pesan_user = str(input_text)
    prediksi_arti_pesan = prediksi_kalimat(pesan_user)
    balasan = dapatkan_balasan(prediksi_arti_pesan, maksud)

    return balasan
