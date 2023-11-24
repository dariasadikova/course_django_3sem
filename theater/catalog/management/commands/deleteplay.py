from typing import Any 
from django.core.management.base import BaseCommand, CommandError 
from catalog.models import Play  
 
class Command(BaseCommand): 
    help = "Last created play in database" 
 
    def handle(self, *args, **options): 
        try: 
            play = Play.objects.latest('id') 
        except: 
            raise CommandError('No plays in the database') 
        play.delete() 
 
        self.stdout.write(self.style.SUCCESS('Successfully deleted last play'))
