print("Está chovendo?")

esta_chovendo = input("Está chovendo? (s/n): ").lower() == "s"

if not esta_chovendo :
    print("Não está chovendo. Você pode sair sem guarda-chuva.")
else :
    print("Está chovendo. Leve um guarda-chuva!")
