import random
import statistics as stats
import json
from datetime import datetime
from pathlib import Path

pasta = Path("saida")
pasta.mkdir(exist_ok=True)

valores = [random.randint(1, 500) for _ in range(30)]
media = stats.mean(valores)
menor = min(valores)
maior = max(valores)


timestamp_arquivo = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
timestamp_json = datetime.now().isoformat()

print(f"Valores: {valores}")
print(f"Média: {media:.2f}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")


# 3. Estruturação dos dados para o JSON
dados_para_salvar = {
    "data_geracao": timestamp_json,
    "metricas": {
        "media": round(media, 2),
        "menor": menor,
        "maior": maior
    },
    "valores": valores
}

    # 4. Definição do nome do arquivo (dinâmico com a data e hora)
nome_arquivo = pasta / f"resultado_{timestamp_arquivo}.json"

# 5. Salvando o arquivo de fato
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    # indent=4 deixa o arquivo legível para humanos
    json.dump(dados_para_salvar, arquivo, indent=4, ensure_ascii=False)

print(f"\nDados salvos com sucesso em: {nome_arquivo}")