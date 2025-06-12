# 🤖 LinkedIn Recruiter Bot com Selenium

Este projeto é um bot criado com Python e Selenium que automatiza conexões no LinkedIn com **Tech Recruiters**, com o objetivo de:

- Bombardear meu feed com **vagas da área tech**, especialmente Python.
- Tornar meu perfil mais **visível para recrutadores** da área.
- Explorar na prática conceitos de **RPA (Robotic Process Automation)**.

---

## 📌 O que o bot faz?

1. Acessa o LinkedIn via navegador automatizado.
2. Busca por **Tech Recruiters** usando a barra de pesquisa.
3. Filtra os resultados por pessoas.
4. Envia solicitações de conexão automaticamente.
5. Repete o processo com diferentes termos ou filtros, conforme programado.

---

## 🚀 Tecnologias usadas

- [Python 3.x](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [WebDriver (ChromeDriver)](https://chromedriver.chromium.org/)
- [time, os, dotenv] (para controle e organização)

---

## 🛠️ Pré-requisitos

- Conta no LinkedIn
- Google Chrome instalado
- ChromeDriver compatível com sua versão do navegador
- Python 3.x instalado

---

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/linkedin-recruiter-bot.git
cd linkedin-recruiter-bot

2.Instale as dependências:
pip install -r requirements.txt

3.Vá ate o arquvi credencias.py e substitua por suas credencias de login do linkedin

4.Execute o script:
python app.py
