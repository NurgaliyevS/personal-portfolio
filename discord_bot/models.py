from django.db import models

class Discord_bot(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="discord_bot/images", default="C:/Users/constantion/Downloads/Telegram Desktop/photo_2022-01-13_08-56-10.jpg")
    # image = ResizedImageField (upload_to="discord_bot/images", blank=True, null=True)
    url = models.URLField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


# Create your models here.
