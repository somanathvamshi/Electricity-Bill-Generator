
from django.db import models  
from django.urls import reverse


class Details(models.Model):  
    COLOR_CHOICES = (
    ('telangana','Telangana'),
    ('delhi', 'Delhi'),
    ('goa','Goa'),
    ('kerala','Kerala'),
    
)
    first_name = models.CharField(max_length=50)  
    gender = models.CharField(max_length=40 )
    address = models.TextField()
    from_date = models.DateField()
    to_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(choices=COLOR_CHOICES,default='telangana',max_length=30)

   
    no_units = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='pictures')
    download_pdf = models.BooleanField("Do you want to download the pdf",default=False)
    class Meta:  
        db_table = "Details"  
    def get_absolute_url(self):
        return reverse('elc-detail', kwargs={'pk': self.pk})