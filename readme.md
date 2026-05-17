# Downloader de vídeo

## Descrição 
Esta uma aplicação desenvolvida em Python para o download de vídeos do Youtube. O objetivo desse projeto é para meu apredizado com a linguagem e suas bibliotecas. Portanto, para downloads oficiais utilize o própio Youtube para isso.

## Como funciona
O programa dará as boas vindas a você usuário e logo em seguida irá pedi-lo que digite a URL (link do vídeo). Então, ele fará uma verificação para conferir se a URL está correta ou se o vídeo existe no youtube e em seguida pedirá para confirmar o download e fará o download, na máxima qualidade disponível, ou não, dependendo da resposta. Por fim, o programa irá perguntar se o usuário deseja fazer o download de outro vídeo e fará o mesmo processo de antes caso o usuário diga que sim  

## 📁 Estrutura do Projeto
1. main.py              # Script principal de execução
2. requirements.txt     # Lista de dependências do projeto
3. .gitignore           # Arquivo para ignorar arquivos desnecessários (como o venv)
4. README.md            # Documentação do projeto

## 📦 Tecnologias Utilizadas
1. Python
2. Pathlib
3. Pytubefix

## 🛠️ Instalação e Configuração
Siga os passos abaixo para configurar o ambiente de desenvolvimento local:

```bash
#Clonar o repositório:
$ git clone [https://github.com/cauan-castro/Downloader-yt](https://github.com/seu-usuario/nome-do-repositorio.git)
  cd nome-do-repositorio
#Criar o ambiente virtual(venv):
$ python3 -m venv venv
```

### ative o ambiente virtual

No Linux/macOS:

```bash
$ source venv/bin/activate
```

No Windows:

```bash
$ .\\venv\\Scripts\\activate
```

## Instale as dependências
```bash
pip install -r requirements.txt
```

💻 Como Usar \
Com o ambiente virtual ativado, execute o script principal:

```Bash
python main.py
```

Siga as instruções que aparecerão no terminal para inserir a URL do vídeo e escolher as opções de download.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Feito com ❤️ por Cauã Castro
