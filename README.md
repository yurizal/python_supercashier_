# SuperCashier - Self Service

Python Super Cashier adalah program sederhana self service yang menggunakan python agar pelanggan bisa memesan barang atau item secara mandiri.

## Description App
- Terdapat table untuk menampilkan item-item apa saja yang bisa dipesan
- Pelanggan bisa menambahkan item dan juga jumlah per item
- Jumlah Item dapat diupdate
- Pelanggan bisa menghapus per item atau hapus sekaligus
- Pelanggan yang telah memesan atau akan membayar diatas ketentuan akan mendapatkan diskon
 
## FlowChart
![Flowchart-Tugas_Pacmaan_Python-revisi drawio](https://user-images.githubusercontent.com/16360023/215666494-06a2ca76-c354-4ec2-a3b3-2285aa3555b8.png)

## Function Code
 | Function | Deskripsi |
 | -------- | --------- |
 | ```def __init__``` | Pertama kali program dijalankan dan penginputan nama |
 | ```def table(self)``` | Untuk menampilkan data atau item yang sudah ada |
 | ```def table_order(self)``` | Untuk menampilkan data atau item yang telah diinputkan oleh pelanggan dan dilakukan penghitungan  |
 | ```def menu(self)``` | Menu awal untuk show table item dan pilihan yang terdiri dari add/update item, checkorder dan exit |
 | ```def add_item(self,tambah_item)``` | Input Item dan kembali ke menu |
 | ```def update_item_qty(self,nama_item)``` | Input atau update jumlah item dan kembali ke menu  |
 | ```def delete_item(self,nama_item)``` | Pilih nama item untuk dihapus |
 | ```def reset_transaction(self)``` | Hapus semua item yang telah diinputkan |
 | ```def check_order(self)``` | Untuk menampilkan data yang telah dilakukan penghitungan. Dan opsi untuk delete item |

## Running Program
- Buat folder dan environment terlebih dahulu
    ```
    mkdir <folder>
    cd <folder>
    copy program ke dalam folder
    python3 -m venv env
    ```
- Aktifkan environment
    ```
    source ./env/bin/activate
    ```
- Install terlebih dahulu package yang diperlukan pada requirement.txt
    ```
    pip install -r requirement.txt
    ```
    > Package yang digunakan 
    
    | Package | README |
    | ------- | ------ |
    | itertools | https://docs.python.org/3/library/itertools.html#itertools.chain |
    | rich | https://rich.readthedocs.io/en/stable/tables.html |
    | collection | https://docs.python.org/3/library/collections.html#collections.defaultdict |
    
- Jalankan app di terminal 
    ```
    python app.py
    ```
## Test Case
- _Menjalankan program dan input nama_

![Screenshot from 2023-01-31 15-39-47](https://user-images.githubusercontent.com/16360023/215710475-e65c037c-5586-43e1-b9f7-eb64be401578.png)

- _Pilih Item (Table Item)_

![Screenshot from 2023-01-31 15-41-04](https://user-images.githubusercontent.com/16360023/215710688-3fb86417-b4eb-44ab-8bf1-dc21c06bee91.png)

- _Add/Update item_

![Screenshot from 2023-01-31 15-43-49](https://user-images.githubusercontent.com/16360023/215711292-8a5e354d-ebe3-437c-854e-0e340cd9a550.png)

- _Jika salah memasukkan nama item_

![Screenshot from 2023-01-31 15-46-00](https://user-images.githubusercontent.com/16360023/215711772-23b1e0e3-5f6f-4bd1-b1fa-31e13ab5837e.png)

- _Pilih Check Order_

![Screenshot from 2023-01-31 15-48-13](https://user-images.githubusercontent.com/16360023/215712220-9af75344-f67e-4746-a384-5f1d5b72b828.png)

- _Menghapus item_

![Screenshot from 2023-01-31 15-51-52](https://user-images.githubusercontent.com/16360023/215712981-57008eef-a846-4da5-990e-ce229404beea.png)

- _Check Out pemesanan_

![Screenshot from 2023-01-31 15-52-29](https://user-images.githubusercontent.com/16360023/215713366-65cbf0aa-5f7c-4909-b5ef-84158c196c69.png)


## Perbaikan kedepan
- ```Perbaikan clean code```
- ```Implementasi metode MVC```
