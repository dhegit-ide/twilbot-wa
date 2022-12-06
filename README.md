# Referensi kode
* https://www.pragnakalp.com/create-whatsapp-bot-with-twilio-using-python-tutorial-with-examples/
* https://youtu.be/sotu6YqPoY0
* https://youtu.be/hW3zfd0mIfw


# Persyaratan untuk jalankan kodenya
* sudah terinstall python dan setup environmentnya
* sambungkan akun github ke vscode *di vscode, kiri bawah klik ikon user trs `sign in` trs pilih github*

# Persiapan
## Setup ngrok
Ngrok ini cuma ubah server lokal `127.0.0` jadi server publik, bisa dibilang pengganti domain, tapi mungkin programnya tidak auto run, misal dihentikan eksekusi programnya nanti botnya juga bakal tidak berkerja. Itumi butuh ki **domain + hosting**, domain itu urlnya, hosting itu tempat upload kode programnya supaya auto run programnya *CMIIW*.
* download ngrok di `https://ngrok.com/download`, trs unzip, trs simpan foldernya di `C:\`
* buka folder ngrok, kalo isinya cuma `ngrok.exe` *brarti cocokmi itu*
* copy path foldernya. Contoh: `C:\ngrok-v3-stable-windows-amd64`
* pergi ke search yg di taskbar ato tekan `win+s`
* cari `edit variabel lingkungan sistem` ato binggrisnya itu
* enviromenmet variables > pilih path yg di system variables > edit > new > copas path ngrok yg tadi> ok > ok > ok
## Setup twilio
* buat akun twilio di `twilio.com`
* *ikuti saja alur pendaftarannya*, trus harus verifikasi pake no.telp dulu, baru bisa terdaftar
* kalo sudah login, *baca-bacami dulu panduannya :"*

# Cara download kodenya
* buka file explorer, pergi ke folder yang mau ditempati untuk dowload kodenya, trus copy pathnya (misal: `C:\Users\Dhea Gita\Desktop\`)
* buka cmd, trus ketik `cd (paste path yg tadi)` *enter*. Contoh: `cd C:\Users\Dhea Gita\Desktop\`
* di repo github ini, klik tombol hijau `code`, trus copy urlnya
* kembali ke cmd tadi, trus ketik `git clone (paste url git yg tadi)` *enter*
* wait *a few moments later...*
* ...
* sudah?
* coba liat di file explorer ke lokasi download foldernya
## Struktur folder
* kalo adami folder `twilbot-wa`, buka foldernya di vscode
* isinya itu `data`, `util`, `main.py`, `coba.py`
* folder `data` itu tempat skrip dialognya
* folder `util` itu program supaya bisa digunakan `data/intents.json` di `main.py`
* `main.py` itu file utama untuk buat fitur"nya

# Cara tes botnya bekerja ato tidak
## running main.py
* install library nya, buka terminal vscode, trus ketik `pip install -r requirements.txt`
* trus ketik `python main.py`, nanti outputnya `Running on http://127.0.0.1:5000/` artinya program sudah berjalan
* buka cmd, ketik `ngrok http 5000`, trus copy link di forwading misal `https://c212-103-105-32-12.ap.ngrok.io`
* WARNING: link yg di ngrok bisa saja berubah pas dijalankan ulang ngroknya
* buka link url nya, nanti akan diarahkan ke whatsapp
* buka twilio, ke navigasi sebelah kiri > Develop > Settings > WhatsApp sandbox settings
* ganti url di box WHEN A MESSAGE COMES IN jadi `link ngrok tadi/wasms`. Contoh: `https://c212-103-105-32-12.ap.ngrok.io/wasms`
