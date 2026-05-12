from pathlib import Path

from pytubefix import YouTube
from pytubefix.cli import on_progress

print("Bem-vindo ao downloader de vídeos do YouTube!")
#garante a execução do while para baixar o vídeo pelo menos uma vez.
baixar_outro = "sim"

#laço de repetição caso o usuário queira baixar outro vídeo.
while baixar_outro == "sim" :

    #solicita a URL do vídeo do YouTube que o usuário deseja baixar.
    url = input("Digite a URL do vídeo do YouTube: ")

    #cria um objeto YouTube usando a URL fornecida e define a função de callback para mostrar o progresso do download.
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    confirmar_download = input("Deseja baixar este vídeo? (sim/não): ").strip().lower()

    #verifica se o usuário confirmou o download do vídeo.
    if confirmar_download == "sim":
        #solicita ao usuário o nome ou caminho da pasta para salvar o vídeo.
        while True:
            pasta = input(
                "Digite o nome ou caminho da pasta para salvar o vídeo "
                "(ex.: Downloads, ~/Vídeos ou caminho completo): "
            ).strip()
            if pasta:
                break
            print("Informe uma pasta.")

        #cria o objeto Path para o destino da pasta e garante que a pasta existe.
        destino = Path(pasta).expanduser().resolve()
        destino.mkdir(parents=True, exist_ok=True)

        #obtém a melhor resolução disponível e inicia o download que será guardado na pasta escolhida pelo usuário.
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=str(destino)) # type: ignore
        print("Download concluído!")

    #caso o usuário não confirme o download do vídeo, o programa informa que o download foi cancelado.
    else:
        print("Download canceled.")
    
    baixar_outro = input("Quer baixar outro vídeo? (sim/não): ").strip().lower()

print("Obrigado por usar o downloader de vídeos do YouTube! Até a próxima!")