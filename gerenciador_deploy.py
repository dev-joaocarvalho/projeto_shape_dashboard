"""Módulo responsável pela automação de deploy do dashboard no GitHub Pages."""

import subprocess
import sys
from datetime import datetime

# Constantes em SCREAMING_SNAKE_CASE
MENSAGEM_PADRAO = "Atualiza progresso de treino e dados do RU"
COMANDOS_GIT = {
    "adicionar": ["git", "add", "."],
    "enviar": ["git", "push"]
}


class GerenciadorRepositorio:
    """Classe responsável por encapsular as operações do repositório Git."""

    def __init__(self, mensagem_personalizada: str = "") -> None:
        """Inicializa o gerenciador com a mensagem de commit desejada.

        :param mensagem_personalizada: Texto que será adicionado ao commit.
        """
        self.mensagem_personalizada = mensagem_personalizada

    def gerar_mensagem_commit(self) -> str:
        """Gera a mensagem final do commit com a data e hora atuais.

        :return: String formatada com a mensagem e timestamp.
        """
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        base_mensagem = self.mensagem_personalizada or MENSAGEM_PADRAO
        return f"{base_mensagem} - [{data_atual}]"

    def executar_comando(self, comando: list[str]) -> None:
        """Executa um comando no terminal do sistema operacional.

        :param comando: Lista de strings representando o comando e argumentos.
        """
        try:
            subprocess.run(comando, check=True)
        except subprocess.CalledProcessError as erro:
            print(f"Erro fatal ao executar o comando {comando}: {erro}")
            sys.exit(1)

    def realizar_deploy(self) -> None:
        """Executa o fluxo completo de add, commit e push para o repositório."""
        mensagem_final = self.gerar_mensagem_commit()
        comando_commit = ["git", "commit", "-m", mensagem_final]

        print("Iniciando processo de deploy...")
        self.executar_comando(COMANDOS_GIT["adicionar"])
        self.executar_comando(comando_commit)
        self.executar_comando(COMANDOS_GIT["enviar"])
        print("✅ Deploy realizado com sucesso no GitHub!")


def iniciar_automacao() -> None:
    """Função principal que orquestra a execução do script."""
    print("--- GERENCIADOR DO SHAPE V-TAPER ---")
    nota_usuario = input("Digite a nota do commit (ou Enter para o padrão): ")

    gerenciador = GerenciadorRepositorio(mensagem_personalizada=nota_usuario)
    gerenciador.realizar_deploy()


if __name__ == "__main__":
    iniciar_automacao()
