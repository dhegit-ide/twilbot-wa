# Referensi kode
* https://www.pragnakalp.com/create-whatsapp-bot-with-twilio-using-python-tutorial-with-examples/
* https://youtu.be/sotu6YqPoY0
* https://youtu.be/hW3zfd0mIfw

# Requirements
* python
* ngrok
* akun twilio

# Setup ngrok
Ngrok ini cuma ubah server lokal `127.0.0` jadi server publik, bisa dibilang pengganti domain, tapi mungkin programnya tidak auto run, misal dihentikan eksekusi programnya nanti botnya juga bakal tidak berkerja. Jadi, mungkin butuh **domain + hosting**, domain itu urlnya, hosting itu tempat upload kode programnya supaya auto run programnya *CMIIW*.
* download ngrok di `https://ngrok.com/download`, trs unzip, trs simpan foldernya di `C:\`
* buka folder ngrok, kalo isinya cuma `ngrok.exe` *brarti cocokmi itu*
* copy path foldernya. Contoh: `C:\ngrok-v3-stable-windows-amd64`
* pergi ke search yg di taskbar ato tekan `win+s`
* cari `edit variabel lingkungan sistem` ato binggrisnya itu
* enviromenmet variables > pilih path yg di system variables > edit > new > copas path ngrok yg tadi> ok > ok > ok

# Setup twilio
* buat akun twilio di `twilio.com`
* *ikuti saja alur pendaftarannya*, trus harus verifikasi pake no.telp dulu, baru bisa terdaftar

# Struktur folder
* kalo adami folder `twilbot-wa`, buka foldernya di vscode
* isinya itu `data`, `util`, `main.py`, `requirements.txt`
* folder `data` itu tempat skrip dialognya
* folder `util` itu program supaya bisa digunakan `data/intents.json` di `main.py`
* `main.py` itu file utama untuk buat fitur"nya
* `requirements.txt` itu daftar modul/library yang harus diinstall

# Cara tes botnya bekerja atau tidak
## running main.py
* install library nya, buka terminal vscode, trus ketik `pip install -r requirements.txt`
* trus ketik `python main.py`, nanti outputnya `Running on http://127.0.0.1:5000/` artinya program sudah berjalan
* buka cmd, ketik `ngrok http 5000`, trus copy link di forwading misal `https://c212-103-105-32-12.ap.ngrok.io`
* WARNING: link yg di ngrok bisa saja berubah pas dijalankan ulang ngroknya
* buka link url nya, nanti akan diarahkan ke whatsapp
* buka twilio, ke navigasi sebelah kiri > Develop > Settings > WhatsApp sandbox settings
* ganti url di box WHEN A MESSAGE COMES IN jadi `link ngrok tadi/wasms`. Contoh: `https://c212-103-105-32-12.ap.ngrok.io/wasms`
