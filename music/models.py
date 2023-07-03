from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Songs model.
class Song(models.Model):
    
    # Language choice List.
    language_Choice = (
        ('Devotional','Devotional'),
        ('Hindi','Hindi'),
        ('Punjabi','Punjabi'),
        ('Haryanvi','Haryanvi'),
        ('English','English')
    )
    
    name = models.CharField(max_length=250)
    album = models.CharField(max_length=250)
    language = models.CharField(max_length=50, choices=language_Choice, default='Hindi')    
    song_img = models.ImageField()
    year = models.IntegerField()
    singer = models.CharField(max_length=250)
    song_file = models.FileField()
    
    class Meta:
        app_label = 'music'
    
    def __str__(self):
        return self.name
    

# Songs playlist model.    
class Playlist(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Playlist_name = models.CharField(max_length=250)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Playlist_name    
        
        
# Favorite songs model.        
class Favorite(models.Model):
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)     
    is_fav = models.BooleanField(default=False)
    
# Recent songs model    
class Recent(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)    
       