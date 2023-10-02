# BetterYou


**Descrição**: O projeto "Better You" é uma aplicação web que permite aos usuários registrar e acompanhar seus hábitos diários. Ele inclui as seguintes funcionalidades:

Registro de Hábitos: Os usuários podem adicionar novos hábitos à sua lista, fornecendo uma descrição do hábito desejado.

Acompanhamento de Hábitos: Os usuários podem marcar seus hábitos como concluídos em datas específicas, acompanhando seu progresso ao longo do tempo.

Visualização de Dados: A aplicação permite aos usuários visualizar seus hábitos registrados e as datas em que foram concluídos.

**Estrutura do Código**: O código Python utiliza o framework Flask e SQLAlchemy para criar a aplicação web e gerenciar o banco de dados. Ele define dois modelos de banco de dados: Habits (Hábitos) e Completions (Completos), que representam os hábitos registrados e as datas em que foram concluídos, respectivamente.

O código inclui rotas para a página inicial, a página de adicionar hábitos e uma rota para marcar hábitos como concluídos. Além disso, ele inicializa o banco de dados SQLite e inicia a aplicação Flask em modo de depuração.

## Pré-requisitos

- Python 3.7 ou superior
- Biblioteca SQLAlchemy e Flasck

## Instalação

Bibliotecas:

```bash
pip install SQLAlchemy
```

```bash
pip install flask
```


## Uso

Abrindo o terminal no diretório correspondente:

```python
python app.py
```

## Caso de uso

**Título:** Acompanhamento de Hábitos

**Ator Principal:** Usuário

**Objetivo:** Acompanhar e gerenciar hábitos diários usando a aplicação "Better You".

**Pré-condições:**
- O usuário possui uma conta registrada na aplicação "Better You".
- O usuário está autenticado na aplicação.

**Fluxo Básico:**

1. O usuário acessa a aplicação "Better You" após fazer o login.

2. Na página inicial, o usuário visualiza uma lista de hábitos que ele já registrou anteriormente.

3. O usuário decide adicionar um novo hábito à sua lista e clica no botão "Adicionar Hábito".

4. O sistema redireciona o usuário para a página de adição de hábito.

5. O usuário preenche um campo de texto com a descrição do novo hábito que deseja adicionar.

6. Após preencher a descrição, o usuário clica no botão "Adicionar" para registrar o novo hábito.

7. O sistema processa a solicitação do usuário e adiciona o novo hábito à lista existente.

8. De volta à página inicial, o usuário visualiza agora o novo hábito adicionado à lista.

9. O usuário decide marcar um hábito como concluído para a data atual. Ele clica no botão correspondente ao hábito desejado.

10. O sistema registra a conclusão do hábito para a data atual e atualiza as informações na lista.

11. O usuário pode continuar a acompanhar e gerenciar seus hábitos diários, adicionando, marcando como concluídos ou editando hábitos conforme necessário.

**Fluxo Alternativo:**

- No passo 6, se o usuário tentar adicionar um hábito sem preencher o campo de descrição, o sistema exibirá uma mensagem de erro solicitando que o campo seja preenchido.

**Pós-condições:**

- O usuário consegue acompanhar e gerenciar seus hábitos diários usando a aplicação "Better You".
- Os hábitos adicionados e as datas de conclusão são registrados e armazenados no banco de dados da aplicação.

Este caso de uso descreve como um usuário pode utilizar a aplicação "Better You" para acompanhar e gerenciar seus hábitos diários, incluindo a adição de novos hábitos e a marcação de hábitos como concluídos. Isso ajuda o usuário a manter o controle de suas metas e objetivos pessoais de forma eficaz.
