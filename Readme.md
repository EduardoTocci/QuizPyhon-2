# Quiz com tema de Futebol
Este é um quiz um pouco mais trabalhado sobre futebol, desenvolvido em Python utilizando a biblioteca Tkinter para criar uma interface gráfica e SQLite para armazenar as respostas e o nome do usuário. O objetivo do quiz é testar o conhecimento dos jogadores sobre diversos temas relacionados ao futebol, como seleções, clubes e jogadores históricos.

# Funcionalidades
•Interface gráfica simples e intuitiva.
•Perguntas de múltipla escolha com 4 opções.
•Contagem de pontos automática.
•Exibição do resultado final ao terminar o quiz.
•Opção de jogar novamente com perguntas em ordem aleatória.
• Armazenamento de respostas e o nome em um banco de dados sendo mostrado no final

# Estrutura do Projeto
•quiz.py: Arquivo principal contendo as perguntas do quiz.
•interface.py: Arquivo principal contendo a lógica e a interface do quiz.
•Perguntas estão definidas como uma lista de dicionários, cada uma com sua pergunta, opções e resposta correta.
•Interface gráfica com botões para selecionar as respostas e exibir o resultado.


## Configuração do Banco de Dados

Este projeto utiliza SQLite como banco de dados. Para criar o banco de dados e as tabelas necessárias, você pode seguir os seguintes passos:

1. Crie um arquivo chamado `bd.py` no diretório principal do projeto com o seguinte conteúdo:

    ```python
    import sqlite3

    con = sqlite3.connect("quiz.db")

    cursor = con.cursor()

    # Criação da tabela "respostas"
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS respostas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        pergunta TEXT,
        resposta TEXT
    );
    """)

    con.commit()
    con.close()
    ```

2. Execute o script `bd.py` para criar o banco de dados localmente:

    ```bash
    python bd.py
    ```

   Isso criará um arquivo `quiz.db` no seu diretório local com a tabela `respostas`.

Agora o banco de dados está pronto para uso no projeto.