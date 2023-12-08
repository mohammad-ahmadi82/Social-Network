from django.db                  import models
from django.contrib.auth.models import User
from django.db.models.signals   import post_save

class Relation(models.Model):
    from_user   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created     = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_user} following {self.to_user}'

class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    age     = models.PositiveSmallIntegerField(default=0)
    bio     = models.TextField(null=True, blank=True) 

def creat_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(receiver=creat_profile, sender=User)
 