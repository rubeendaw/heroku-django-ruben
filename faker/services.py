from faker import Faker
from services.models import Service

fake = Faker()

for i in range(3):
    service = Service()

    service.slug = fake.slug()
    service.name_service = fake.name()
    service.type_service = "Music"
    service.price = 1

    service.save()