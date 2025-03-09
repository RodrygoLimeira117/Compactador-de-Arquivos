import random
import string

def generate_text_file(filename, word_count=100000000000):
    words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10))) for _ in range(word_count)]
    text = ' '.join(words)
    
    filepath = "C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\" + filename
    
    with open(filepath, 'w') as f:
        f.write(text)
    
    print(f"Arquivo {filepath} gerado com {word_count} palavras.")

# Gerar arquivo
generate_text_file("arquivo.txt")