import asyncio
import random
from telethon import TelegramClient, events, errors
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsRecent
import uuid
from datetime import datetime
from telethon import events
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetShortName
import asyncio
import aiohttp
from urllib.parse import quote
from urllib.parse import quote_plus
from telethon import events
import requests
import json
import chardet
import time
import tempfile
import os

api_id = 22413019
api_hash = '7d5bc33c12e733198347f1d86eb88f03'

OWNER_ID = 6673505038  # Ganti dengan ID Telegram kamu

client = TelegramClient('userbot', api_id, api_hash)

online = True
self_mode = True

kata_kata_list = [
    "```Jangan menyerah, hari ini berat tapi besok kamu lebih kuat.```",
    "```Fokus pada tujuan, bukan hambatan```.",
    "```Waktu tidak bisa diputar, jadi manfaatkan sekarang```.",
    "```Kesalahan bukan akhir, tapi awal pembelajaran.```",
    "```Kalau kamu yakin, jalanmu pasti terbuka.```"
]

def safe_run(coro):
    async def wrapper(event):
        try:
            await coro(event)
        except Exception as e:
            await event.reply(f"[!] Error: {str(e)}")
    return wrapper

premium_users = set()

PREMIUM_FILE = "premium.txt"

def load_premium():
    if os.path.exists(PREMIUM_FILE):
        with open(PREMIUM_FILE, "r") as f:
            return set(map(int, f.read().split()))
    return set()

def save_premium(premium_ids):
    with open(PREMIUM_FILE, "w") as f:
        f.write(" ".join(map(str, premium_ids)))

premium_users = load_premium()

async def is_admin(chat, user):
    try:
        participant = await client(GetParticipantRequest(chat, user))
        return isinstance(participant.participant, (ChannelParticipantCreator, ChannelParticipantAdmin))
    except:
        return False

def check_access(user_id):
    # Ganti ID kamu jika ingin membatasi akses
    return True

def safe_run(func):
    async def wrapper(event):
        try:
            await func(event)
        except Exception as e:
            await event.respond(f"❌ Terjadi error: {e}")
    return wrapper

# ----------------------------------------
# Helper function untuk cek hak akses
def check_access(sender_id):
    if self_mode:
        return sender_id == OWNER_ID or sender_id in premium_users
    else:
        return True
# ----------------------------------------

@client.on(events.NewMessage(pattern=r'^\!babukeluar$'))
@safe_run
async def botmii_menu(event):
    mode = "SELF - HANYA OWNER" if self_mode else "PUBLIK"
    if not self_mode or event.sender_id == OWNER_ID:
        menu_caption = (
            "╔═━─━★⟟ 𝑴𝑰𝑰𝑩𝑶𝑻𝒁𝒁 𝑿 𝑼𝑩𝑶𝑻 ⟟★━─━═╗\n\n"
        " • ⟬ 友 /cekid ⟭   \n"
        " • ⟬ 友 /autotag ⟭   \n"
        " • ⟬ 友 /katakata ⟭   \n"
        " • ⟬ 友 /off ⟭   \n"
        " • ⟬ 友 /on ⟭  \n"
        " • ⟬ 友 /self ⟭   \n"
        " • ⟬ 友 /public ⟭   \n"
        " • ⟬ 友 /koinflip⟭   \n"
        " • ⟬ 友 /kawin ⟭   \n"
        " • ⟬ 友 /predikgb ⟭   \n"
        " • ⟬ 友 /predikinfinix ⟭   \n"
        " • ⟬ 友 /spamngl ⟭   \n"
        " • ⟬ 友 /trackipmii ⟭   \n"
        " • ⟬ 友 /cekweb ⟭   \n"
        " • ⟬ 友 /miixtt ⟭   \n"
        " • ⟬ 友 /ai ⟭   \n"
        " • ⟬ 友 /ektp ⟭   \n"
        " • ⟬ 友 /miixtweet ⟭   \n"
        " • ⟬ 友 /sertifikat ⟭   \n"
        " • ⟬ 友 /cfd ⟭  \n"
        " • ⟬ 友 /blank_stc ⟭  \n"
        " • ⟬ 友 /cekidgb ⟭   \n"
        "• ⟬ 友 /brat⟭  \n"
        " ```MIIBOTZZ X UBOT``` \n\n"
        "╚═━ 𝑷𝑶𝑾𝑬𝑹𝑬𝑫 𝑩𝒀 𝑴𝑰𝑰 ━═╝"
        )
    else:
        menu_caption = (
        "╔═━────━★𝑼𝑺𝑬𝑹𝑩𝑶𝑻★━────━═╗\n\n"
        " • LU SIAPA ANJ BUKAN USER PREM/OWN"
        f"╚═━ 𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 𝙼𝙸𝙸 ★ 𝙼𝙾𝙳𝙴: {mode} ━═╝"
        )

    await client.send_file(
        event.chat_id,
        file="https://l.top4top.io/m_34596y8ak1.mp4",
        caption=menu_caption
    )

    await client.send_file(
        event.chat_id,
        file="https://h.top4top.io/m_3436lwa1n1.mp3"
    )

@client.on(events.NewMessage(pattern=r'^/self$'))
@safe_run
async def set_self(event):
    if not check_access(event.sender_id):
        return
    global self_mode
    self_mode = True
    await event.reply("[🔒] Mode SELF diaktifkan. Hanya kamu yang bisa gunakan bot ini.")

@client.on(events.NewMessage(pattern=r'^/public$'))
@safe_run
async def set_public(event):
    if not check_access(event.sender_id):
        return
    global self_mode
    self_mode = False
    await event.reply("[🔓] Mode PUBLIK diaktifkan. Orang lain bisa gunakan fitur terbatas.")

@client.on(events.NewMessage(pattern=r'^/cekid(?:\s+(@\w+))?$'))
@safe_run
async def cekid_handler(event):
    if not check_access(event.sender_id):
        return
    args = event.pattern_match.group(1)
    if args:
        username = args.lstrip('@')
        try:
            user = await client.get_entity(username)
            user_mention = f"@{user.username}" if user.username else user.first_name
            text = (
                "\n┏━━━★ BOT MII USERBOT ★━━━┓\n\n"
                f"USER: {user_mention}\n"
                f"ID  : {user.id}\n\n"
                "🙏 THANK BRO 🎉\n"
                "┗━━★ Powered by Mii ★━━┛"
            )
            await event.reply(text)
        except Exception:
            await event.reply(f"[!] User {args} tidak ditemukan.")
    else:
        if event.message.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user = await client.get_entity(reply_msg.from_id)
            username = f"@{user.username}" if user.username else user.first_name
            text = (
                "\n┏━━━★ BOT MII USERBOT ★━━━┓\n\n"
                f"USER: {username}\n"
                f"ID  : {user.id}\n\n"
                "🙏 THANK BRO 🎉\n"
                "┗━━★ Powered by Mii ★━━┛"
            )
            await event.reply(text)
        else:
            await event.reply("[!] Gunakan dengan reply pesan atau masukkan @username.")

@client.on(events.NewMessage(pattern=r'^/autotag$'))
@safe_run
async def autotag_handler(event):
    if not check_access(event.sender_id):
        return
    if event.is_group or event.is_channel:
        participants = await client(GetParticipantsRequest(
            channel=event.chat_id,
            filter=ChannelParticipantsRecent(),
            offset=0,
            limit=200,
            hash=0
        ))
        mentions = '[MiiBOTZZ TAG AKTIF]\n\n'
        for user in participants.users:
            if user.username:
                mentions += f'@{user.username} '
            else:
                mentions += f'[{user.first_name}](tg://user?id={user.id}) '
        await event.reply(mentions)

@client.on(events.NewMessage(pattern=r'^/katakata$'))
@safe_run
async def katakata_handler(event):
    if not check_access(event.sender_id):
        return
    kata = random.choice(kata_kata_list)
    await event.reply(f"📢 KATA-KATA HARI INI:\n\n“{kata}”")

@client.on(events.NewMessage(pattern=r'^/off$'))
@safe_run
async def off_handler(event):
    if not check_access(event.sender_id):
        return
    global online
    online = False
    await event.reply("[⚠] MODE OFFLINE DIAKTIFKAN.")

@client.on(events.NewMessage(pattern=r'^/on$'))
@safe_run
async def on_handler(event):
    if not check_access(event.sender_id):
        return
    global online
    online = True
    await event.reply("[✅] MODE ONLINE AKTIF. Auto reply dinonaktifkan.")

@client.on(events.NewMessage)
@safe_run
async def auto_reply_off(event):
    global online
    if not online and event.is_private:
        await event.reply("```[⚠] KETUA LAGI OFF GAUSAH GANGGU```")

@client.on(events.NewMessage(pattern=r'^\.koinflip\s+(.+)$'))
@safe_run
async def koinflip_handler(event):
    if not check_access(event.sender_id):
        return

    input_text = event.pattern_match.group(1).strip()
    pemain = input_text.split('.')

    random.seed(uuid.uuid4().int)

    hasil_koin = random.choice(["depan", "belakang"])
    pemenang = []

    await event.reply("🎞️ Lempar koin dimulai...")
    await client.send_file(event.chat_id, "merci-gimmiko.mp4", caption="🪙 Koin dilambungkan...")

    await asyncio.sleep(2.5)

    response = f"🎯 **Hasil: {hasil_koin.upper()}**\n\n"

    for data in pemain:
        try:
            nama, tebakan = data.split(',')
            nama = nama.strip()
            tebakan = tebakan.strip().lower()
            if tebakan == hasil_koin:
                pemenang.append(nama)
        except ValueError:
            continue

    if pemenang:
        winner_text = '\n'.join([f"🏆 **{p}** menang! 🎉" for p in pemenang])
        response += winner_text
    else:
        response += "😅 Tidak ada yang menebak dengan benar."

    await event.reply(response, parse_mode='markdown')

@client.on(events.NewMessage(pattern=r'^\/kawin\s+(.+)$'))
@safe_run
async def kawin_handler(event):
    if not check_access(event.sender_id):
        return
    nama = event.pattern_match.group(1).strip()
    tahun_nikah = random.randint(2025, 2040)
    respon = (
        f"💍 *Prediksi Nikah:*\n"
        f"`{nama}` akan menikah di tahun *{tahun_nikah}* 💘\n"
        "Siapin undangannya dari sekarang ya! 🎉"
    )
    await event.reply(respon, parse_mode='markdown')

@client.on(events.NewMessage(pattern=r'^\/predikgb$'))
@safe_run
async def rolg_handler(event):
    if not check_access(event.sender_id):
        return

    now = datetime.now()
    menit = now.minute

    if 0 <= menit <= 6:
        prediksi = "K"
    elif 7 <= menit <= 16:
        prediksi = "B"
    elif 17 <= menit <= 25:
        prediksi = "K"
    elif 26 <= menit <= 36:
        prediksi = "B"
    elif 37 <= menit <= 45:
        prediksi = "K"
    elif 46 <= menit <= 56:
        prediksi = "B"
    else:
        prediksi = "K"

    text = (
        "┏━━━★ PREDIKSI GB ★━━━┓\n\n"
        f"vip  BY MIIBOTZZ\n"
        f"🎯 PREDIKSI BESAR/KECIL: {prediksi}\n\n"
        "┗━━★ Powered by Mii ★━━┛"
    )

    await event.reply(text)

@client.on(events.NewMessage(pattern=r'^/predikinfinix$'))
@safe_run
async def predikinfinix_handler(event):
    if not check_access(event.sender_id):
        return

    now = datetime.now()
    menit = now.minute

    # Perbaiki range menit supaya lengkap 0-59
    if 0 <= menit <= 6:
        prediksi = "B"
    elif 7 <= menit <= 16:
        prediksi = "K"
    elif 17 <= menit <= 25:
        prediksi = "B"
    elif 26 <= menit <= 36:
        prediksi = "K"
    elif 37 <= menit <= 45:
        prediksi = "B"
    elif 46 <= menit <= 58:  # 46 sampai 58 (sebelum 59)
        prediksi = "K"
    else:  # menit 59
        prediksi = "B"  # default

    teks = (
        "╔══════════════════════╗\n"
        "║    🔁 BOT BY MIIBOTZZ 🔁    ║\n"
        "╚══════════════════════╝\n\n"
        "✨ GINI PREDIK INFINIX ✨\n\n"
        f"👉 𝗠𝗔𝗦𝗨𝗞 𝗪𝗜𝗡 : {prediksi} 👈\n\n"
        "⚠️ 𝗜𝗡𝗚𝗔𝗧 𝗕𝗢𝗧 𝗜𝗡𝗜 𝗛𝗔𝗡𝗬𝗔 𝗙𝗜𝗫 𝟴𝟬% ⚠️"
    )

    await event.reply(teks)
    
@client.on(events.NewMessage(pattern=r'^/listprem$'))
@safe_run
async def list_prem_handler(event):
    if event.sender_id != OWNER_ID:
        return
    if not premium_users:
        await event.reply("Belum ada user premium.")
        return
    users_str = "\n".join([str(uid) for uid in premium_users])
    await event.reply(f"Daftar User Premium:\n{users_str}")

@client.on(events.NewMessage(pattern=r'^/addprem\s+(\d+)$'))
@safe_run
async def add_premium(event):
    if event.sender_id != OWNER_ID:
        return
    user_id = int(event.pattern_match.group(1))
    premium_users.add(user_id)
    save_premium(premium_users)
    await event.reply(f"User {user_id} sudah ditambahkan ke premium.")

@client.on(events.NewMessage(pattern=r'^/delprem\s+(\d+)$'))
@safe_run
async def del_premium(event):
    if event.sender_id != OWNER_ID:
        return
    user_id = int(event.pattern_match.group(1))
    if user_id in premium_users:
        premium_users.remove(user_id)
        save_premium(premium_users)
        await event.reply(f"User {user_id} sudah dihapus dari premium.")
    else:
        await event.reply(f"User {user_id} tidak ditemukan di premium.")

async def send_message(session, username, message, index):
    unique_message = quote(f"{message} | MiiBOTZZ KE{index}")
    url = f"https://api.siputzx.my.id/api/tools/ngl?link=https://ngl.link/{username}&text={unique_message}"
    try:
        async with session.get(url, timeout=10) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"[!] Error kirim ke-{index}: {e}")
        return False

# --- Fungsi Spam Berulang ---
async def spam_messages(username, message, count, event):
    success_count = 0
    fail_count = 0
    await event.reply(f"🚀 Mulai spam ke `https://ngl.link/{username}` sebanyak {count} pesan...")
    async with aiohttp.ClientSession() as session:
        for i in range(1, count + 1):
            try:
                await event.respond(f"⌛ Mengirim ke-{i}...")
                success = await send_message(session, username, message, i)
                if success:
                    await event.respond(f"[✓] Ke-{i} berhasil.")
                    success_count += 1
                else:
                    await event.respond(f"[✗] Ke-{i} gagal.")
                    fail_count += 1
                await asyncio.sleep(25)
            except Exception as e:
                await event.respond(f"[ERROR] Gagal ke-{i}: {e}")
                fail_count += 1
    await event.respond(f"""
📊 *Hasil Spam NGL:*
✅ Berhasil: {success_count}
❌ Gagal: {fail_count}
Link: https://ngl.link/{username}
    """, parse_mode="markdown")

# --- Handler Command /spamngl ---
@client.on(events.NewMessage(pattern=r'^/spamngl\s+(.+)$'))
@safe_run
async def spamngl_handler(event):
    if not check_access(event.sender_id):
        return
    try:
        args = event.pattern_match.group(1).split(',')
        if len(args) != 3:
            await event.reply("Format salah!\nGunakan: `/spamngl user,isi pesan,jumlah`\nContoh: `/spamngl miibotzz,hallo dari Mii,5`", parse_mode="markdown")
            return
        username = args[0].strip()
        message = args[1].strip()
        count = int(args[2].strip())
        await spam_messages(username, message, count, event)
    except Exception as e:
        await event.reply(f"[!] Gagal memproses perintah: {e}")

@client.on(events.NewMessage(pattern=r'^/trackipmii\s+(.+)$'))
@safe_run
async def trackipmii_handler(event):
    if not check_access(event.sender_id):
        return
    ip = event.pattern_match.group(1).strip()
    url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,zip,lat,lon,isp,org,as,query"
    
    banner = (
        "╭━━━━━━━━━━━━━━━━━━━╮\n"
        "┃   🔍 TRACKING IP BY MIIBOTZZ 🔍\n"
        "╰━━━━━━━━━━━━━━━━━━━╯\n"
        "📡 Sedang melacak IP kamu...\n"
        f"🧠 Target: `{ip}`\n"
        "⌛ Mohon tunggu sebentar..."
    )
    await event.reply(banner)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                data = await resp.json()

                if data['status'] != 'success':
                    await event.reply(f"❌ Gagal melacak IP: {data.get('message', 'Unknown error')}")
                    return

                hasil = (
                    "╭━━━[ 🌍 HASIL TRACKING IP ]━━━╮\n"
                    f"┃ 🌐 IP        : `{data['query']}`\n"
                    f"┃ 🗺️ Benua     : {data['continent']}\n"
                    f"┃ 🏳️ Negara    : {data['country']}\n"
                    f"┃ 🏙️ Provinsi  : {data['regionName']}\n"
                    f"┃ 🏡 Kota      : {data['city']}\n"
                    f"┃ 🔢 Kode Pos  : {data['zip']}\n"
                    f"┃ 📶 ISP       : {data['isp']}\n"
                    f"┃ 🧾 Org       : {data['org']}\n"
                    f"┃ 🛰️ AS        : {data['as']}\n"
                    f"┃ 📍 Lokasi    : {data['lat']}, {data['lon']}\n"
                    "╰━━━━━━━━━━━━━━━━━━━━━━╯\n"
                    "👣 Diburu oleh: **MiiBOTZZ** ⚡\n"
                    "🔗 Powered By Miibotzz"
                )
                await event.reply(hasil)
    except Exception as e:
        await event.reply(f"❌ Terjadi kesalahan saat tracking: `{str(e)}`")

@client.on(events.NewMessage(pattern=r'^/cekweb (.+)'))
@safe_run
async def cek_web(event):
    url = event.pattern_match.group(1)

    await event.reply("🔍 Mengecek website...")

    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()
        speed = int((end - start) * 1000)
        status_code = response.status_code

        if status_code == 200:
            status = f"✅ ONLINE ({status_code} OK)"
        else:
            status = f"⚠️ ERROR ({status_code})"

    except requests.exceptions.RequestException:
        status = "❌ OFFLINE / Gagal Terhubung"
        speed = "-"

    result = f"""\
┏━━━★ CEK WEB BY MII ★━━━┓

LINK        : {url}
STATUS      : {status}
KECEPATAN   : {speed}ms

┗━━★ Powered by Mii ★━━┛"""

    await event.reply(result)

@client.on(events.NewMessage(pattern=r'^/miixtt\s+(https?://[^\s]+)'))
@safe_run
async def tiktok_handler(event):
    if not check_access(event.sender_id):
        return

    url = event.pattern_match.group(1).strip()
    encoded_url = quote_plus(url)
    api_url = f"https://api.siputzx.my.id/api/tiktok/v2?url={encoded_url}"

    await event.reply("🔄 Memproses video TikTok...")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as resp:
                if resp.status != 200:
                    await event.reply(f"❌ API gagal dijangkau. Status: {resp.status}")
                    return
                data = await resp.json()

        if data.get("success") and data.get("data") and data["data"].get("download"):
            video_links = data["data"]["download"]["video"]
            video_url = video_links[0] if video_links else None

            if video_url:
                # Unduh video ke file temporer
                async with aiohttp.ClientSession() as session:
                    async with session.get(video_url) as video_resp:
                        if video_resp.status != 200:
                            await event.reply(f"❌ Gagal mengunduh video. Status: {video_resp.status}")
                            return
                        video_bytes = await video_resp.read()

                # Simpan ke file sementara
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
                    tmp_file.write(video_bytes)
                    tmp_path = tmp_file.name

                # Kirim file lokal
                await client.send_file(event.chat_id, tmp_path, caption="✅ Video TikTok berhasil diunduh.")

                # Hapus file setelah kirim
                os.remove(tmp_path)

            else:
                await event.reply("❌ Video tidak ditemukan di data API.")
        else:
            await event.reply("❌ API tidak memberikan data video yang valid.")

    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")

@client.on(events.NewMessage(pattern=r'^/ai\s+(.+)'))
@safe_run
async def ai_handler(event):
    if not check_access(event.sender_id):
        await event.reply("🚫 Kamu tidak diizinkan menggunakan perintah ini.")
        return

    user_input = event.pattern_match.group(1).strip()
    encoded_input = quote_plus(user_input)
    api_url = f"https://api.siputzx.my.id/api/ai/metaai?query={encoded_input}"

    await event.reply("🤖 Meta AI sedang memproses...")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; TelegramBot/1.0)",
            "Accept": "application/json"
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(api_url) as resp:
                if resp.status == 429:
                    return await event.reply("⚠️ Terlalu banyak permintaan. Coba lagi sebentar.")
                elif resp.status != 200:
                    return await event.reply(f"❌ Gagal akses API. Status: {resp.status}")

                raw = await resp.read()
                text = raw.decode('utf-8', errors='ignore')
                data = json.loads(text)

        if data.get("status") is True and data.get("data"):
            result_text = data["data"]
        else:
            result_text = "❌ Meta AI tidak merespons."

        await event.reply(f"🤖 META AI:\n\n{result_text}")

    except Exception as e:
        await event.reply(f"❌ Terjadi error: {str(e)}")

@client.on(events.NewMessage(pattern=r'^/ektp\s+(.+)'))
@safe_run
async def ektp_handler(event):
    if not check_access(event.sender_id):
        return

    try:
        input_text = event.pattern_match.group(1)
        parts = input_text.split('|')
        if len(parts) != 18:
            await event.reply(
                "❌ Format salah!\n\nContoh:\n"
                "`/ektp Nama|NIK|TTL|Jenis Kelamin|Gol. Darah|Alamat|RT/RW|Kel/Desa|Kecamatan|Agama|Status|Pekerjaan|WNI/WNA|Provinsi|Kota|Berlaku|Terbit|Foto`"
            )
            return

        (
            nama, nik, ttl, jenis_kelamin, gol_darah, alamat,
            rt_rw, kel_desa, kecamatan, agama, status,
            pekerjaan, kewarganegaraan, provinsi, kota,
            masa_berlaku, terbuat, pas_photo
        ) = map(lambda x: quote_plus(x.strip()), parts)

        api_url = (
            f"https://api.siputzx.my.id/api/m/ektp?"
            f"provinsi={provinsi}&kota={kota}&nik={nik}&nama={nama}&ttl={ttl}"
            f"&jenis_kelamin={jenis_kelamin}&golongan_darah={gol_darah}&alamat={alamat}"
            f"&rt%2Frw={rt_rw}&kel%2Fdesa={kel_desa}&kecamatan={kecamatan}"
            f"&agama={agama}&status={status}&pekerjaan={pekerjaan}&kewarganegaraan={kewarganegaraan}"
            f"&masa_berlaku={masa_berlaku}&terbuat={terbuat}&pas_photo={pas_photo}"
        )

        await event.reply("🪪 Membuat e-KTP...")

        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as resp:
                if resp.status != 200:
                    await event.reply(f"❌ Gagal akses API. Status: {resp.status}")
                    return

                image_data = await resp.read()

        # Simpan ke file lokal
        path = "foto/mii.png"
        with open(path, "wb") as f:
            f.write(image_data)

        # Kirim file dari lokal
        await client.send_file(
            event.chat_id,
            file=path,
            caption="bymii"
        )

    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")

@client.on(events.NewMessage(pattern=r'^/miixtweet\s+(.+)'))
@safe_run
async def tweet_handler(event):
    if not check_access(event.sender_id):
        return

    try:
        # Split input by '|'
        parts = event.pattern_match.group(1).split('|')
        if len(parts) != 11:
            await event.reply(
                "❌ Format salah!\n\nContoh:\n"
                "/miixtweet profile_url|name|username|tweet_text|image|null|theme|retweets|quotes|likes|client"
            )
            return

        (
            profile, name, username, tweet, image, null_param,
            theme, retweets, quotes, likes, client_param
        ) = map(lambda x: quote_plus(x.strip()), parts)

        api_url = (
            f"https://api.siputzx.my.id/api/m/tweet?"
            f"profile={profile}&name={name}&username={username}&tweet={tweet}"
            f"&image={image}&theme={theme}&retweets={retweets}&quotes={quotes}&likes={likes}"
            f"&client={client_param}"
        )

        await event.reply("🐦 miixtweet...")

        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as resp:
                if resp.status != 200:
                    await event.reply(f"❌ Gagal akses API. Status: {resp.status}")
                    return
                image_data = await resp.read()

        # Simpan sementara file
        path = "foto/tweet.png"
        with open(path, "wb") as f:
            f.write(image_data)

        await client.send_file(event.chat_id, path, caption="✅ Tweet berhasil dibuat!")

    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")

@client.on(events.NewMessage(pattern=r'^/sertifikat\s+(.+)'))
@safe_run
async def sertifikat_handler(event):
    if not check_access(event.sender_id):
        return await event.reply(" TA BOLEH ASU")

    user_input = event.pattern_match.group(1).strip()
    encoded_text = quote_plus(user_input)
    api_url = f"https://api.siputzx.my.id/api/m/sertifikat-tolol?text={encoded_text}"

    await event.reply("🖼️ Mii lagi bikin sertifikat tolol...")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; TelegramBot/1.0)",
            "Accept": "image/jpeg"
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(api_url) as resp:
                if resp.status != 200:
                    await event.reply(f"❌ Gagal akses API. Status: {resp.status}")
                    return
                image_data = await resp.read()

        # Simpan sebagai PNG (walaupun original-nya JPEG, tetap bisa dikirim pakai .png)
        os.makedirs("foto", exist_ok=True)
        file_path = "foto/sertifikat.png"
        with open(file_path, "wb") as f:
            f.write(image_data)

        await client.send_file(
            event.chat_id,
            file_path,
            caption="📄 Ini sertifikat tolol kamu!",
            reply_to=event.message.id
        )

    except Exception as e:
        await event.reply(f"❌ Terjadi error: {str(e)}")

# Daftar grup aman (langsung diset manual)
GROUP_IDS = [
    -1002454481805, -1002456256135, -1001913396375, -1002109832504,
    -1002342330285, -1002592740347, -1002609124780, -1002284433354,
    -1002529588343, -1002633239878, -1002560769943, -1002573319616,
    -1002446730772, -1002552188539, -1002311885460, -1001585072585,
]

client.cfd_running = False

def is_premium(user_id):
    try:
        with open("prem.txt", "r") as f:
            return str(user_id) in f.read().splitlines()
    except FileNotFoundError:
        return False

@client.on(events.NewMessage(pattern=r'^/cfd(?: (\d+))?$'))
async def cfd(event):
    sender = await event.get_sender()
    user_id = sender.id

    # Cek akses
    if user_id != OWNER_ID and not is_premium(user_id):
        return await event.reply("❌ Lu siapa gua? Fitur ini khusus premium atau owner!")

    # Harus reply pesan
    if not event.is_reply:
        return await event.reply("❗ Balas pesan kamu sendiri dengan /cfd <jumlah>")

    try:
        jumlah = int(event.pattern_match.group(1) or 3)
    except:
        jumlah = 3

    if jumlah > len(GROUP_IDS):
        jumlah = len(GROUP_IDS)

    reply_msg = await event.get_reply_message()
    text_to_send = reply_msg.text

    if not text_to_send:
        return await event.reply("❗ Pesan tidak memiliki teks untuk dikirim.")

    targets = random.sample(GROUP_IDS, jumlah)
    client.cfd_running = True
    await event.reply(f"🚀 Mulai mengirim ke {jumlah} grup aman...")

    success, fail = 0, 0
    for gid in targets:
        if not client.cfd_running:
            break
        try:
            await client.send_message(gid, text_to_send)
            success += 1
        except:
            fail += 1
        await asyncio.sleep(random.randint(5, 8))

    client.cfd_running = False
    await event.reply(f"✅ Terkirim: {success}\n❌ Gagal: {fail}")

@client.on(events.NewMessage(pattern=r'^/stopcfd$'))
async def stopcfd(event):
    if client.cfd_running:
        client.cfd_running = False
        await event.reply("🛑 Broadcast dihentikan.")
    else:
        await event.reply("ℹ️ Tidak ada proses yang berjalan.")

        await event.reply("ℹ️ Tidak ada broadcast yang sedang berjalan.")
            
@client.on(events.NewMessage(pattern=r'^/cekidgb$'))
async def cekidgb_grup(event):
    if not check_access(event.sender_id):
        return await event.reply(" TA BOLEH ASU")
        
    if not event.is_group:
        await event.reply("⚠️ Perintah ini hanya bisa dijalankan di grup.")
        return

    try:
        group_id = event.chat_id
        sender = await event.get_sender()
        sender_id = sender.id

        # Format ID grup
        id_str = str(group_id)
        if not id_str.startswith("-100"):
            id_str = f"-100{abs(group_id)}"

        # Kirim ke PM si pemilik perintah
        await client.send_message(sender_id, f"✅ ID Grup ini: `{id_str}`")

        await event.reply("📬 ID grup sudah dikirim ke PM kamu.")

    except Exception as e:
        await event.reply(f"❌ Gagal ambil ID: {e}")

@client.on(events.NewMessage(pattern=r"^/blank_stc$"))
async def crash_ui(event):
    me = await client.get_me()
    if event.sender_id != me.id:
        await event.reply("🚫 KHUSUS PREM/OWN DAN MIIBOTZZ😜")
        return

    await event.reply("STC KE KIRIM BOS")
    try:
        result = await client(GetStickerSetRequest(
            stickerset=InputStickerSetShortName("uwuwuwubyltfr"),
            hash=0
        ))

        for doc in result.documents[:12]:
            await client.send_file(event.chat_id, doc)
            await asyncio.sleep(0.5)

    except Exception as e:
        await event.reply(f"❌ Gagal mengirim stiker: {e}")

@client.on(events.NewMessage(pattern=r'^/brat\s+(.+)', incoming=True))
@safe_run
async def brat_handler(event):
    if not check_access(event.sender_id):
        return await event.reply("🚫 TA BOLEH ASU (khusus owner/admin)")

    user_input = event.pattern_match.group(1).strip()

    # Biar multiline, ubah spasi jadi newline (misal: "gua anak telegram")
    formatted_text = "%0A".join(user_input.split())

    # Jangan animasi, biar bisa dikonversi ke .webp
    api_url = f"https://api.siputzx.my.id/api/m/brat?text={formatted_text}&isAnimated=false"

    await event.reply("🖼️ Mii lagi bikin stikernya...")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; TelegramBot/1.0)",
            "Accept": "image/jpeg"
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(api_url) as resp:
                if resp.status != 200:
                    return await event.reply(f"❌ Gagal akses API. Status: {resp.status}")
                image_data = await resp.read()

        # Konversi JPEG ke WEBP (stiker)
        image = Image.open(io.BytesIO(image_data)).convert("RGBA")
        os.makedirs("foto", exist_ok=True)
        sticker_path = "foto/brat.webp"
        image.save(sticker_path, format="WEBP")

        # Kirim sebagai STIKER
        await client.send_file(
            event.chat_id,
            sticker_path,
            file_type='sticker',
            reply_to=event.message.id
        )

    except Exception as e:
        await event.reply(f"❌ Error cuk: {str(e)}")
              
print("MiiBOTZZ running...")

with client:
    client.run_until_disconnected()
