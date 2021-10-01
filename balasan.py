import requests
import json


def sample_responses(input_text, namauser):
    pesan_user = str(input_text).lower()
    
    #======================================
    #Kategori balasan
    perkenalan = ["apa kabar", "siapa kamu", "siapa namamu", "kamu siapa"]
    sapaan = ["halo", "hi", "hai", "selamat pagi"]
    covidinfo = ["covid", "info covid", "covid 19", "covid-19", "gejala covid"]
    pamitan = ["sampai jumpa", "bye", "selamat tinggal"]
    #=========================================
    #Eksekusi
    if pesan_user in sapaan:
        return f"Halo {namauser}!!"
    
    
                 
    if pesan_user in perkenalan:
        return f"Saya adalah ICA, Indonesian Covid Assistant\n/nSaya akan membantu anda mencari informasi seputar Covid-19"

    if pesan_user in pamitan:
        return f"Sampai jumpa {namauser}"
   

   

    return "Aku tidak mengerti"
    #==========================================
