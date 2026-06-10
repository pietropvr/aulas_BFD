from faker import Faker

fake = Faker("pt-BR")
for _ in range(3):
    print(f"{fake.name()} - {fake.email()}")