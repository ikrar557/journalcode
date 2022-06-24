#Inventory Management System
#Thanks to "Momen Shilia" for guide, linkendin "https://www.linkedin.com/in/momen-shili-a00291192/"

#Dictionaries
unit_price={}
description={}
stock={}

#Untuk membuka file stock
details = open("stock.txt","r")

#"readline()", digunakan untuk membaca line pada file yang ditunjuk

no_items  = int((details.readline()).rstrip("\n")) #First line of the file is the number of items

#Menambahkan item ke dalam Dictionaries
for i in range(0,no_items):
    #"rstrip()", untuk menghapus character yang ditunjuk
    line  = (details.readline()).rstrip("\n")
    #"split()", merubah string menjadi list
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=float(x2)

    #Dictionary "update()" with "key : value" format
    unit_price.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)

    #Dictionary Update
    description.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=int(x2)

    #Dictionary Update
    stock.update({x1: x2})

details.close()
#List untuk menyimpan barang
cart=[]

#Perintah yang digunakan
print("Inventory Management Systems \n")
print("A - Tambahkan Barang")
print("R - Hapus Barang")
print("E - Edit Barang Tertentu")
print("L - Tampilkan List Barang")
print("D - Detail Barang")
print("B - Beli Barang")
print("C - Checkout")
print("S - Tampilkan Barang Yang Dibeli")
print("Q - Keluar")
print("X - Hapus Barang Dari Keranjang")
print("Help - Tampilkan Bantuan \n")

#Giving "0" to variable, agar bisa dipanggil dan digunakan
total_cost=0 
flag=0 #To check if they have checked out
c=0 #Variabel untuk menyimpan input key dari user

while(c != "q" or c != "Q"):
    c = input("Pilih Aksi : ")

    if(c == "q" or c == "Q"):
        break
        
    elif(c == "A" or c == "a"): #Tambah Barang
        part_no     = int(input("Nomor Barang : "))
        part_price  = int(input("Harga Barang : "))
        part_desc   = input("Detail Barang : ")
        part_stock  = int(input("Jumlah Stock Barang: "))
        
        m = 0
        for i in range(0,len(unit_price)):
            if(part_no in unit_price):
                part_no += 1
                m = 1
        if( m == 1 ):
            print()
            print("Nomor Barang Sudah Terdaftar, Nomor Barang Diganti Menjadi ", part_no)
                
        unit_price.update({part_no: part_price})
        description.update({part_no: part_desc})
        if(part_stock > -1):
            stock.update({part_no: part_stock})
        else:
            part_stock = 0
            stock.update({part_no: part_stock})
            print("Jumlah Stock Barang Tidak Boleh Minus, Stock Barang Sudah Diganti Menjadi 0")
        print()
        print("Nomor Barang :",part_no,"\nDetail :",description.get(part_no),"\nHarga :",unit_price.get(part_no),"\nStock :",stock.get(part_no))
        print("Berhasil Menambahkan Barang")
        print()
        
    elif(c=="E" or c=="e"):#Edit Barang
        print()
        part_no = int(input("Nomor Barang: "))
        if(part_no in unit_price):
            part_price  = int(input("Harga Barang: "))
            part_desc   = input("Detail Barang: ")
            part_stock  = int(input("Jumlah Stock: "))
                
            unit_price.update({part_no: part_price})
            description.update({part_no: part_desc})
            stock.update({part_no: part_stock})
            
        else:
            print("Barang tidak tersedia, untuk menambahkan barang gunakan key A/a")
        print()
    
            # Implementasi "Stack" metode "Dictionaries"
    elif(c == "R" or c == "r"):#Hapus barang
        print()
        part_no = int(input("Nomor Barang: "))
        if(part_no in unit_price):
            delete_item = input("Yakin Untuk Menghapus Barang(y/n)? ")
            if(delete_item == "y" or delete_item == "Y"):
                unit_price.pop(part_no)
                description.pop(part_no)
                stock.pop(part_no)
                print("Barang Berhasil Dihapus!")
            print()
        else:
            print("Maaf, Barang Tidak Tersedia!")
            print()
        
    elif(c == "L" or c == "l"):#Menampilkan Semua Barang
        print()
        print("Barang dan Harganya :\n",unit_price, "\n")
        print("Deskripsi : ")
        print(description)
        print("\nStock :\n", stock)
        print()

    elif(c == "D" or c == "d"):#Detail Barang
        print()
        part_no=int(input("Nomor Barang: "))
        if(part_no in unit_price):
            print()
            print("Nomor Barang :",part_no,"\nDeskripsi :",description.get(part_no),"\nHarga :",unit_price.get(part_no),"\nStock :",stock.get(part_no))
            if(stock.get(part_no) <3 and stock.get(part_no)!=0):
                print("Hanya Tersisa",stock.get(part_no),)
            print()
        else:
            print("Barang Tidak Tersedia")
            print()
        
    elif(c == "B" or c == "b"):#Membeli Barang
        print()
        part_no = int(input("Nomor Barang: "))
        if(part_no in unit_price):
            if(flag == 1):
                flag = 0
            stock_current = stock.get(part_no)
            if(stock_current > 0):
                stock_current   = stock.get(part_no)
                stock[part_no]  = stock_current-1
                item_price      = unit_price.get(part_no)
                total_cost      = total_cost + item_price
                print(description.get(part_no),"Ditambahkan ke Keranjang: ","Rp",item_price)
                # Menyimpan barang di keranjang
                cart.append(part_no)
            else:
                print("Maaf, Stock Barang Kosong")
        else:
                print("Barang Tidak Tersedia")
        print()

    elif(c == "s" or c == "S"):#Cetak list keranjang
        print("\n",*cart, sep = "\n") #sep & * untuk menampilkan list dengan new line

        
    elif(c == "C" or c == "c"):#Check out
        if len(cart) < 1:
            print("\nAnda Belum Memilih Barang\n")
        else:
            print("\nAnda Membeli Barang Sebagai Berikut: ", cart)
            print("Jumlah Total: ","Rp",round(total_cost, 2))
            tax = round(0.13 * total_cost,2)
            print("Pajak 13%: ","Rp", tax)
            total = round(total_cost + tax, 2)
            print("Setelah Pajak: ","Rp", total)
            total_cost = 0
            flag = 1
            print("\nAnda Masih Bisa Membeli Barang Setelah Keranjang Dihapus. Untuk keluar tekan 'q'\n")
            #Menghapus semua barang dari list keranjang
            cart.clear()
            
        #Implementasi "Stack" metode list
    elif(c=="x" or c=="X"):#Menghapus Barang Dari Keranjang
        print()
        delete_item = input("Yakin Untuk Menghapus Barang Dari Keranjang(y/n)? ")
        if(delete_item=="y"):
            part_no = int(input("Nomor Barang Yang Akan Dihapus: "))
            if(part_no in cart):
                stock_current = stock.get(part_no)
                stock[part_no] = stock_current+1
                item_price = unit_price.get(part_no)
                total_cost = total_cost-item_price
                j=0
                cart.pop()
                print(description.get(part_no),"Dihapus dari Keranjang: ")
                print()
            else:
                print("\nBarang Tidak Ada di Keranjang\n")

        #Tampilkan Semua Perintah
    elif(c == "help" or c == "h" or c == "Help" or c == "H"):
        print("A - Tambahkan Barang")
        print("R - Hapus Barang")
        print("E - Edit Barang Tertentu")
        print("L - Tampilkan List Barang")
        print("D - Detail Barang")
        print("B - Beli Barang")
        print("C - Checkout")
        print("S - Tampilkan Barang Yang Dibeli")
        print("Q - Keluar ")
        print("X - Hapus Barang Dari Keranjang")
        print("Help - Tampilkan Bantuan \n")

    else:
        print("\nERROR! Hubungi Karyawan Untuk Meminta Bantuan \n")


#Total Belanja user yang tidak melakukan checkout
if(total_cost > 0 and flag == 0):
    print()
    print("Anda Membeli: ", cart)
    print("Jumlah Total: ","Rp",round(total_cost, 2))
    tax = round(0.13 * total_cost, 2)
    print("Pajak 13%: ","Rp", tax)
    total = round(total_cost + tax, 2)
    print("Setelah Pajak ","Rp",total)
    
print("\n\nInventory Management System \n")

#Update inventory ke "stock.txt"
details = open("stock.txt", "w")
no_items = len(unit_price)
details.write(str(no_items)+"\n")
for i in range(0,no_items):
    details.write(str(i+1) + "#" + str(unit_price[i+1])+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1) + "#" + description[i+1]+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1) + "#" + str(stock[i+1])+"\n")
    
details.close()
