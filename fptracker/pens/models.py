from django.db import models
from django.forms import ModelForm
from django.forms.widgets import TextInput
# Create your models here.

NIBS_SIZES =(
    ('B' , 'Broad'),
    ('M' , 'Medium'),
    ('F' , 'Fine'),
    ('E' , 'Extra Fine')
)


class Pens(models.Model):
    modelName = models.CharField(max_length = 100)
    brandName = models.CharField(max_length = 100)
    color = models.CharField(max_length = 7)
    nibsSizes= models.CharField(max_length = 2 , choices = NIBS_SIZES)
    datePurchases  = models.DateField()


    def __str__(self):
        return self.color + " " + self.brandName + " " + self.modelName


class PenForm(ModelForm):
    class Meta:
        model = Pens
        fields= '__all__'
        widgets= {
            'color' : TextInput(attrs={'type' : 'color'})
        }
    
    