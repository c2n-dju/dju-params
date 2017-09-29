from django.core.management.base import BaseCommand

from dju_params.models import StartLog

class Command(BaseCommand):
    help = "Return the GIT-SHA1 of the code along with the last site starting timestamp"

    def handle(self, *args, **options):
        q = StartLog.objects.latest('pk')
        print(q.gitsha1 + " " + q.timestart.isoformat())
