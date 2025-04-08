import cv2
import matplotlib.pyplot as plt

def equalizar_histograma_colorido(img):
    # Converter para YCrCb
    img_y_cr_cb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    
    # Equalizar apenas o canal Y
    img_y_cr_cb[:, :, 0] = cv2.equalizeHist(img_y_cr_cb[:, :, 0])
    
    # Converter de volta para BGR
    return cv2.cvtColor(img_y_cr_cb, cv2.COLOR_YCrCb2BGR)

def mostrar_imagem_comparacao(titulo, original, equalizada):
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    axs[0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    axs[0].set_title(f'{titulo} - Original')
    axs[0].axis('off')
    
    axs[1].imshow(cv2.cvtColor(equalizada, cv2.COLOR_BGR2RGB))
    axs[1].set_title(f'{titulo} - Equalizada')
    axs[1].axis('off')
    
    plt.tight_layout()
    plt.show()

# Lista de arquivos
arquivos = ["lena.png", "unequalized.jpg", "img_aluno.jpg"]

for arquivo in arquivos:
    img = cv2.imread(arquivo)
    if img is None:
        print(f"⚠️ Não encontrei a imagem: {arquivo}")
        continue

    img_eq = equalizar_histograma_colorido(img)
    mostrar_imagem_comparacao(arquivo.split('.')[0], img, img_eq)
    cv2.imwrite(f"{arquivo.split('.')[0]}_equalizada.png", img_eq)
