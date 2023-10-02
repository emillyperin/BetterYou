# BetterYou

**Descrição**: O projeto "Better You" é uma aplicação web que permite aos usuários registrar e acompanhar seus hábitos diários. Ele inclui as seguintes funcionalidades:

Registro de Hábitos: Os usuários podem adicionar novos hábitos à sua lista, fornecendo um nome do hábito desejado.

Visualização de Dados: A aplicação permite aos usuários visualizar a tarefa completa.

**Estrutura do Código**: O código Python utiliza o framework Flask e SQLAlchemy para criar a aplicação web e gerenciar o banco de dados. Ele define dois modelos de banco de dados: Habits (Hábitos) e Completions (Completos), que representam os hábitos registrados e as datas em que foram concluídos, respectivamente.

O código inclui rotas para a página inicial, a página de adicionar hábitos e uma rota para marcar hábitos como concluídos. Além disso, ele inicializa o banco de dados SQLite e inicia a aplicação Flask em modo de depuração.

## Pré-requisitos

- Python 3.7 ou superior
- Biblioteca SQLAlchemy e Flask

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

**Título:** Registro de Hábitos

**Ator Principal:** Usuário

**Objetivo:** Adicionar um hábito na base de dados.

**Fluxo Básico:**

1. Na página inicial, o usuário visualiza uma lista de hábitos que ele já registrou anteriormente.

2. O usuário decide adicionar um novo hábito à sua lista e clica no botão "Adicionar Hábito".

3. O sistema redireciona o usuário para a página de adição de hábito.

4. O usuário preenche um campo de texto com a descrição do novo hábito que deseja adicionar. Ex.: 'Correr'.

6. Após preencher a descrição, o usuário clica no botão "Adicionar" para registrar o novo hábito.

7. O sistema processa a solicitação do usuário e adiciona o novo hábito à lista existente.

8. De volta à página inicial, o usuário visualiza agora o novo hábito adicionado à lista.

9. O usuário decide marcar um hábito como concluído para a data atual. Ele clica no botão correspondente ao hábito desejado.

10. O sistema registra a conclusão do hábito para a data atual e atualiza as informações na lista.

11. O usuário pode continuar a acompanhar e gerenciar seus hábitos diários, adicionando, marcando e marcando como concluídos.

**Pós-condições:**

- O usuário consegue acompanhar e gerenciar seus hábitos diários usando a aplicação "Better You".
- Os hábitos adicionados e as datas de conclusão são registrados e armazenados no banco de dados da aplicação.

Este caso de uso descreve a funcionalidade de adição de novos hábitos e a marcação de tarefas como concluídas utilizando da entrada de dados do usuário em integração de interface web com uma base de dados.
