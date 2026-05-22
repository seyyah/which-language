import subprocess
import os
import shutil

# --- Yardimci Fonksiyon ---
def run_cmd(args):
    result = subprocess.run(
        ["python", "solution_v1.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

# --- Setup ve Temizlik ---
def setup_function():
    if os.path.exists(".minitodo"):
        shutil.rmtree(".minitodo")

# --- V1 Testleri ---

# 1. 'init' komutunun dizin olusturma testi
def test_init_creates_directory():
    output = run_cmd(["init"])
    assert os.path.exists(".minitodo")
    assert "basariyla olusturuldu" in output

# 2. 'init' komutunun tekrar calistirilma hata testi
def test_init_already_exists():
    run_cmd(["init"])
    output = run_cmd(["init"])
    assert "Sistem zaten baslatilmis" in output

# 3. 'add' komutu ile tek bir gorev ekleme testi
def test_add_single_task():
    run_cmd(["init"])
    output = run_cmd(["add", "Sut al"])
    assert "Gorev #1 eklendi" in output

# 4. 'add' komutunda eksik arguman hata testi
def test_missing_arguments_add():
    run_cmd(["init"])
    output = run_cmd(["add"])
    assert "Kullanim Hasi" in output