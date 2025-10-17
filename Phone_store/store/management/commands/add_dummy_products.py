from django.core.management.base import BaseCommand
from store.models import Product
from django.core.files import File
from pathlib import Path
import os

class Command(BaseCommand):
    help = 'Populates the database with dummy products'

    def handle(self, *args, **kwargs):
        # Create dummy products
        products = [
            {
                'name': 'iPhone 15 Pro Max',
                'description': 'The most advanced iPhone ever with A17 Pro chip, titanium design, and advanced camera system.',
                'price': 144199.99,
                'category': 'iPhone',
                'stock': 50,
                'display_size': '6.7-inch Super Retina XDR OLED',
                'storage': '256GB',
                'ram': '8GB',
                'battery': '4422 mAh'
            },
            {
                'name': 'Samsung Galaxy S24 Ultra',
                'description': 'Experience the ultimate Android flagship with S Pen support and advanced AI features.',
                'price': 120699.99,
                'category': 'Samsung',
                'stock': 45,
                'display_size': '6.8-inch Dynamic AMOLED 2X',
                'storage': '512GB',
                'ram': '12GB',
                'battery': '5000 mAh'
            },
            {
                'name': 'Xiaomi 14 Pro',
                'description': 'Flagship performance with Leica optics and lightning-fast charging.',
                'price': 867999.99,
                'category': 'Xiaomi',
                'stock': 30,
                'display_size': '6.73-inch AMOLED',
                'storage': '256GB',
                'ram': '12GB',
                'battery': '4880 mAh'
            },
            {
                'name': 'iPhone 15',
                'description': 'The perfect balance of features and value with amazing camera capabilities.',
                'price': 790679.99,
                'category': 'iPhone',
                'stock': 60,
                'display_size': '6.1-inch Super Retina XDR OLED',
                'storage': '128GB',
                'ram': '6GB',
                'battery': '3877 mAh'
            },
            {
                'name': 'Samsung Galaxy S24+',
                'description': 'Premium Android experience with powerful performance and great battery life.',
                'price': 170099.99,
                'category': 'Samsung',
                'stock': 40,
                'display_size': '6.7-inch Dynamic AMOLED 2X',
                'storage': '256GB',
                'ram': '8GB',
                'battery': '4900 mAh'
            },
            {
                'name': 'Tecno Phantom X2 Pro',
                'description': 'Premium features at a competitive price with outstanding camera capabilities.',
                'price': 26699.99,
                'category': 'Tecno',
                'stock': 25,
                'display_size': '6.8-inch AMOLED',
                'storage': '256GB',
                'ram': '12GB',
                'battery': '5160 mAh'
            },
            {
                'name': 'Infinix Zero 40 Pro',
                'description': 'High-end features and premium design at an affordable price point.',
                'price': 30499.99,
                'category': 'Infinix',
                'stock': 35,
                'display_size': '6.67-inch AMOLED',
                'storage': '256GB',
                'ram': '8GB',
                'battery': '4600 mAh'
            },
            {
                'name': 'Xiaomi Redmi Note 13 Pro+',
                'description': 'Mid-range champion with flagship-level features and great value.',
                'price': 28399.99,
                'category': 'Xiaomi',
                'stock': 55,
                'display_size': '6.67-inch AMOLED',
                'storage': '128GB',
                'ram': '8GB',
                'battery': '5000 mAh'
            }
        ]

        for product_data in products:
            product = Product.objects.create(**product_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created product: {product.name}')
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated the database with dummy products')
        )