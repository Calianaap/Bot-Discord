# 🤖 Discord Registration Bot

Um bot do Discord desenvolvido em Python utilizando a biblioteca `discord.py`. O projeto automatiza o processo de cadastro de membros no servidor através de modais interativos, além de contar com sistemas de seleção de cargos e logs de administração.

---

## 🚀 Funcionalidades

* **Comando de Embed:** Envia uma mensagem em formato de Embed incentivando os usuários a se identificarem.
* **Cadastro via Modal:** Interface limpa e nativa do Discord para o usuário preencher suas informações.
* **Dropdown de Cargos (Select Menus):** Menu interativo para a administração gerenciar e atribuir cargos aos membros.
* **Logs do Sistema:** Canal dedicado para o monitoramento das ações administrativas.

---

## 🛠️ Tecnologias Utilizadas

* [Python 3.8+](https://www.python.org/)
* [Discord.py v2.0+](https://discordpy.readthedocs.io/en/stable/)
* [Python-dotenv](https://pypi.org/project/python-dotenv/) (Gerenciamento de variáveis de ambiente)

---

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
* Python instalado.
* Uma conta no Discord e um bot criado no [Discord Developer Portal](https://discord.com/developers/applications).

### ⚙️ Ativação das Intents (Obrigatório)
Para o correto funcionamento do bot, certifique-se de ativar as seguintes **Privileged Gateway Intents** na aba "Bot" do painel do desenvolvedor do Discord:
* `Presence Intent`
* `Server Members Intent` (Necessária para manipular membros)
* `Message Content Intent` (Necessária para ler comandos)

---

## 🔧 Configuração e Instalação

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio

   
