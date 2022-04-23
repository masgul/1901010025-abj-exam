file = open ("db-Inventory.txt","a")
while True:
    x = input ("Masukan Data Inventory Baru (ya/tidak)")
    print ('******************************************')
    if x == 'tidak':
        file = open ("db-Inventory.txt","r")
        for item in file:
            item=item.strip()
            print(item)
        file.close()
        break
    
    elif x == 'y' or 'ya':
        perangkat = input("Nama Perangkat : ")
        lokasi = input("Lokasi: ")
        file.write("Nama Perangkat : " + perangkat + ", Lokasi: " + lokasi + "\n")
        print('-------------------------------------------')
        file.close()