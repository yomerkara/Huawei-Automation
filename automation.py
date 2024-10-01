

# Kopyalanacak sütunlar ve hedef hücreler
columns_to_copy = ['Cell ID', 'Region', 'OAM SITE IP', 'New Huawei RNC']  # Kopyalanacak sütunlar
hedef_hucreler1 = {
    'OAM SITE IP': [(4, 1)],  # Birden fazla hedef hücre (satır, sütun)
}
hedef_hucreler2 = {
    'Cell ID': [(9, 3), (9, 16), (9, 25), (9, 36), (9, 61)],  # Birden fazla hedef hücre (satır, sütun)
    'New Huawei RNC': [(9, 1)]
}

# Sütun isimlerini bulma
column_indices1 = {cell.value: cell.column for cell in kaynak_sayfa1[1] if cell.value in columns_to_copy}
column_indices2 = {cell.value: cell.column for cell in kaynak_sayfa2[1] if cell.value in columns_to_copy}

# Hata kontrolü
for col_name in columns_to_copy:
    if col_name not in column_indices1:
        print(f"Hata: '{col_name}' sütunu kaynak dosya 1'de bulunamadı.")
    if col_name not in column_indices2:
        print(f"Hata: '{col_name}' sütunu kaynak dosya 2'de bulunamadı.")

# Verileri kopyalama ve hedef dosyaya yazma
for col_name in columns_to_copy:
    if col_name in column_indices1:
        col_index1 = column_indices1[col_name]
        for hedef_satir, hedef_sutun in hedef_hucreler1.get(col_name, []):
            for row in range(2, 7):  # 2'den 7'ye kadar olan satırlar (ilk 6 satır)
                value1 = kaynak_sayfa1.cell(row=row, column=col_index1).value
                hedef_sayfa1.cell(row=hedef_satir + row - 2, column=hedef_sutun, value=value1)
    
    if col_name in column_indices2:
        col_index2 = column_indices2[col_name]
        for hedef_satir, hedef_sutun in hedef_hucreler2.get(col_name, []):
            for row in range(2, 8):  # 2'den 7'ye kadar olan satırlar (ilk 6 satır)
                value2 = kaynak_sayfa2.cell(row=row, column=col_index2).value
                hedef_sayfa2.cell(row=hedef_satir + row - 2, column=hedef_sutun, value=value2)

# Dosyaları kaydetme
hedef_kitap1.save(hedef_dosya_yolu1)
hedef_kitap2.save(hedef_dosya_yolu2)

print("bitti")
