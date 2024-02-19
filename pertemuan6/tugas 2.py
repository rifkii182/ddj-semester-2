belanja = [
    {"produk":"baju","jumlah":20},
    {"produk":"celana","jumlah":15},
    {"produk":"sepatu","jumlah":25},
    {"produk":"tas","jumlah":10},
]

total_belajaan = 0
for item in belanja :
    total_belajaan += item ["jumlah"]
    
print("total belanja :",total_belajaan)