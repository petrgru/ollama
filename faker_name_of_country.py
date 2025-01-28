from faker import Faker
fake = Faker('cs_CZ')  # Create a new instance of Faker for Czech locale

# Generate an array of 100 fake first names
names = [fake.first_name() for _ in range(100)]
print(names)

