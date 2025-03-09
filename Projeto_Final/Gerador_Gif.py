from PIL import Image
import imageio
import os

# Função para ler todas as imagens de uma pasta
def ler_imagens(pasta):
    imagens = []
    for filename in sorted(os.listdir(pasta)):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            caminho = os.path.join(pasta, filename)
            imagens.append(Image.open(caminho))
    return imagens

# Função para criar um GIF a partir de uma sequência de imagens
def criar_gif(imagens, caminho_saida, duracao):
    frames = [imageio.imread(img.filename) for img in imagens]
    imageio.mimsave(caminho_saida, frames, duration=duracao)

# Caminhos de entrada e saída
pasta_imagens = r"C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\imagens"
caminho_saida_gif = r"C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\saida.gif"

# Ler imagens da pasta
imagens = ler_imagens(pasta_imagens)

# Definir a duração de cada frame (em segundos)
duracao = 0.5

# Criar GIF
criar_gif(imagens, caminho_saida_gif, duracao)

print(f"GIF criado e salvo em: {caminho_saida_gif}")
