import pytesseract
import cv2
import jellyfish as jf

def buscarPorPalavra(palavra,nLinhas):
    index = 0
    textoRetorno = ''
    for x in splitTexto:
        index += 1
        if(len(str(x).split()) != 0):
            if(jf.levenshtein_distance(palavra.upper(), str(x).split()[0].upper()) < 5):
                textoRetorno += x
                for y in range(nLinhas):
                    textoRetorno += "\n" + splitTexto[index + y]
    
    return textoRetorno


img = cv2.imread("teste.jpg",0)
clahe = cv2.createCLAHE(clipLimit=1, tileGridSize=(8, 8))
equalized = clahe.apply(img)

caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(equalized, lang="por")

splitTexto = str(texto).split("\n")
nome = splitTexto[0]
print("----------------------------------------------------------------------------------------------------------------------------")
print("Nome: ")
print(nome)
objetivo = buscarPorPalavra("objetivo",1)
print("----------------------------------------------------------------------------------------------------------------------------")
print("Objetivo: ")
print(objetivo)
formacao = buscarPorPalavra("Formação",5)
print("----------------------------------------------------------------------------------------------------------------------------")
print("Educação: ")
print(formacao)
experiencia = buscarPorPalavra("Experiência",4)
print("----------------------------------------------------------------------------------------------------------------------------")
print("Experiência: ")
print(experiencia)
    
