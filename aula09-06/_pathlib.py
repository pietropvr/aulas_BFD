from pathlib import Path

#Define o nome da nova pasta para "dados"
pasta = Path("exercicios")

#Cria a pasta "dados"
pasta.mkdir(exist_ok=True)

#Define um novo arquivo para ser criado dentro da pasta "dados" chamado "registro.txt"
arquivo = pasta / "README.txt"

#
arquivo.write_text("Sai fora curioso", encoding="utf-8")
print(arquivo.write_text)
