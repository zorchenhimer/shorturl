from django.core.management.base import BaseCommand, CommandError
from shortener.models import Link
from django.utils import timezone
#import datetime

class Command(BaseCommand):
    help = 'Deletes URLs older than 24 hours.'

    def handle(self, *args, **options):
        linklist = Link.objects.filter(create_time__lte=timezone.now() - timezone.timedelta(1))
        self.stdout.write('Found {n} links to delete.'.format(n=len(linklist)))
        for l in linklist:
            self.stdout.write('[{sn}] {ct}'.format(sn=l.short_name, ct=l.create_time))

        linklist.delete()

