import matplotlib.pyplot as plt

# Dados para os gráficos
metodos = ["LZW", "Zlib", "OptiPNG", "pngcrush", "Gifsicle", "ImageMagick"]
tempo_medio = [0.002, 0.001, 0.5, 0.6, 0.4, 0.5]  # em segundos
reducao = [40, 45, 30, 35, 25, 30]  # em porcentagem
memoria_media = [15, 10, 50, 55, 40, 45]  # em KB

# Configuração dos gráficos na horizontal para uma folha A4
fig, axes = plt.subplots(3, 1, figsize=(11.7, 8.3))  # Tamanho A4 na orientação paisagem

# Gráfico de Tempo Médio
axes[0].barh(metodos, tempo_medio, color='blue', alpha=0.7)
axes[0].set_title("Tempo Médio de Compressão")
axes[0].set_xlabel("Tempo (s)")

# Gráfico de Redução de Tamanho
axes[1].barh(metodos, reducao, color='green', alpha=0.7)
axes[1].set_title("Redução Média de Tamanho (%)")
axes[1].set_xlabel("Redução (%)")

# Gráfico de Memória Média
axes[2].barh(metodos, memoria_media, color='red', alpha=0.7)
axes[2].set_title("Consumo Médio de Memória")
axes[2].set_xlabel("Memória (KB)")

# Ajustar layout para melhor visualização em uma folha A4
plt.tight_layout()
plt.show()
