# 🦺 EPI Manager — Sistema de Gestão de EPIs com Django

Sistema web desenvolvido em **Python + Django** para controle de empréstimo e devolução de Equipamentos de Proteção Individual (EPI), em conformidade com a **NR-6**.

---

## 📋 Funcionalidades

**Colaboradores** — CRUD completo com pesquisa por nome e modal de confirmação de exclusão.

**Equipamentos (EPI)** — Cadastro com código, Certificado de Aprovação (CA) e controle de estoque.

**Controle de Empréstimos** — Registro de entrega com status dinâmicos (Emprestado, Fornecido, Devolvido, Danificado, Perdido). Relatório com filtro AND por colaborador, equipamento e status.

**Dashboard** — Cards de resumo em tempo real com os totais de cada categoria.

**Painel Admin Django** — Interface administrativa completa gerada automaticamente pelo Django em `/admin/`.

---

## 🛠️ Tecnologias

| Camada      | Tecnologia                     |
|-------------|-------------------------------|
| Framework   | Django 5.x                    |
| Banco       | SQLite (padrão Django)        |
| ORM         | Django ORM + Migrations       |
| Formulários | Django Forms (ModelForm)      |
| Frontend    | Bootstrap 5 + Bootstrap Icons |
| Templates   | Django Template Language      |

---

## 🗂️ Estrutura do Projeto

```
epi_django/
├── manage.py
├── requirements.txt
├── .gitignore
├── epi_django/               ← Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/                     ← Aplicação principal
    ├── models.py             ← Colaborador, Equipamento, Emprestimo
    ├── views.py              ← Lógica de cada tela
    ├── forms.py              ← Formulários com validação
    ├── urls.py               ← Roteamento da app
    ├── admin.py              ← Configuração do painel admin
    ├── migrations/           ← Histórico do banco de dados
    ├── static/core/css/      ← Estilo personalizado
    └── templates/core/       ← Templates HTML
        ├── base.html
        ├── index.html
        ├── colaboradores/
        ├── equipamentos/
        └── emprestimos/
```

---

## 🚀 Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/V1t0rG4m4/EPI_Sistema.git
cd EPI_Sistema

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute as migrations (cria o banco de dados)
python manage.py migrate

# 5. Crie um superusuário para o admin (opcional)
python manage.py createsuperuser

# 6. Inicie o servidor
python manage.py runserver
```

Acesse em: **http://127.0.0.1:8000**
Painel admin: **http://127.0.0.1:8000/admin/**

---

## 📌 Diferenças em relação à versão Flask

| Aspecto        | Flask (versão anterior)       | Django (versão atual)              |
|----------------|-------------------------------|------------------------------------|
| Banco          | SQL manual com `sqlite3`      | ORM com `models.py` e migrations   |
| Formulários    | HTML manual + validação na view | `ModelForm` com validação nativa |
| Admin          | Não tinha                     | Painel completo em `/admin/`       |
| Rotas          | Decoradores `@app.route`      | `urls.py` centralizado por app     |
| Organização    | Arquivo único `app.py`        | Separação em models/views/forms    |

---

## 📚 Referência Normativa

Desenvolvido para auxiliar o cumprimento da **NR-6** — Equipamentos de Proteção Individual.

---

## 👨‍💻 Autor

Desenvolvido por **Vítor Gama** — Análise e Desenvolvimento de Sistemas, SENAI.
