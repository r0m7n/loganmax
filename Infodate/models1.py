from django.db import models
from django.utils import timezone

class Infodate(models.Model):
STATUS_CHOICES1 = (
    ('новый', 'новый'),
    ('б/у', 'б/у'),
)

STATUS_CHOICES2 = (
    ('да', 'да'),
    ('нет', 'нет'),
)
author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
probeg_tek = models.CharField(max_length=8)
date_create = models.DateTimeField('Дата приобретения')
probeg_all = models.CharField(max_length=8)
date_publish = models.DateTimeField(auto_now_add=True)
conder = models.CharField(max_length=3, choices = STATUS_CHOICES1, default='да')
type_expl = models.CharField(max_length=5, choices = STATUS_CHOICES2, default='новый')
	
def publish(self):
    self.date_publish = timezone.now()
    self.save()

def _str_(self):
    return self.probeg_tek
    return self.probeg_all
    return self.conder
                                        
    
    
# Create your models here.
