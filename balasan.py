
def sample_responses(input_text, namauser):
    pesan_user = str(input_text).lower()
    
    #======================================
    #Kategori balasan
    sapaan = ["halo", "hi", "hai", "selamat pagi"]
    covidinfo = ["covid", "info covid", "covid 19", "covid-19", "gejala covid"]
    pamitan = ["sampai jumpa", "bye"]
    #=========================================

    #======================================
    #Eksekusi
    if pesan_user in sapaan:
        return f"Halo {namauser}!!"

    if pesan_user in covidinfo:
        return f"{namauser} mau info covid? \n\nTunggu tim riset yaa... :3"

    if pesan_user in pamitan:
        return f"Sampai jumpa {namauser}"
    
   

    return "Aku tidak mengerti"
    #==========================================
