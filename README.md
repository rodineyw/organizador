# Organizador de Pastas Automágico (com GUI) 📁✨🧹

## Descrição

Cansado da sua pasta de Downloads (ou qualquer outra) parecer uma zona de guerra digital? Este script Python está aqui para (tentar) salvar o dia!

Ele organiza automaticamente os arquivos em subpastas baseadas em suas extensões (tipo `.jpg`, `.pdf`, `.zip`), tornando mais fácil encontrar o que você precisa no meio da bagunça. Chega de rolar por uma lista infinita de arquivos aleatórios! A ferramenta utiliza uma interface gráfica simples (`tkinter`) para que você possa escolher a pasta alvo com um clique, em vez de digitar caminhos no terminal. Praticidade acima de tudo (ou quase).

**Aviso:** Use por sua conta e risco. Faça backup antes de usar pela primeira vez!

## Funcionalidades Principais ✨

* **Seleção de Pasta via GUI:** Interface gráfica (`tkinter`) para escolher a pasta que você quer organizar. Adeus, digitação de caminhos! 👋
* **Organização por Tipo:** Move arquivos para subpastas categorizadas (Imagens, Documentos, Vídeos, etc.).
* **Criação Automática de Pastas:** As pastas de categoria (`Imagens`, `Documentos`, etc.) são criadas automaticamente se não existirem.
* **Categorias Personalizáveis:** Edite facilmente o script para adicionar/remover categorias ou extensões de arquivo.
* **Pasta "Outros":** Arquivos com extensões desconhecidas ou sem extensão são movidos para uma pasta `Outros`, para que nada fique perdido (só menos organizado).
* **Feedback no Terminal:** Exibe mensagens sobre o progresso e o resultado da organização.

## Como Usar 🚀

1.  **Pré-requisitos:**
    * Ter o [Python 3](https://www.python.org/downloads/) instalado.
    * A biblioteca `tkinter` (geralmente já vem com o Python no Windows e em muitas distribuições Linux/Mac. Se não vier, pode ser necessário instalar `python3-tk` ou similar).

2.  **Baixar o Script:**
    * Clone este repositório: `git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git`
    * Ou baixe o arquivo `.py` diretamente.

3.  **Executar:**
    * Abra seu terminal ou prompt de comando.
    * Navegue até a pasta onde você salvou o script usando o comando `cd`.
    * Execute o script com o comando:
        ```bash
        python organizador.py
        ```
        (Substitua `nome_do_script.py` pelo nome real do arquivo, ex: `organizador_downloads_gui.py`).

4.  **Selecionar a Pasta:**
    * Uma janela do sistema operacional será aberta.
    * Navegue e selecione a pasta que deseja organizar.
    * Clique em "Selecionar Pasta" (ou botão similar).

5.  **Aguardar:**
    * O script processará os arquivos e os moverá para as subpastas apropriadas dentro da pasta que você selecionou. As mensagens de progresso aparecerão no terminal.

## Configuração e Personalização ⚙️

Você pode (e provavelmente vai querer) personalizar as categorias e as extensões de arquivo diretamente no código Python. Procure pela seção `categorias` no script:

```python
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
    # Adicione suas próprias categorias e extensões aqui!
    # Ex: "Planilhas": ['.xlsx', '.xls', '.ods', '.csv'],
    "Outros": [] # Deixe esta vazia para capturar o resto
}
