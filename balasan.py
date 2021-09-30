
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
    
   def covid(message):
        texts = pesan_user
        provinsi = texts[7:]
        page = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
        page_json = page.json()
        features = page_json['features']
        for i in features:
            prov = i['attributes']['Provinsi']
            pos =  i['attributes']['Kasus_Posi']
            sem = i['attributes']['Kasus_Semb']
            men = i['attributes']['Kasus_Meni']
            dirawat = int(pos)-int(sem)-int(men)
            data = ('''
        Provinsi = {}
        Positif = {}
        Sembuh = {}
        Meninggal= {}
        Dirawat = {}
        '''.format(prov, pos, sem, men, dirawat))
    if provinsi.upper() in prov.upper():
        return (message, data)
    else:
     #       pass

    return "Aku tidak mengerti"
    #==========================================
