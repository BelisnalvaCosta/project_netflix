from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Create a new token...'
    def add_arguments(self, parser):
                      parser.add_arguments('--username', requerid=True)
                      parser.add_arguments('--password', requerid=True)

    def handle(self, *args, **options):
            username = options['username']
            password = options['password']
            self.stdout.write(                    
                    self.style.WARNING(f'Creating user...')
            )
            
            user = User(username=username)
            user.first_name = username
            user.set_password(password)
            user.save()
            self.stdout.write(                    
                    self.style.SUCCESS(f'User created!')
            )

            self.stdout.write(                    
                    self.style.WARNING(f'Creating a new token...')
            )

            token = Token.objects.create(user=user)
            self.stdout.write(                    
                    self.style.SUCCESS(f'Token created: {token.key}')
            )