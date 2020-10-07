# read-csv-file-and-input-to-dictionary
Sebelum memulai, download dulu atau siapkan fiel .csv yang akan kita eksekusi
Di sini saya menggunakan dataset dari atapdata.ai

<img width="907" alt="1" src="https://user-images.githubusercontent.com/49053021/95326998-a127f380-08cd-11eb-824c-e6587bbf2dda.PNG">

Berikut linknya : https://atapdata.ai/dataset/242

## Membaca file
<img src="https://user-images.githubusercontent.com/49053021/95327143-cc124780-08cd-11eb-8e87-35991d7ab541.png">

singkatan.csv ada file csv yang sudah saya downlod dan akan di baca dengan menggunakan perintah readlines()
Jika ingin melihat isi dari file tersebut maka tinggal print saja

<img src="https://user-images.githubusercontent.com/49053021/95327643-915cdf00-08ce-11eb-9a85-7d3ceb6bf2f2.png">

## Membuat Dictionary
Untuk memasukkan data kedalam dictionari terlebih dahulu buat dictionarinya, misalnya kita namakan hash
di paling atas code buat dictionary kosong

<img src="https://user-images.githubusercontent.com/49053021/95327905-f4e70c80-08ce-11eb-8e19-d57a641e6203.png">

Dalam hash ada namanya key dan value, dapat kita lihat bahwa data kita di bisahkan dengan tanda ','
saya akan menjadikan singkatan sebagai key, dan artinya sebagai value, kita pisahkan dengan perintah split()
kita coba dengan 1 baris dulu


