import io
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

def pdf2text(inPDFfile):
    infile = open(inPDFfile,'rb')
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    TxtConverter = TextConverter(resMgr,retData,laparams=LAParams())
    interpreter = PDFPageInterpreter(resMgr,TxtConverter)

    for page in PDFPage.get_pages(infile):
        interpreter.process_page(page)
    txt=retData.getvalue()
    return txt

makaleMat=['mat1.pdf','mat3.pdf','mat4.pdf','mat5.pdf','mat6.pdf','mat7.pdf','mat8.pdf']
makaleTarih=['tarih1.pdf','tarih2.pdf','tarih3.pdf','tarih4.pdf','tarih5.pdf']
makaleTip=['tip1.pdf','tip2.pdf','tip3.pdf','tip4.pdf','tip5.pdf','tip6.pdf','tip7.pdf','tip8.pdf','tip9.pdf']
print("1: a-theorem-on-inverses-of-tridiagonal-matrices.pdf\n2: advances-in-gene-therapy-technologies.pdf\n3: age-related-macular-degeneration.pdf\n4: history-of-us-vol-x-ch1.pdf\n5: norm-estimates-for-inverses-of-vandermonde-matrices.pdf\n6: patients-with-suspected-glaucoma.pdf\n7: positive-definite-matrices-and-the-s-divergence.pdf\n8: the-british-empire-city-states-and-commercially-oriented-politics.pdf\n9: the-ottoman-empire-and-the-capitalist-world-economy.pdf")
sozluk = {1: "a-theorem-on-inverses-of-tridiagonal-matrices.pdf",2: "advances-in-gene-therapy-technologies.pdf",3: "age-related-macular-degeneration.pdf",4: "history-of-us-vol-x-ch1.pdf",5: "norm-estimates-for-inverses-of-vandermonde-matrices.pdf",6:"patients-with-suspected-glaucoma.pdf",7:"positive-definite-matrices-and-the-s-divergence.pdf",8:"the-british-empire-city-states-and-commercially-oriented-politics.pdf",9:"the-ottoman-empire-and-the-capitalist-world-economy.pdf"}
testMakale= int(input("Test etmek istediğiniz makale numarasını giriniz : "))
matematikKelimeler =[]
tarihKelimeler =[]
tipKelimeler =[]
testKelimeler=[]

stops=[]
with open('stopWords.txt','r') as file:
    for line in file:
        for word in line.split():
            stops.append(word)
#----------------------------------------------------
for matfor in makaleMat:
    text = pdf2text(matfor)
    noktalama = [".",",",":","?","'",'"',"”","–", "—", '"',";","(",")","[","]"]
    text=text.replace("-"," ")
    text=text.replace("/"," ")
    for i in noktalama:
        text= text.replace(i,"")

    text= text.lower()
    text= text.split()
    for kelime in text:
        if len(kelime)>2:
            matematikKelimeler.append(kelime)

    for sword in stops:
        for word in matematikKelimeler:
            if sword==word:
                 matematikKelimeler.remove(word)
#-------------------------------------------------------------
for tarihfor in makaleTarih:
    text = pdf2text(tarihfor)
    noktalama = [".",",",":","?","'",'"',"”","–", "—", '"',";","(",")","[","]"]
    text=text.replace("-"," ")
    text=text.replace("/"," ")
    for i in noktalama:
        text= text.replace(i,"")

    text= text.lower()
    text= text.split()
    for kelime in text:
        if len(kelime)>2:
            tarihKelimeler.append(kelime)
    for sword in stops:
        for word in tarihKelimeler:
            if sword==word:
                 tarihKelimeler.remove(word)
#------------------------------------------------------------------

for tipfor in makaleTip:
    text = pdf2text(tipfor)
    noktalama = [".",",",":","?","'",'"',"”","–", "—", '"',";","(",")","[","]"]
    text=text.replace("-"," ")
    text=text.replace("/"," ")
    for i in noktalama:
        text= text.replace(i,"")
    text= text.lower()
    text= text.split()
    for kelime in text:
        if len(kelime)>2:
            tipKelimeler.append(kelime)
    for sword in stops:
        for word in tipKelimeler:
            if sword==word:
                 tipKelimeler.remove(word)
#---------------------------------------------------------------------


text = pdf2text(sozluk[testMakale])
noktalama = [".",",",":","?","'",'"',"”","–", "—", '"',";","(",")","[","]"]
text=text.replace("-"," ")
text=text.replace("/"," ")
for i in noktalama:
    text= text.replace(i,"")
text= text.lower()
text= text.split()
for kelime in text:
    if len(kelime)>2:
        testKelimeler.append(kelime)
for sword in stops:
    for word in testKelimeler:
        if sword==word:
             testKelimeler.remove(word)

test = set(testKelimeler)
tip = set(tipKelimeler)
tarih = set(tarihKelimeler)
matematik = set(matematikKelimeler)

tipKar = (test & tip)
tarKar= (test & tarih)
matKar = (test & matematik)

if len(tipKar) > len(tarKar):
    if len(tipKar) > len(matKar):
        print("Girilen makale Tıp makalesidir")
    else:
        print("Girilen makale Matematik makalesidir")

else:
    if len(tarKar) > len(matKar):
        print("Girilen makale Tarih makalesidir")
    else:
        print("Girilen makale Matematik makalesidir")




