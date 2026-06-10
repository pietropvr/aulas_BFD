import random
import statistics as stats

valores = [random.randint(1, 100) for _ in range(20)]
print(f"Valores: {valores}")
print(f"Média: {stats.mean(valores):.2f}")
print(f"Mediana: {stats.median(valores)}")
