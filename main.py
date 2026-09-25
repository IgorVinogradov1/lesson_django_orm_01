import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard

if __name__ == '__main__':
    # load_dotenv()
    # adress_db = os.getenv('HOST')
    # password_db = os.getenv('PASSWORD')
    # secret_key = os.getenv('SECRET_KEY')
    
    active_passcards = Passcard.objects.filter(is_active=True)
    print('Всего пропусков', Passcard.objects.count())
    print('Активных пропусков', len(active_passcards))