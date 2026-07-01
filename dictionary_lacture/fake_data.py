from faker import Faker
fake=Faker('en_IN')
print(fake.name())
print(fake.email())
print(fake.address())
print(fake.phone_number())
print(fake.text())