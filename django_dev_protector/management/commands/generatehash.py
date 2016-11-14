from django.core.management.base import BaseCommand, CommandError
from django_dev_protector.settings import PROTECT_HASH_FILE, DIR_NAME

def generate_hash():
    import random
    return '%032x' % random.getrandbits(128)


class Command(BaseCommand):
    help = 'Generates hash for django-dev-protector.'

    def handle(self, *args, **options):
        self.stdout.write('Generating random hash')
        r_hash = generate_hash()

        try:
            f = open(DIR_NAME + PROTECT_HASH_FILE, mode='w')
            f.write(r_hash)
            f.close()
            self.stdout.write('Saving... OK.')
            self.stdout.write('Save your hash code:')
            self.stdout.write(r_hash)
        except Exception as e:
            self.stdout.write('Saving... ERROR.')
            self.stdout.write(e)
