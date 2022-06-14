import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('--ofn',
                action='store', dest='ofn',default='django-cli-out.pdf',
                help='filename to store the result')
        parser.add_argument('--odir',
                action='store', dest='odir',default=None,
                help='directory to store the result, default is in the project/noddy/out dir')

    def handle(self, **options):
        verbosity = int(options['verbosity'])  #django gives us 0-3 in BaseCommand, 1 is default
        ofn = options['ofn'] or 'django-cli-out.pdf'
        odir = options['odir']
        if odir is None:
            from project import noddy
            odir = os.path.join(os.path.dirname(noddy.__file__),'out')
        from project.noddy.doc import generate
        generate(os.path.join(odir,ofn),verbosity)
