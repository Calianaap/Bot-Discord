import discord
from discord.ext import commands
from discord import ui
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
ID_CANAL_LOGS = int(os.getenv("ID_CANAL_LOGS"))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Sucesso! Conectado como: {bot.user.name}")


class SelectCargos(ui.Select):
    def __init__(self, membro_alvo: discord.Member, novo_nome: str):
        self.membro_alvo = membro_alvo
        self.novo_nome = novo_nome

        options = []

        guild = membro_alvo.guild

        for cargo in guild.roles[1:26]:
            if not cargo.managed:
                options.append(
                    discord.SelectOption(
                        label=cargo.name,
                        value=str(cargo.id)
                    )
                )

        super().__init__(
            placeholder="Selecione um cargo para o membro",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        cargo_id = int(self.values[0])
        cargo = interaction.guild.get_role(cargo_id)

        await self.membro_alvo.add_roles(cargo)
        await self.membro_alvo.edit(nick=self.novo_nome)

        await interaction.response.send_message(
            f"O membro {self.membro_alvo.mention} recebeu o cargo {cargo.name} "
            f"e teve seu nome alterado para {self.novo_nome}.",
            ephemeral=True
        )


class LogAdminView(ui.View):
    def __init__(self, membro_alvo: discord.Member, novo_nome: str):
        super().__init__()
        self.add_item(SelectCargos(membro_alvo, novo_nome))


class MeuModal(ui.Modal, title="Cadastro de Membros"):
    nome = ui.TextInput(
        label="Qual seu nome?",
        placeholder="Digite seu nome aqui"
    )

    id_usuario = ui.TextInput(
        label="Qual seu ID?",
        placeholder="Digite seu ID aqui"
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"Obrigado, {self.nome.value}! Sua ficha foi enviada para análise.",
            ephemeral=True
        )

        canal_logs = interaction.guild.get_channel(ID_CANAL_LOGS)

        if canal_logs:
            embed_log = discord.Embed(
                title="Novo Cadastro",
                description=f"Nome: {self.nome.value}\nID: {self.id_usuario.value}",
                color=discord.Color.blue()
            )

            await canal_logs.send(
                embed=embed_log,
                view=LogAdminView(interaction.user, self.nome.value)
            )


class CadastroView(ui.View):
    @ui.button(label="Fazer cadastro", style=discord.ButtonStyle.primary)
    async def abrir_modal(self, interaction: discord.Interaction, button: ui.Button):
        await interaction.response.send_modal(MeuModal())


@bot.command()
async def enviar_embed(ctx: commands.Context):
    minha_embed = discord.Embed(
        title="Cadastro",
        description="Precisamos que você se identifique!"
    )

    imagem = discord.File("imagens/Kymeraimag.png", filename="kymera.png")
    minha_embed.set_image(url="attachment://kymera.png")

    await ctx.reply(
        embed=minha_embed,
        file=imagem,
        view=CadastroView()
    )


bot.run(TOKEN)