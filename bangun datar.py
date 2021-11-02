import sys
import time
import math
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print("\n")
text = " PROGRAM MENGITUNG LUAS DAN KELILING BANGUN DATAR "
time.sleep(2)
print(text.center(100, "="))
head = ("\nBERIKUT DAFTAR BANGUN RUANG YANG KAMI DUKUNG:"
        "\n\n1. PERSEGI"
        "\n2. PERSEGI PANJANG"
        "\n3. TRAPESIUM"
        "\n4. JAJAR GENJANG"
        "\n5. SEGITIGA"
        "\n6. BELAH KETUPAT"
        "\n7. LAYANG-LAYANG"
        "\n8. LINGKARAN"
        "\n9. KELUAR"
        f"\n\n{Fore.RED}{Style.BRIGHT}MOHON UNTUK MEMASUKKAN BANGUN DATAR DI ATAS"
        "\033[39m"
        f"\n{Style.BRIGHT}MASUKKAN BANGUN DATAR: " f"{Fore.BLACK}{Back.WHITE}SEGITIGA")
time.sleep(2)
print(head)

mulai = True
while mulai == True:
    time.sleep(2)
    bangundatar = input("\nMASUKKAN BANGUN DATAR:   ").upper()
    jalan = True

    while jalan == True:

        if bangundatar == "KELUAR":
            text0 = " TERIMA KASIH TELAH MENGGUNAKAN APLIKASI KAMI "
            print(text0.center(100, "="))
            sys.exit()
        if bangundatar == "PERSEGI":
            time.sleep(2)
            print("\nMENGHITUNG KELILING DAN LUAS PERSEGI")
            sisi = int(input("MASUKKAN SISI PERSEGI:   "))
            keliling = 4*sisi
            luas = sisi*sisi
            print("KELILING PERSEGI ANDA = ", keliling, " DAN LUASNYA = ", luas)
            keluar = input("\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
            time.sleep(2)
            if keluar == "YES":
                jalan = True
                break
            else:
                exit()
        elif bangundatar == "PERSEGI PANJANG":
            time.sleep(2)
            print("\nMENGHITUNG KELILING DAN LUAS PERSEGI PANJANG")
            panjang_pp = int(input("MASUKKAN PANJANG:    "))
            lebar_pp = int(input("MASUKKAN LEBAR:      "))
            keliling_pp = (2*panjang_pp)+(2*lebar_pp)
            luas_pp = panjang_pp*lebar_pp
            print("KELILING PERSEGI PANJANG ANDA = ", keliling_pp, " DAN LUASNYA = ", luas_pp)
            keluar = input("\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
            time.sleep(2)
            if keluar == "YES":
                jalan = True
                break
            else:
                exit()
        elif bangundatar == "JAJAR GENJANG":
            time.sleep(2)
            print("\nMENGHIUTNG KELILING DAN LUAS JAJAR GENJANG")
            print("\nMASUKKAN TIAP SISI JAJAR GENJANG")
            sisia = int(input("MASUKKAN SISI a:   "))
            sisib = int(input("MASUKKAN SISI b:   "))
            sisic = int(input("MASUKKAN SISI c:   "))
            sisid = int(input("MASUKKAN SISI d:   "))
            print("\nMASUKKAN TINGGI JAJAR GENJANG")
            tinggi_jg = int(input("MASUKKAN TINGGI:   "))
            keliling_jg = sisia + sisib + sisic + sisid
            luas_jg = sisia*tinggi_jg
            print("KELILING JAJAR GENJANG ANDA = ", keliling_jg, " DAN LUASNYA = ", luas_jg)
            keluar = input("\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
            time.sleep(2)
            if keluar == "YES":
                jalan = True
                break
            else:
                exit()
        elif bangundatar == "SEGITIGA":
            time.sleep(2)
            print("\nMENGHITUNG KELLING DAN LUAS SEGITIGA")
            print("\nMASUKKAN TIAP SISI SEGITIGA")
            sisias = int(input("MASUKKAN SISI a:   "))
            sisibs = int(input("MASUKKAN SISI b:   "))
            sisics = int(input("MASUKKAN SISI c:   "))
            print("\nMASUKKAN TINGGI SEGITIGA")
            tinggi_s = int(input("MASUKKAN TINGGI:   "))
            keliling_s = sisias + sisibs + sisics
            luas_s = 1/2*sisias*tinggi_s
            print("KELILING SEGITIGA ANDA = ", keliling_s, " DAN LUASNYA = ", luas_s)
            keluar = input("\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
            time.sleep(2)
            if keluar == "YES":
                jalan = True
                break
            else:
                exit()
        elif bangundatar == "BELAH KETUPAT":
            time.sleep(2)
            print("\nMENGHIUTNG KELILING DAN LUAS BELAH KETUPAT")
            print("\nMASUKKAN TIAP SISI BELAH KETUPAT")
            sisiab = int(input("MASUKKAN SISI a:   "))
            sisibb = int(input("MASUKKAN SISI b:   "))
            sisicb = int(input("MASUKKAN SISI c:   "))
            sisidb = int(input("MASUKKAN SISI d:   "))
            print("\nMASUKKAN DIAGONAL BELAH KETUPAT")
            diagonal1 = int(input("MASUKKAN DIAGONAL 1:   "))
            diagonal2 = int(input("MASUKKAN DIAGONAL 2:   "))
            keliling_bk = sisiab + sisibb + sisicb + sisidb
            luas_bk = 1/2*diagonal1*diagonal2
            print("KELILING BELAH KETUPAT ANDA = ", keliling_bk, " DAN LUASNYA = ", luas_bk)
            keluar = input("\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
            time.sleep(2)
            if keluar == "YES":
                jalan = True
                break
            else:
                exit()
        elif bangundatar == "LAYANG-LAYANG":
            time.sleep(2)
            print("\nMENGHITUNG KELILING DAN LUAS LAYANG-LAYANG")
            print("\nMASUKKAN TIAP SISI LAYANG-LAYANG")
            sisial = int(input("MASUKKAN SISI a:    "))
            sisibl = int(input("MASUKKAN SISI b:    "))
            sisicl = int(input("MASUKKAN SISI c:    "))
            sisidl = int(input("MASUKKAN SISI d:    "))
            print("\nMASUKKAN DIAGONAL LAYANG-LAYANG")
            dsatu = int(input("MASUKKAN DIAGONAL 1:    "))
            ddua = int(input("MASUKKAN DIAGONAL 2:    "))
            kl = sisial + sisibl + sisicl + sisidl
            luasl = 1/2*dsatu*ddua
            print("KELILING BELAH KETUPAT ANDA = ", kl, " DAN LUASNYA = ", luasl)
            keluar = input("\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
            time.sleep(2)
            if keluar == "YES":
                jalan = True
                break
            else:
                exit()
        elif bangundatar == "TRAPESIUM":
            time.sleep(2)
            print("\nMENGHITUNG KELILING DAN LUAS TRAPESIUM")
            print("\nMASUKKAN TIAP SISI TRAPESIUM")
            st1 = int(input("MASUKKAN SISI a:   "))
            st2 = int(input("MASUKKAN SISI b:   "))
            st3 = int(input("MASUKKAN SISI c:   "))
            st4 = int(input("MASUKKAN SISI d:   "))
            tp = int(input("MASUKKAN TINGGI TRAPESIUM:  "))
            kt = st1 + st2 + st3 + st4
            lt = st1+st2/2*tp
            print("KELILING BELAH KETUPAT ANDA = ", kt, " DAN LUASNYA = ", lt)
            keluar = input("\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
            time.sleep(2)
            if keluar == "YES":
                jalan = True
                break
            else:
                exit()
        elif bangundatar == "LINGKARAN":
            time.sleep(2)
            print("\nMENGHITUNG KELILING DAN LUAS LINGKARAN")
            r = int(input("MASUKKAN JARI-JARI:  "))
            k = 2*(math.pi)*r
            l = (math.pi)*r*r
            print("KELILING LINGKARAN ANDA = ", k, " DAN LUASNYA = ", l)
            keluar = input("\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
            time.sleep(2)
            if keluar == "YES":
                jalan = True
                break
            else:
                exit()
        else:
            print("MASUKKAN PERINTAH YANG TERTERA PADA MONITOR!")
            jalan = False
            bangundatar = input("\nMASUKKAN BANGUN DATAR:   ").upper()
            if bangundatar == "PERSEGI" or "PERSEGI PANJANG" or "JAJAR GENJANG" or "SEGITIGA" or "LAYANG-LAYANG" or "TRAPESIUM" or "BELAH KETUPAT" or "KELUAR" or "LINGKARAN":
                jalan = True

    if jalan == True:
        print("\n")
        kembali = " SELAMAT DATANG KEMBALI "
        print(kembali.center(100, "="))
        time.sleep(2)
        head1 = ("\nBERIKUT DAFTAR BANGUN RUANG YANG KAMI DUKUNG:"
                "\n\n1. PERSEGI"
                "\n2. PERSEGI PANJANG"
                "\n3. TRAPESIUM"
                "\n4. JAJAR GENJANG"
                "\n5. SEGITIGA"
                "\n6. BELAH KETUPAT"
                "\n7. LAYANG-LAYANG"
                "\n8. LINGKARAN"
                "\n9. KELUAR"
                f"\n\n{Fore.RED}{Style.BRIGHT}MOHON UNTUK MEMASUKKAN BANGUN DATAR DI ATAS"
                "\033[39m"
                f"\n{Style.BRIGHT}MASUKKAN BANGUN DATAR: " f"{Fore.BLACK}{Back.WHITE}SEGITIGA")
        time.sleep(2)
        print(head1)



