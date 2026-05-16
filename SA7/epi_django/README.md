# EPI Manager — Sistema de Gestão de Equipamentos de Proteção Individual

Sistema web desenvolvido em Python com o framework Django para controle de empréstimo e devolução de Equipamentos de Proteção Individual (EPI), em conformidade com a NR-6 do Ministério do Trabalho e Emprego.

---

## Funcionalidades

**Colaboradores** — Cadastro completo com nome, matrícula, cargo, setor, telefone e e-mail. Suporte a pesquisa por nome, edição e exclusão com modal de confirmação.

**Equipamentos (EPI)** — Cadastro com código identificador, Certificado de Aprovação (CA), quantidade em estoque e descrição técnica. Operações completas de criação, leitura, atualização e exclusão.

**Controle de Empréstimos** — Registro de entrega de EPI por colaborador, com datas de entrega e devolução prevista. Atualização de status com campos dinâmicos que aparecem conforme o contexto. Relatório com filtro combinado (AND) por colaborador, equipamento e status.

**Dashboard** — Painel inicial com totais em tempo real: colaboradores, equipamentos, empréstimos ativos, fornecidos, devolvidos e danificados.

**Painel Administrativo** — Interface administrativa completa gerada automaticamente pelo Django, acessível em `/admin/`.

---

## Tecnologias Utilizadas

| Camada       | Tecnologia                        |
|--------------|-----------------------------------|
| Framework    | Django 5.x                        |
| Banco        | SQLite (padrão Django)            |
| ORM          | Django ORM com Migrations         |
| Formulários  | Django ModelForm                  |
| Templates    | Django Template Language (DTL)    |
| Frontend     | Bootstrap 5 e Bootstrap Icons     |

---

## Estrutura do Projeto

```
epi_django/
├── manage.py
├── requirements.txt
├── .gitignore
├── epi_django/                    <- Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/                          <- Aplicação principal
    ├── models.py                  <- Modelos: Colaborador, Equipamento, Emprestimo
    ├── views.py                   <- Lógica de cada tela
    ├── forms.py                   <- Formulários com validação nativa
    ├── urls.py                    <- Roteamento interno da aplicação
    ├── admin.py                   <- Configuração do painel administrativo
    ├── migrations/                <- Histórico de alterações no banco de dados
    ├── static/core/css/           <- Folha de estilos personalizada
    └── templates/core/            <- Templates HTML
        ├── base.html              <- Template base com menu lateral e topbar
        ├── index.html             <- Dashboard
        ├── colaboradores/
        ├── equipamentos/
        └── emprestimos/
```

---

## Como Executar Localmente

Pre-requisito: Python 3.10 ou superior instalado na maquina.

**1. Clone o repositório**
```bash
git clone https://github.com/V1t0rG4m4/EPI_Sistema.git
cd EPI_Sistema
```

**2. Crie e ative um ambiente virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Execute as migrations para criar o banco de dados**
```bash
python manage.py migrate
```

**5. Crie um superusuário para acessar o painel administrativo**
```bash
python manage.py createsuperuser
```

**6. Inicie o servidor de desenvolvimento**
```bash
python manage.py runserver
```

**7. Acesse no navegador**

Sistema: http://127.0.0.1:8000

Painel admin: http://127.0.0.1:8000/admin/

---

## Status dos Empréstimos

| Status      | Descrição                                       |
|-------------|-------------------------------------------------|
| Emprestado  | EPI entregue temporariamente ao colaborador     |
| Fornecido   | EPI entregue em caráter definitivo              |
| Devolvido   | EPI retornado ao estoque em boas condições      |
| Danificado  | EPI retornado com avarias                       |
| Perdido     | EPI não localizado ou extraviado                |

---

## Modelo de Dados

O sistema possui três tabelas relacionadas entre si por chaves estrangeiras.

```
colaboradores               equipamentos
─────────────               ────────────
id (PK)                     id (PK)
nome                        nome
matricula (UNIQUE)          codigo (UNIQUE)
cargo                       descricao
setor                       quantidade
telefone                    ca
email                       criado_em
criado_em
          \                /
            emprestimos
            ───────────
            id (PK)
            colaborador_id (FK)
            equipamento_id (FK)
            data_emprestimo
            data_prevista_devolucao
            data_devolucao
            status
            observacao_devolucao
            criado_em
```

---

## Referência Normativa

Este sistema foi desenvolvido para auxiliar o cumprimento da NR-6 — Equipamentos de Proteção Individual, que regulamenta a obrigatoriedade de fornecimento, registro e controle de EPIs por parte do empregador.

---

## Autor

Desenvolvido por Vítor Gama como projeto prático do curso de Análise e Desenvolvimento de Sistemas — SENAI.
