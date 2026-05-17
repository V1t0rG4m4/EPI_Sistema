# EPI Manager — Sistema de Gestão de Equipamentos de Proteção Individual

Sistema web desenvolvido em Python com o framework Django para controle de empréstimo e devolução de Equipamentos de Proteção Individual (EPI), em conformidade com a NR-6 do Ministério do Trabalho e Emprego.

---

## Etapas do Projeto

| Etapa | Escopo | Situação |
|-------|--------|----------|
| Etapa 1 | Tela Base, Cadastro de Colaboradores, Cadastro de Equipamentos | Concluída |
| Etapa 2 | Tela de Empréstimo, Relatórios com filtros AND, Atualização de Status | Concluída |

---

## Funcionalidades

**Colaboradores** — Cadastro completo com nome, matrícula, cargo, setor, telefone e e-mail. Suporte a pesquisa por nome, edição e exclusão com modal de confirmação. Mensagens de sucesso ou falha a cada operação.

**Equipamentos (EPI)** — Cadastro com código identificador, Certificado de Aprovação (CA), quantidade em estoque e descrição técnica. Operações completas de criação, leitura, atualização e exclusão, com mensagens de feedback.

**Controle de Empréstimos (Etapa 2)** — Registro de entrega de EPI por colaborador, com datas de entrega e devolução prevista. A data prevista para devolução é validada tanto no front-end (JavaScript) quanto no back-end (`forms.py`) para garantir que seja sempre posterior ao momento atual e à data de entrega.

**Atualização de Status (Etapa 2)** — O técnico pode atualizar o status de cada empréstimo. Os campos Colaborador, Equipamento, Data do Empréstimo e Data Prevista de Devolução são exibidos como somente leitura, conforme requisito. Os campos Data de Devolução e Observação só aparecem quando o status selecionado é Devolvido, Danificado ou Perdido.

**Relatórios (Etapa 2)** — Tela de listagem histórica de todos os empréstimos (ativos, devolvidos, danificados etc.), com filtro combinado do tipo AND por nome do colaborador, nome do equipamento e status. Como exemplo prático: filtrar por colaborador e status "Emprestado" exibe apenas os EPIs que esse colaborador ainda não devolveu.

**Status disponíveis no cadastro** — Apenas Emprestado e Fornecido. Os status Devolvido, Danificado e Perdido ficam ocultos no formulário de cadastro e só aparecem na tela de edição.

**Dashboard** — Painel inicial com totais em tempo real: colaboradores, equipamentos, empréstimos ativos, fornecidos, devolvidos e danificados.

**Painel Administrativo** — Interface administrativa completa gerada automaticamente pelo Django, acessível em `/admin/`.

---

## Tecnologias Utilizadas

| Camada       | Tecnologia                                          |
|--------------|-----------------------------------------------------|
| Framework    | Django 5.x                                          |
| Banco        | SQLite (padrão Django)                              |
| ORM          | Django ORM com Migrations                           |
| Formulários  | Django ModelForm com validação customizada (`clean()`) |
| Templates    | Django Template Language (DTL)                      |
| Frontend     | Bootstrap 5 e Bootstrap Icons                       |

---

## Estrutura do Projeto

```
epi_django/
├── manage.py
├── requirements.txt
├── .gitignore
├── epi_django/                       <- Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/                             <- Aplicação principal
    ├── models.py                     <- Modelos: Colaborador, Equipamento, Emprestimo
    ├── views.py                      <- Lógica de cada tela
    ├── forms.py                      <- Formulários com validação nativa e customizada
    ├── urls.py                       <- Roteamento interno da aplicação
    ├── admin.py                      <- Configuração do painel administrativo
    ├── migrations/                   <- Histórico de alterações no banco de dados
    ├── static/core/css/              <- Folha de estilos personalizada
    └── templates/core/               <- Templates HTML
        ├── base.html                 <- Template base com menu lateral e topbar
        ├── index.html                <- Dashboard
        ├── confirmar_exclusao.html
        ├── colaboradores/
        │   ├── form.html             <- Cadastro e edição
        │   └── lista.html            <- Listagem com pesquisa por nome
        ├── equipamentos/
        │   ├── form.html
        │   └── lista.html
        └── emprestimos/
            ├── form.html             <- Cadastro com validação de datas (Etapa 2)
            ├── editar.html           <- Atualização de status (Etapa 2)
            └── lista.html            <- Relatórios com filtros AND (Etapa 2)
```

---

## Como Executar Localmente

Pré-requisito: Python 3.10 ou superior instalado na máquina.

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

| URL | Tela |
|-----|------|
| http://127.0.0.1:8000 | Dashboard |
| http://127.0.0.1:8000/colaboradores/ | Listagem de colaboradores |
| http://127.0.0.1:8000/equipamentos/ | Listagem de equipamentos |
| http://127.0.0.1:8000/emprestimos/ | Relatórios de empréstimos |
| http://127.0.0.1:8000/emprestimos/novo/ | Novo empréstimo |
| http://127.0.0.1:8000/admin/ | Painel administrativo |

---

## Status dos Empréstimos

| Status      | Disponível no Cadastro | Disponível na Edição | Descrição |
|-------------|:---:|:---:|------------------------------------------------|
| Emprestado  | Sim | Sim | EPI entregue temporariamente ao colaborador    |
| Fornecido   | Sim | Sim | EPI entregue em caráter definitivo             |
| Devolvido   | Nao | Sim | EPI retornado ao estoque em boas condições     |
| Danificado  | Nao | Sim | EPI retornado com avarias                      |
| Perdido     | Nao | Sim | EPI não localizado ou extraviado               |

---

## Modelo de Dados

O sistema possui três tabelas relacionadas entre si por chaves estrangeiras, atendendo ao requisito de integridade relacional da Etapa 2.

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
            colaborador_id (FK -> colaboradores.id)
            equipamento_id (FK -> equipamentos.id)
            data_emprestimo
            data_prevista_devolucao   <- deve ser > agora (validado)
            data_devolucao            <- nullable, preenchido na edição
            status                    <- Emprestado | Fornecido | Devolvido | Danificado | Perdido
            observacao_devolucao
            criado_em
```

---

## Validações Implementadas (Etapa 2)

A validação da data prevista para devolução ocorre em duas camadas independentes, o que garante robustez mesmo que uma delas seja contornada.

No front-end, ao submeter o formulário de cadastro, o JavaScript verifica o campo `data_prevista_devolucao` contra o horário atual do navegador. Se a data for inválida, o envio é bloqueado imediatamente e o campo recebe destaque visual, sem necessidade de round-trip ao servidor.

No back-end, independentemente do JavaScript, o servidor executa o método `clean()` do `EmprestimoCadastroForm` e valida que a data prevista é posterior tanto ao momento atual (`timezone.now()`) quanto à data de entrega informada. Os erros são vinculados diretamente ao campo correspondente e renderizados pelo template ao lado do input, seguindo o padrão nativo do Django.

---

## Referência Normativa

Este sistema foi desenvolvido para auxiliar o cumprimento da **NR-6 — Equipamentos de Proteção Individual**, que regulamenta a obrigatoriedade de fornecimento, registro e controle de EPIs por parte do empregador.

---

## Autor

Desenvolvido por **Vitor Gama** como projeto prático do curso de Desenvolvimento de Sistemas — SENAI.
