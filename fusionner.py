# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileMerger
import os, string as st

# Récupérer la liste des fichiers du répertoire courant
files=sorted(list(os.walk('.'))[0][2])
print("les fichiers dans le dosssier courant sont: ")
print(files)

# Sélectionner la liste des fichiers finissant par .pdf ou .PDF
pdfs=[x for x in files if '.pdf' == str.lower(x[-4:])]

# Lister les fichiers pdf à fusionner
print( "\nListe des fichiers fusionnés : \n")
for i,f in enumerate(pdfs):
    print ('%2d : %s'%(i+1,f))

# Fusionner les pdf du répertoire courant
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))
    
# Créer un répertoire "fusion_pdf" s'il n'existe pas déjà
try:
    os.mkdir(r'.\fusion_pdf')
except:
    pass

# './fusion_pdf/result.pdf' : fichier contenant les pdf fusionnés   
with open('./fusion_pdf/result.pdf', 'wb') as fout:
    merger.write(fout)

print ("\nLes fichiers listés sont concaténés dans './fusion_pdf/result.pdf'\n")