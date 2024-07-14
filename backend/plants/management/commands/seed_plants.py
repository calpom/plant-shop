from django.core.management.base import BaseCommand
from plants.models import Plant

class Command(BaseCommand):
    help = 'Seed the database with initial plant data'

    def handle(self, *args, **kwargs):
        # Clear the existing data
        Plant.objects.all().delete()

        plants = [
            {
                "name": "Aloe Vera",
                "description": "Aloe Vera is a succulent plant species known for its medicinal properties and low maintenance. It thrives in bright, indirect sunlight and requires watering only when the soil is completely dry, making it drought-tolerant. Aloe Vera prefers a dry environment and does not require high humidity levels, making it an ideal houseplant for beginners.",
                "price": 10.99,
                "stock": 50,
                "image_url": "https://images.unsplash.com/photo-1644585949224-cbe48d2cc2d6?q=80&w=3037&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            },
            {
                "name": "Snake Plant",
                "description": "Snake Plant, also known as Sansevieria, is a hardy plant that can tolerate low light conditions but prefers bright, indirect light for optimal growth. It requires minimal watering, about once every two to three weeks, allowing the soil to dry out completely between waterings. This plant adapts well to low humidity environments, making it a versatile and resilient indoor plant.",
                "price": 12.99,
                "stock": 30,
                "image_url": "https://images.unsplash.com/photo-1593482892290-f54927ae1bb6?q=80&w=3387&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            },
            {
                "name": "Spider Plant",
                "description": "Spider Plant is a popular houseplant known for its arching leaves and spider-like offshoots. It thrives in bright, indirect light and should be watered moderately, keeping the soil slightly moist but not soggy. Spider Plants appreciate a humid environment but can tolerate average indoor humidity levels, making them an excellent choice for most homes.",
                "price": 8.99,
                "stock": 45,
                "image_url": "https://images.unsplash.com/photo-1608161779298-f42256d2c58d?q=80&w=3474&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            },
            {
                "name": "Jade Pothos",
                "description": "Jade Pothos is a hardy, trailing plant with vibrant green leaves. It grows well in low to bright indirect light and requires watering when the top inch of soil feels dry. Jade Pothos prefers higher humidity levels but can adapt to typical indoor conditions, making it a versatile and easy-care plant for any room.",
                "price": 9.99,
                "stock": 40,
                "image_url": "https://images.unsplash.com/photo-1537039557108-4a42c334fd5e?q=80&w=3024&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            },
            {
                "name": "Monstera Deliciosa",
                "description": "Monstera Deliciosa, also known as the Swiss Cheese Plant, is a tropical plant with large, fenestrated leaves. It thrives in bright, indirect light and requires regular watering, allowing the soil to dry out slightly between waterings. Monstera Deliciosa prefers a humid environment, so misting its leaves or placing it in a room with higher humidity levels will help it flourish.",
                "price": 15.99,
                "stock": 25,
                "image_url": "https://images.unsplash.com/photo-1525498128493-380d1990a112?q=80&w=3024&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            }
        ]

        for plant_data in plants:
            Plant.objects.create(**plant_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with plant data.'))
