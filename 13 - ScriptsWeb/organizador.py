import os
import shutil

def organizar_pasta(pasta_origem):
    """
    Organiza arquivos em subpastas baseadas na extensão do arquivo.

    Args:
        pasta_origem (str): Caminho da pasta que será organizada.
    """
    if not os.path.isdir(pasta_origem):
        print(f"Erro: A pasta '{pasta_origem}' não existe ou não é um diretório válido.")
        return

    arquivos = os.listdir(pasta_origem)
    if not arquivos:
        print(f"A pasta '{pasta_origem}' está vazia. Nada a organizar.")
        return

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta_origem, arquivo)

        # Apenas arquivos (não diretórios)
        if os.path.isfile(caminho_arquivo):
            # Extrai a extensão (sem o ponto) e coloca em minúsculas
            extensao = arquivo.split('.')[-1].lower() if '.' in arquivo else "sem_extensao"

            # Cria pasta destino com o nome da extensão
            pasta_destino = os.path.join(pasta_origem, extensao)
            os.makedirs(pasta_destino, exist_ok=True)

            # Move o arquivo para a pasta destino
            destino_final = os.path.join(pasta_destino, arquivo)

            # Evita sobrescrever arquivos existentes
            if os.path.exists(destino_final):
                print(f"Aviso: O arquivo '{arquivo}' já existe na pasta '{extensao}'. Pulando.")
            else:
                shutil.move(caminho_arquivo, destino_final)
                print(f"Movido: {arquivo} -> {extensao}/")

    print(f"Organização concluída na pasta '{pasta_origem}'.")

if __name__ == "__main__":
    caminho = input("Informe o caminho da pasta que deseja organizar: ").strip()
    organizar_pasta(caminho)
