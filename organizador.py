import os
import shutil
import time
import tkinter as tk  # Importa o tkinter
from tkinter import filedialog  # Importa o seletor de arquivos/pastas

# --- Configuração Inicial ---

# 1. Criar a janela raiz do tkinter e escondê-la
root = tk.Tk()
root.withdraw() # Esconde a janela principal feia

# 2. Abrir a janela para selecionar a pasta
print("Ok, rod. Vai abrir uma janela pra você escolher a pasta de Downloads...")
print("Se não abrir, talvez esteja atrás de outra janela. Procura aí.")
time.sleep(1) # Pausa dramática

download_folder = filedialog.askdirectory(title="Rod, escolha a pasta de Downloads pra organizar")

# 3. Verificar se o usuário selecionou uma pasta ou cancelou
if not download_folder:
    print("\nUé, cancelou? Ou não escolheu nenhuma pasta? Tá bom então, abortando a missão.")
    exit() # Tchau, já que você não colabora.

# O resto é praticamente igual ao script anterior...

# Dicionário com as categorias e suas extensões (tudo em minúsculo!)
categorias = {
    "Imagens": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.heic', '.tiff'],
    "Documentos": ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.odt', '.ods', '.odp', '.rtf', '.csv'],
    "Vídeos": ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm'],
    "Músicas": ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    "Compactados": ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2'],
    "Executáveis": ['.exe', '.msi', '.dmg', '.app', '.deb', '.rpm'],
    "Código e Dev": ['.py', '.ipynb', '.js', '.html', '.css', '.java', '.c', '.cpp', '.cs', '.php', '.sql', '.json', '.xml', '.sh'],
    "Fontes": ['.ttf', '.otf', '.woff', '.woff2'],
    "Outros": []
}

# --- Mão na Massa ---

print(f"\nBeleza, rod. A pasta escolhida foi: {download_folder}")
print("Organizando a bagunça... Relaxa aí.")
time.sleep(2)

# Verificar se o caminho selecionado é realmente uma pasta (nunca se sabe)
if not os.path.isdir(download_folder):
    print(f"Erro: O caminho '{download_folder}' que você selecionou não parece ser uma pasta válida. Tenta de novo.")
    exit()

# Criar as pastas das categorias (se não existirem)
for categoria in categorias:
    categoria_path = os.path.join(download_folder, categoria)
    os.makedirs(categoria_path, exist_ok=True)

outros_path = os.path.join(download_folder, "Outros")
os.makedirs(outros_path, exist_ok=True)

# Listar todos os itens na pasta de Downloads
try:
    arquivos_na_pasta = os.listdir(download_folder)
except Exception as e:
    print(f"Ih, deu ruim ao tentar ler a pasta: {e}")
    print("Verifica se você tem permissão pra acessar essa pasta.")
    exit()

arquivos_movidos = 0
arquivos_ignorados = 0

# Iterar sobre cada item
for item_nome in arquivos_na_pasta:
    item_path_completo = os.path.join(download_folder, item_nome)

    if os.path.isdir(item_path_completo):
        eh_pasta_categoria = False
        for categoria in categorias:
            if item_nome == categoria:
                eh_pasta_categoria = True
                break
        if item_nome == "Outros" or eh_pasta_categoria:
            continue
        else:
             print(f"Ignorando pasta desconhecida: {item_nome}")
             arquivos_ignorados += 1
             continue

    try:
        _, extensao = os.path.splitext(item_nome)
        extensao = extensao.lower()

        if not extensao:
            destino_path = os.path.join(outros_path, item_nome)
            # print(f"Arquivo sem extensão: '{item_nome}' -> Movendo para 'Outros'") # Descomente para debug
            # Precisamos garantir que o destino não seja o mesmo que a origem (caso raro)
            if item_path_completo != destino_path:
                 shutil.move(item_path_completo, destino_path)
                 arquivos_movidos += 1
            else:
                arquivos_ignorados +=1
            continue

        categoria_destino = None
        for categoria, extensoes in categorias.items():
            if extensao in extensoes:
                categoria_destino = categoria
                break

        if categoria_destino:
            destino_folder = os.path.join(download_folder, categoria_destino)
            destino_path = os.path.join(destino_folder, item_nome)
            # print(f"Movendo '{item_nome}' para '{categoria_destino}'...") # Descomente para debug
            if item_path_completo != destino_path:
                shutil.move(item_path_completo, destino_path)
                arquivos_movidos += 1
            else:
                arquivos_ignorados +=1
        else:
            destino_path = os.path.join(outros_path, item_nome)
            # print(f"Extensão '{extensao}' desconhecida. Movendo '{item_nome}' para 'Outros'...") # Descomente para debug
            if item_path_completo != destino_path:
                shutil.move(item_path_completo, destino_path)
                arquivos_movidos += 1
            else:
                arquivos_ignorados +=1

    except FileNotFoundError:
         print(f"Opa! O arquivo '{item_nome}' sumiu no meio do processo? Estranho... Ignorando.")
         arquivos_ignorados += 1
    except PermissionError:
        print(f"Xii... Sem permissão para mover '{item_nome}'. Pulando esse.")
        arquivos_ignorados += 1
    except Exception as e:
        # Uma melhoria aqui: tratar o erro específico se o arquivo já existe no destino
        if isinstance(e, shutil.Error) and "already exists" in str(e):
             print(f"Arquivo '{item_nome}' já existe no destino. Pulando.")
             arquivos_ignorados += 1
        else:
            print(f"Deu um erro inesperado ao processar '{item_nome}': {e}. Pulando esse.")
            arquivos_ignorados += 1


# --- Finalização ---
print("\n-----------------------------")
print("Faxina Concluída! (Com direito a janela de seleção e tudo)")
print(f"Arquivos movidos: {arquivos_movidos}")
print(f"Itens ignorados (pastas, erros, duplicados ou cancelados): {arquivos_ignorados}")
print("Confere lá se a 'praticidade' funcionou, rod.")
print("-----------------------------")

# Garante que a janela do tkinter (mesmo escondida) seja fechada corretamente
root.destroy()