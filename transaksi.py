from rich.console import Console
from rich.table import Table
from itertools import chain
from collections import defaultdict

"""
Class color untuk membuat warna pada teks
"""
class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
class Transaksi:
    nama_customer = ""
    _item = {
        "CITATO":10000,
        "SABUN MANDI":15000,
        "PASTA GIGI":8000,
        "ROTI":3000
    }
    _header_item ={"No":"cyan",
                  "Item":"magenta",
                  "Harga":"green"}
    _order = {}
    _header_order ={"No":"cyan",
                  "Item":"magenta",
                  "Harga":"green",
                  "Jumlah":"green",
                  "Total":"green"}
    diskon = []
    def __init__(self):
        print(f"Selamat datang di AndyMart")
        Transaksi.nama_customer = input("Masukkan Nama Anda : ") 


    """
    untuk menampilkan table dari data Transaksi._item
    """
    def table(self):
        # print("-"*30,"\n")
        print(f"Berikut item yang tersedia\n")
        self.table_item = Table(title="List Item Andy Mart")

        self._item = Transaksi._item
        self._header_item = Transaksi._header_item

        for index,key in enumerate(self._header_item.items()):
            self.table_item.add_column(f"{key[0]}", style=f"{key[1]}")

        for index,key in enumerate(self._item.items()):
            self.table_item.add_row(f"{index}",f"{key[0]}",f"Rp {int(key[1]):,}")

        console = Console()
        console.print(self.table_item)

    """
    untuk menampilkan table dari data Transaksi._order
    """
    def table_order(self):
        self.table_order_item = Table(title="Item yang anda order sebagai berikut")
        self._item = Transaksi._item
        self._order = Transaksi._order
        self._header_order = Transaksi._header_order
        dict3 = defaultdict(list)
        total_diskon = 0

        for k, v in chain(self._item.items(), self._order.items()):
            dict3[k].append(v)

        for index,key in enumerate(self._header_order.items()):
            if index != 0 :
                self.table_order_item.add_column(f"{key[0]}", style=f"{key[1]}")

        for key,value in dict3.items():
            try:
                harga = value[0]
                jumlah = value[1]
                total = harga * jumlah
                self.table_order_item.add_row(f"{key}",f"Rp {int(harga):,}",f"{int(jumlah)}",f"Rp {int(total):,}")
                total_diskon += total

            except:
                continue

        console1 = Console()
        console1.print(self.table_order_item)

        self.diskon = [total_diskon-(total_diskon*0.1),'10%'] if total_diskon > 500000 else [total_diskon-(total_diskon*0.08),'8%'] if total_diskon > 300000 else [total_diskon-(total_diskon*0.05),'5%'] if total_diskon > 200000 else [total_diskon,'0']
        if self.diskon[1] != '0':
            print(f"Anda mendapatkan diskon sebesar {self.diskon[1]} dari Rp {int(total_diskon)} sehingga yang dibayar adalah {Color.BOLD}Rp {int(self.diskon[0])}{Color.END}")
        else:
            print(f"Total Jumlah yang dibayar adalah {Color.BOLD}Rp {self.diskon[0]}{Color.END}")
            
    """
    - untuk mengecek item 
      > jika ada akan masuk ke function update_qty_item
      > jika tidak ada/tidak sesuai akan gagal
      > jika ketik back akan kembali ke menu 
    """
    def tambah(self):
        while True:
            print(f"- Ketik {Color.RED}BACK{Color.END} jika ingin kembali")
            print(f"- Ketik {Color.YELLOW}nama item{Color.END} jika ingin mengupdate jumlah item")
            pilih = input("Silahkan masukkan item yang ingin dibeli : ").upper()
            if pilih in Transaksi._item:
                self.update_qty_item(pilih)
                print(f"Pesanan Anda {Transaksi._order}\n")
            elif pilih.upper() == "BACK":
                # self.table()
                break
            else:
                print(f"\nitem {Color.RED}{pilih}{Color.END} tidak ada dalam table, silahkan cek ulang kembali\n")
                break
        
    """
    untuk menambah dan mengupdate jumlah item yang dipesan
    """
    def update_qty_item(self, nama_item):
        while True:
            try:
                jumlahItem = input(f"{Color.BOLD}Pilih jumlah Item : {Color.END}").upper()
                if jumlahItem == "BACK":
                    break
                else:
                    jumlahItem = int(jumlahItem)
                    Transaksi._order[nama_item]=jumlahItem
                print(f"\n{Color.CYAN}Pesanan telah diupdate, silahkan menambahkan item lagi{Color.END}")
                break
            except:
                print(f'{Color.RED}Masukkan Decimal/Jumlah Item{Color.END}')
    
    """
    - untuk menampilkan order yang telah dipesan
    - untuk menampilkan dan memilih opsi (check out, remove, back)
    """                
    def check_order(self):
        if len(Transaksi._order) == 0:
            print(f"{Color.UNDERLINE}{Color.BOLD}Anda belum menambahkan / mengorder item, silahkan order dengan mengetik angka 1, Terima kasih{Color.END}\n")
        else:
            self.table_order()
            while True:
                # print("\n")
                print(f"{Color.BLUE}1. Check Out{Color.END} (FINISH)\n{Color.YELLOW}2. Remove{Color.END} (DELETE/RESET Item)\n{Color.RED}3. BACK{Color.END} (Menu Utama)")
                pilih = input("Silahkan pilih opsi (1/2/3) : ")
                if pilih == "1":
                    selesai = input("\nAnda yakin ingin menyelesaikan pembayaran (Yes=Y, No=press any key)? ").upper()
                    # while True:
                    if selesai == "Y":
                        print(f"Silahkan membayar item anda sebesar {Color.BOLD}Rp {int(self.diskon[0])}{Color.END}\nTerima kasih sudah berkunjung ke AndyMart saudara/i {self.nama_customer.upper()} \n")
                        exit()
                    else:
                        continue
                elif pilih == "2":
                    print(f"\n{Color.RED}Silahkan pilih opsi (1/2/press any key) :{Color.END}\n1. Delete (Hapus item)\n2. Reset (Hapus semua item)\n3. Cancel")
                    rmv = input("Silahkan pilih opsi anda : ").upper()
                    if len(Transaksi._order) == 0:
                        print("\nTidak ada item yang diorder\n")
                        break
                        # self.opsi()
                    elif rmv == "1":
                        print(Transaksi._order)
                        a = input("Silahkan ketikan item yang akan dihapus : ").upper()
                        print(self.delete_item(a))
                    elif rmv == "2":
                        if self.reset_transaction() == "1":
                            print(f"{Color.GREEN}Semua item sudah dihapus{Color.END}")
                            break
                        else:
                            continue
                    else:
                        print("\n")
                        continue
                elif pilih == "3":
                    break
                else:
                    print(f"{Color.RED}Anda salah memilih opsi {Color.END}")
    
    """
    delete_item function untuk menghapus per item, berdasarkan nama item yang diinputkan
    """
    def delete_item(self,nama_item):
        self.nama_item = nama_item
        pesan = input("Yakin mau hapus data (Yes=y, No=press any key) ?").upper()
        if pesan == "Y":
            for k,v in list(Transaksi._order.items()):
                if k == self.nama_item:
                    del Transaksi._order[k]
                    return f"\n{Color.YELLOW}Item sudah dihapus{Color.END}\n"
                else:
                    return(f"Item {self.nama_item} tidak ada atau sudah dihapus, silahkan diperiksa kembali")
        else:
            return "Silahkan Pilih : "

    """
    - reset_transaction function untuk menghapus semua item sekaligus.
    """
    def reset_transaction(self):
        rst = input("Anda yakin mau menghapus semua item yang sudah diinputkan (Yes=y, No=press any key)? ").upper()
        if rst == "Y":
            Transaksi._order.clear()
            return "1"
        else:
            return "2"
    
    """
    - untuk menampilkan table item
    - untuk menampilkan opsi (add/update item, check order, exit)
    """
    def menu(self):
        while True:
            self.table()
            print("1. Add/Update Item\n2. Check Order (Finish/Delete Item)\n3. Exit")
            pilih = input("Masukkan opsi (1/2/3) : ")
            print("\n")
            if pilih == "1":
                self.tambah()
            elif pilih == "2":
                self.check_order()
            elif pilih == "3":
                print("Terima kasih, telah mengunjungi AndyMart")
                break
            else:
                print("Anda salah memasukkan opsi, silahkan cek ulang")
        quit()
            