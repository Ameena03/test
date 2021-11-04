from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files import File


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    image = models.ImageField(default='default.png', upload_to="profile_img",)
    bio = models.TextField(max_length=300, null=True, blank=True)
    cover = models.ImageField(default='background.jpg',upload_to="cover_img",)

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    name = models.TextField(max_length=200)
    slug = models.SlugField(max_length=40)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


YEAR_CHOICES = [
    ('2550', '2550'),
    ('2551', '2551'),
    ('2552', '2552'),
    ('2553', '2553'),
    ('2554', '2554'),
    ('2555', '2555'),
    ('2556', '2556'),
    ('2557', '2557'),
    ('2558', '2558'),
    ('2559', '2559'),
    ('2560', '2560'),
    ('2561', '2561'),
    ('2562', '2562'),
    ('2563', '2563'),
    ('2564', '2564'),
]

class Project(models.Model):
    p_name = models.TextField(max_length=500)
    p_author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    p_date = models.CharField(
        max_length = 20,
        choices = YEAR_CHOICES,
        )
    p_type = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='categories' )
    p_abstract = models.TextField(max_length=2000)
    p_img = models.ImageField(null=True, blank=True)
    f_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    count_download = models.IntegerField(default=0, verbose_name=('count download'),null=True,blank=True)

