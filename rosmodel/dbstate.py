import os, os.path
import sys
import django

def main():
    print('*** dbstate ***')
    print('This file', __file__)
    print('Hi from rosmodel dbstate working from', os.getcwd(), '.')
    #for pt in sys.path:
    #    print(pt)
    print()
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rosmodel.settings')
    django.setup()
    
    from rosmodel import settings
    print('Database:')
    print(os.path.abspath(settings.DATABASES['default']['NAME']))
    print()
    
    from state.models import Happening
    h = Happening(description="Created from dbstate.py")
    h.save()
    
    for hap in Happening.objects.all():
        print(hap)


if __name__ == '__main__':
    main()
