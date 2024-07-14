# plants/management/commands/seed_plants.py

from django.core.management.base import BaseCommand
from plants.models import Plant

class Command(BaseCommand):
    help = 'Seed the database with initial plant data'

    def handle(self, *args, **kwargs):
        plants = [
            {
                "name": "Aloe Vera",
                "description": "A succulent plant species of the genus Aloe.",
                "price": 10.99,
                "stock": 50,
                "image_url": "https://images.unsplash.com/photo-1644585949224-cbe48d2cc2d6?q=80&w=3037&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            },
            {
                "name": "Snake Plant",
                "description": "A species of flowering plant in the family Asparagaceae.",
                "price": 12.99,
                "stock": 30,
                "image_url": "https://images.unsplash.com/photo-1593482892290-f54927ae1bb6?q=80&w=3387&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            },
            {
                "name": "Spider Plant",
                "description": "A species of evergreen perennial flowering plant.",
                "price": 8.99,
                "stock": 45,
                "image_url": "https://images.unsplash.com/photo-1608161779298-f42256d2c58d?q=80&w=3474&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            }
        ]

        for plant_data in plants:
            Plant.objects.create(**plant_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with plant data.'))
