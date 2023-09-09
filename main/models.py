from django.db import models

# Create your models here.


class Config(models.Model):
    logo = models.FileField(upload_to='images/logo/', null=True, blank=True)
    after_logo_text = models.CharField(max_length=256, null=True, blank=True)
    text1 = models.CharField(max_length=256, default="Better Solutions For Your Business")
    text2 = models.CharField(max_length=256, default="We are team of talented designers making websites with Bootstrap")
    image1 = models.FileField(upload_to='images/hero/')

    text3 = models.CharField(max_length=256, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ")
    text4 = models.CharField(max_length=256, default="Ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. ")
    texts1 = models.TextField(default="""Ullamco laboris nisi ut aliquip ex ea commodo consequat
Duis aute irure dolor in reprehenderit in voluptate velit
Ullamco laboris nisi ut aliquip ex ea commodo consequat""")
    image2 = models.FileField(upload_to='images/about/')
    text5 = models.CharField(max_length=256, default="Voluptatem dignissimos provident quasi corporis voluptates")
    text6 = models.CharField(max_length=256, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ")

    text7 = models.CharField(max_length=256, default="Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.")

    text8 = models.CharField(max_length=256, default="Call To Action")
    text9 = models.CharField(max_length=256, default="Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    link1 = models.CharField(max_length=256, default="tel:226")

    text10 = models.CharField(max_length=256, default="Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.")

    text11 = models.CharField(max_length=256, default="Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.")

    text12 = models.CharField(max_length=256, default="Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.")

    text13 = models.CharField(max_length=256, default="Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.")

    location1 = models.CharField(max_length=256, default="Adijon viloyati, Paxtaobod tumani, 23 uy")
    email1 = models.CharField(max_length=256, default="info@infinite-co.uz")
    call1 = models.CharField(max_length=256, default="+1 99999999999999999")
    lat_lon1 = models.CharField(max_length=256, default="http://googlmap.com")

    text14 = models.TextField(max_length=256, default="""Paxtaobod tumani 360-uy
Andijon viloyati
O'zbekiston
""")
    
    text15 = models.CharField(max_length=256, default="Cras fermentum odio eu feugiat lide par naso tierra videa magna derita valies")

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Categories(models.Model):
    title = models.CharField(max_length=64)
    data_filter = models.CharField(max_length=64)

    def __str__(self):
        return self.data_filter

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='portfolio_images/')
    description = models.TextField(default="Infinite Co tomonidan yaratildi")
    url = models.CharField(max_length=1000)
    about = models.TextField(default='Portfolio haqida')
    filter_text = models.CharField(max_length=256, choices=(('filter-website', 'Website'), ('filter-telegram-bot', 'Telegram bot'), ('filter-automation', 'Automation'), ('filter-desktop', 'Desktop')), blank=True, null=True)
    # filter_text = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='filter_text')

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=64)
    image = models.FileField(upload_to='team_images/')
    subject = models.CharField(max_length=64)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class SocialNetworks(models.Model):
    title = models.CharField(max_length=64)
    icon = models.CharField(max_length=64)
    url = models.CharField(max_length=64)

    def __str__(self):
        return self.title
class TeamNetwork(models.Model):
    team = models.ForeignKey(Team, models.CASCADE, related_name='team')
    icon = models.CharField(max_length=64, default='')
    url = models.CharField(max_length=64, default='')

class Partners(models.Model):
    image = models.FileField(upload_to='partners_images')
    title = models.CharField(max_length=64, default='')

    def __str__(self):
        return self.title

class Navbar(models.Model):
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Getstarted(models.Model):
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Statics(models.Model):
    direction = models.CharField(max_length=64)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return self.direction
    
class Services(models.Model):
    icon = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    data_aos_delay = models.IntegerField(default=0)    

    def __str__(self):
        return self.title

class Questions(models.Model):
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=512)
    data_aos_delay = models.IntegerField(default=0)
    faq_list = models.IntegerField(default=0)

    def __str__(self):
        return self.question
