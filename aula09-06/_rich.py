from rich.console import Console
from rich.table import Table

console = Console()
tabela = Table(title="Produtos")
tabela.add_column("ID")
tabela.add_column("Nome")
tabela.add_column("Preço")

tabela.add_row("1", "Teclado", "R$150,00")
tabela.add_row("2", "Mouse", "R$80,00")

console.print(tabela)

