import math                                                     # import module math

def amountConverter(item):                                      # membuat fungsi
    RM = math.floor(item/500)                                   # perhitungan rim
    KD = math.floor((item%500)/20)                              # perhitungan kodi
    LSN = math.floor((item%50/20)%12)                           # perhitungan lusin
    print('Konversi :',str(RM)+':'+str(KD)+':'+str(LSN))        # cetak hasil perhitungan dan konversi ke string

while True:                                                     # membuat perulangan dengan while
    try:                                                        # try & except untuk filter data sesuai kriteria
        item = int(input('Masukkan bilangan bulat : '))         # input bilangan secara manual
        if 1 < item < 35999:                                    # kriteria sesuai, memanggil fungsi
            amountConverter(item)                               
        elif item > 35999:                                      # kriteria tidak sesuai
            print('Invalid Input!')
        elif 0 < item < 1:                                      # kriteria tidak sesuai
            print('Invalid Input!')
        elif item < 0:                                          # kriteria tidak sesuai
            print('Invalid Input!')                                                     
    except:                                                     # kriteria tidak sesuai
        print('Invalid Input!')