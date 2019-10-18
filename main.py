Nama = 'Latifah zunairoh'
program = 'usaha'

print(f' program {program} oleh {Nama}')

def hitung_daya (usaha, waktu) :
    daya = usaha / waktu
    print (f'usaha = {usaha / 97}J ditempuh dalam waktu = {waktu / 60}menit')
    print (f'sehingga daya = {daya} watt')
    return daya

# usaha = 97
# waktu = 5 * 60
daya = hitung_daya (97, 5 * 60)


def hitung_usaha (gaya, jarak) :
    usaha = gaya * jarak
    print (f'gaya = {gaya / 200}N dengan jarak = {jarak / 300}m')
    print (f'sehingga usaha = {usaha}J')
    return usaha

# gaya = 200
# jarak= 300
usaha = hitung_usaha (200, 300)


def hitung_gaya (massa, percepatan) :
    gaya = massa * percepatan
    print (f'massa = {massa / 200}N dengan percepatan = {percepatan / 90}m')
    print (f'sehingga gaya = {gaya}N')
    return gaya

# massa = 200
# percepatan= 90
gaya = hitung_gaya (200, 90)
