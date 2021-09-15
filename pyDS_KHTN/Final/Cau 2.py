import csv
print("%70s" %"DANH SÁCH SẢN PHẨM")
print("%-6s %-5s %-30s %-30s %-35s %10s" %("STT", "MÃ SP", "TÊN SP", "URL" , "HÌNH SP" , "GIÁ"))
file = open("san_pham.csv", 'r', encoding='utf-8')
for STT, row in enumerate(csv.reader(file)):
    print("%-6s %-5s %-30s %-30s %-35s %10s" %(STT+1, row[0],row[1],row[2],row[3],row[4]))
