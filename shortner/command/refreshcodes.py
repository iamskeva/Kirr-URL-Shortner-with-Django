from django.core.management.base import BaseCommand, CommandError
from shortner.models import  KirrURL

class Command(BaseCommand):
    help = 'Refreshes all KirrURL shortcodes'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcode()