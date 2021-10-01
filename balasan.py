def sample_responses(input_text, namauser):
    pesan_user = str(input_text).lower()
    
    #======================================
    #Kategori balasan
    perkenalan = ["apa kabar", "siapa kamu", "siapa namamu", "kamu siapa"]
    sapaan = ["halo", "hi", "hai", "selamat pagi"]
    covidinfo = ["covid", "info covid", "covid 19", "covid-19", "gejala covid"]
    pamitan = ["sampai jumpa", "bye", "selamat tinggal"]
    #=========================================
    #respon
    sapabalik = ["Hai", "halo", "Ada yang bisa dibantu?", "Selamat pagi"]
    #Eksekusi
    if pesan_user in sapaan:
        sapakembali = random.choice(sapabalik)
        return sapakembali
    
    if pesan_user in covidinfo:
        return f"{namauser} mau info covid? \n\nTunggu tim riset yaa... :3"
                 
    if pesan_user in perkenalan:
        return f"Saya adalah ICA, Indonesian Covid Assistant\n/nSaya akan membantu anda mencari informasi seputar Covid-19"

    if pesan_user in pamitan:
        return f"Sampai jumpa {namauser}"
   

   

    return "Aku tidak mengerti"
    #==========================================
