from faker import Faker
from rich.console import Console
from rich.table import Table

print("Iniciando o script...")

fake = Faker("pt_BR")
console = Console()

tabela = Table(title="Perfis de Usuários Brasileiros")
tabela.add_column("Nome", style="cyan", no_wrap=True)
tabela.add_column("E-mail", style="magenta")
tabela.add_column("Cidade", style="green")

print("Gerando os perfis...")

for i in range(5):
    nome = fake.name()
    email = fake.email()
    cidade = fake.city()
    tabela.add_row(nome, email, cidade)
    print(f"Perfil {i+1} gerado com sucesso!")

print("Exibindo a tabela:")
console.print(tabela)