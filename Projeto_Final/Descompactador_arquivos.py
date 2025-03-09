import sys
import time
import os
import tracemalloc
import zlib
import pickle
import subprocess

# Diretório base
base_dir = r"C:\\Users\\rodri\\OneDrive\\Área de Trabalho"

# Função para ler um arquivo de texto
def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()

# Função para salvar dados comprimidos
def salvar_comprimido(caminho, dados):
    with open(caminho, 'wb') as arquivo:
        pickle.dump(dados, arquivo)

# Função para carregar dados comprimidos
def carregar_comprimido(caminho):
    with open(caminho, 'rb') as arquivo:
        return pickle.load(arquivo)

# Funções de medição
def medir_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return fim - inicio, resultado

def medir_memoria(func, *args):
    tracemalloc.start()
    resultado = func(*args)
    atual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return pico, resultado

# Compressão LZW
def compress_lzw(uncompressed):
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionary[w])
    return result

# Compressão Zlib
def compress_zlib(data):
    return zlib.compress(data.encode('utf-8'))

# Compressão GIF usando Gifsicle
def compress_gif_gifsicle(input_path, output_path):
    subprocess.run(['gifsicle', '--optimize', input_path, '-o', output_path])

# Compressão GIF usando ImageMagick
def compress_gif_imagemagick(input_path, output_path):
    subprocess.run(['magick', 'convert', input_path, '-layers', 'Optimize', output_path])

# Compressão PNG usando OptiPNG
def compress_png_optipng(input_path, output_path):
    subprocess.run(['optipng', '-o7', input_path, '-out', output_path])

# Compressão PNG usando pngcrush
def compress_png_pngcrush(input_path, output_path):
    subprocess.run(['pngcrush', '-brute', input_path, output_path])

# Menu de escolha do usuário
print("Escolha o tipo de compressão:")
print("1 - Texto (LZW)")
print("2 - Texto (Zlib)")
print("3 - GIF (Gifsicle)")
print("4 - GIF (ImageMagick)")
print("5 - PNG (OptiPNG)")
print("6 - PNG (pngcrush)")

opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    caminho_entrada = os.path.join(base_dir, "arquivo.txt")
    caminho_saida = os.path.join(base_dir, "saida_lzw.pkl")
    data = ler_arquivo(caminho_entrada)
    tempo_compressao, compressed = medir_tempo(compress_lzw, data)
    pico_memoria, _ = medir_memoria(compress_lzw, data)
    salvar_comprimido(caminho_saida, compressed)
    print(f"Texto comprimido com LZW salvo em: {caminho_saida}")
    print(f"Tempo de compressão: {tempo_compressao} segundos")
    print(f"Pico de uso de memória: {pico_memoria} bytes")

elif opcao == "2":
    caminho_entrada = os.path.join(base_dir, "arquivo.txt")
    caminho_saida = os.path.join(base_dir, "saida_zlib.txt")
    data = ler_arquivo(caminho_entrada)
    tempo_compressao, compressed = medir_tempo(compress_zlib, data)
    pico_memoria, _ = medir_memoria(compress_zlib, data)
    with open(caminho_saida, 'wb') as f:
        f.write(compressed)
    print(f"Texto comprimido com Zlib salvo em: {caminho_saida}")
    print(f"Tempo de compressão: {tempo_compressao} segundos")
    print(f"Pico de uso de memória: {pico_memoria} bytes")

elif opcao == "3":
    caminho_entrada = os.path.join(base_dir, "exemplo.gif")
    caminho_saida = os.path.join(base_dir, "exemplo_comprimido_gifsicle.gif")
    tempo_compressao, _ = medir_tempo(compress_gif_gifsicle, caminho_entrada, caminho_saida)
    pico_memoria, _ = medir_memoria(compress_gif_gifsicle, caminho_entrada, caminho_saida)
    print(f"GIF comprimido (Gifsicle) salvo em: {caminho_saida}")
    print(f"Tempo de compressão: {tempo_compressao} segundos")
    print(f"Pico de uso de memória: {pico_memoria} bytes")

elif opcao == "4":
    caminho_entrada = os.path.join(base_dir, "exemplo.gif")
    caminho_saida = os.path.join(base_dir, "exemplo_comprimido_imagemagick.gif")
    tempo_compressao, _ = medir_tempo(compress_gif_imagemagick, caminho_entrada, caminho_saida)
    pico_memoria, _ = medir_memoria(compress_gif_imagemagick, caminho_entrada, caminho_saida)
    print(f"GIF comprimido (ImageMagick) salvo em: {caminho_saida}")
    print(f"Tempo de compressão: {tempo_compressao} segundos")
    print(f"Pico de uso de memória: {pico_memoria} bytes")

elif opcao == "5":
    caminho_entrada = os.path.join(base_dir, "exemplo.png")
    caminho_saida = os.path.join(base_dir, "exemplo_comprimido_optipng.png")
    tempo_compressao, _ = medir_tempo(compress_png_optipng, caminho_entrada, caminho_saida)
    pico_memoria, _ = medir_memoria(compress_png_optipng, caminho_entrada, caminho_saida)
    print(f"PNG comprimido (OptiPNG) salvo em: {caminho_saida}")
    print(f"Tempo de compressão: {tempo_compressao} segundos")
    print(f"Pico de uso de memória: {pico_memoria} bytes")

elif opcao == "6":
    caminho_entrada = os.path.join(base_dir, "exemplo.png")
    caminho_saida = os.path.join(base_dir, "exemplo_comprimido_pngcrush.png")
    tempo_compressao, _ = medir_tempo(compress_png_pngcrush, caminho_entrada, caminho_saida)
    pico_memoria, _ = medir_memoria(compress_png_pngcrush, caminho_entrada, caminho_saida)
    print(f"PNG comprimido (pngcrush) salvo em: {caminho_saida}")
    print(f"Tempo de compressão: {tempo_compressao} segundos")
    print(f"Pico de uso de memória: {pico_memoria} bytes")

else:
    print("Opção inválida. Por favor, escolha uma opção válida.")