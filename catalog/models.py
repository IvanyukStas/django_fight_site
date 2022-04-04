from django.db import models

# Create your models here.
from django.urls import reverse


class Fighter(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter the first name of figther', null=True, blank=True)
    nick_name = models.CharField(max_length=50, help_text='Enter the nick name of figther', null=True, blank=True)
    last_name = models.CharField(max_length=50, help_text='Enter the last name of figther', null=True, blank=True)
    date_of_birth = models.DateField()
    height = models.CharField(max_length=10, help_text='Enter the height of figther', null=True, blank=True)
    wieght = models.CharField(max_length=10, help_text='Enter the wieght of figther', null=True, blank=True)


    class Meta:
        ordering = ['-first_name']


    def display_record(self):
        a = Record.objects.get(id=self.id)
        return a
    display_record.short_description = 'Record'


    def get_absolute_url(self):
        return reverse('fighter-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Record(models.Model):
    wins = models.IntegerField(null=True, blank=True)
    losses = models.IntegerField(null=True, blank=True)
    draws = models.IntegerField(null=True, blank=True)
    fighter_id = models.ForeignKey('Fighter', on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['-wins', '-losses']




    def __str__(self):
        return f'{self.wins} - {self.losses} - {self.draws}'


