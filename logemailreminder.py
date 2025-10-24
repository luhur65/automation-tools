import re
from datetime import datetime
from playwright.sync_api import sync_playwright

CABANG = {
    "Medan": "http://tasmdn.kozow.com:8074",
    "Jakarta": "http://tasjkt.kozow.com:8074",
    "Surabaya": "http://tassby.kozow.com:8074",
    "Makassar": "http://tasmks.kozow.com:8074"
}

USERNAME = "dharma"
PASSWORD = "12345678qq"

def cek_log_email(page, cabang):
    page.goto(f"{CABANG[cabang]}/trucking/logreminderemail/index")
    page.wait_for_load_state("networkidle")

    # Ambil isi tabel log email
    html = page.inner_html("#gview_jqGrid")
    today = datetime.now().strftime("%d-%m-%Y")

    # Cari tanggal hari ini di grid
    pattern = rf"{today}\s+\d{{2}}:\d{{2}}:\d{{2}}"  # contoh: 24-10-2025 08:45:22
    match = re.search(pattern, html)

    if match:
        return match.group(0)
    else:
        return None


def login(page, base_url):
    page.goto(f"{base_url}/trucking/login")
    page.get_by_role("textbox", name="User ID").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_load_state("networkidle")


def run():
    hasil = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for cabang, base_url in CABANG.items():
            context = browser.new_context()
            page = context.new_page()

            print(f"🔍 Mengecek log email cabang {cabang} ...")
            try:
                login(page, base_url)
                waktu = cek_log_email(page, cabang)
                hasil[cabang] = waktu if waktu else "-"
            except Exception as e:
                hasil[cabang] = f"❌ Error: {e}"
            finally:
                context.close()

        browser.close()

    print("\n=== HASIL CEK LOG EMAIL REMINDER ===")
    for cabang, waktu in hasil.items():
        if waktu and waktu != "-":
            print(f"✅ {cabang}: Email terkirim pada {waktu}")
        else:
            print(f"⚠️ {cabang}: Tidak ada log pengiriman hari ini")


if __name__ == "__main__":
    run()
