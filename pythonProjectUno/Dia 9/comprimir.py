import zipfile

#Para comprimir
mi_zip = zipfile.ZipFile('mi.zip', 'w')
mi_zip.write('texto_A.txt')
mi_zip.write('texto_B.txt')

mi_zip.close()

#tambien se puede comprimir y descomprimir usando shutil con shutil