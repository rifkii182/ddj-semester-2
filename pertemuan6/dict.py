belanja = [
       {"buah":"semangka","harga":12000},
        {"buah":"nanas","harga":10000},
         {"buah":"pepaya","harga":12000},
]
    
total_belajaan = 0
for item in belanja :
    total_belajaan += item ["harga"]
    
print("total belanja :",total_belajaan)