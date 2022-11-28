# Persyaratan untuk jalankan kodenya
* sudah terinstall python dan setup environmentnya *silakan cari di yt tutorialnya :'*
* sambungkan akun github ke vscode *di vscode, kiri bawah klik ikon user trs `sign in` trs pilih github*

# Persiapan
## Setup ngrok
Ngrok ini cuma ubah server lokal `127.0.0` jadi server publik, bisa dibilang pengganti domain, tpi kyknya nda auto run ki programnya, misal dihentikanmi eksekusi programnya nnti bakal nda berkerja botnya juga. Itumi butuh ki **domain + hosting**, domain itu urlnya, hosting itu tempat upload kode programnya supaya auto run programnya *CMIIW*.
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
* buka cmd, trus ketik `cd (paste path yg tadi)` enter. Contoh: `cd C:\Users\Dhea Gita\Desktop\`
* di repo github ini, klik tombol hijau `code`, trus copy urlnya
* kembali ke cmd tadi, trus ketik `git clone (paste url git yg tadi)` enter
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
* `coba.py` itu file untuk tes awal botnya, krna di kode baris 6-12 dan 14-15 hampirji sama di `main.py` kode baris 11-19 dan 61-62. *Kira-kira apa bedanya :"*

# Cara tes botnya bekerja ato tidak
## running coba.py
* buka terminal vscode nya, trus ketik `python coba.py`
* kalo outputnya adami `Running on http://127.0.0.1:5000/` brarti berjalanmi itu
* buka cmd, ketik `ngrok http 5000`, trus copy link di forwading misal `https://c212-103-105-32-12.ap.ngrok.io`
* WARNING: link yg di ngrok bisa saja berubah pas dijalankan ulang ngroknya
* buka twilio, ke navigasi sebelah kiri > Develop > Settings > WhatsApp sandbox settings
* ganti url di box WHEN A MESSAGE COMES IN jadi `link ngrok tadi/wasms`. Contoh: `https://c212-103-105-32-12.ap.ngrok.io/wasms`
* wasms itu routenya spya terhubung ke bot wa *routenya bisa diliat di file coba.py baris 6*
* klik `save`
* di wa, chat bot yg kushare trus kirim`stop`
* trus kirim kode joinnya *bisa dilliat di twilio, Sandbox Participants yg **join...** *
* coba chat botnya lagi, klo direspon `helow` brarti berjalanmi kode yg file coba.py
## running main.py
* *samaji caranya di atas*, di terminal, tekan `ctrl+c` untuk hentikan program `python coba.py` yg tadi
* trus ketik `python main.py`, outputnya adami `Running on http://127.0.0.1:5000/`
* coba chat botnya sesuai tag/patterns di folder `data/intents.json`
