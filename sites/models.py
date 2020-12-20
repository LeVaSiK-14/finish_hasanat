from django.db import models

class News(models.Model):
	title = models.CharField(max_length=128)
	sub_title = models.CharField(max_length=2048)
	img = models.ImageField(upload_to='News_images/')

	def __str__(self):
		return self.title

class Projects(models.Model):
	title = models.CharField(max_length=128)
	sub_title = models.CharField(max_length=2048)
	img = models.ImageField(upload_to='Projects_images/')

	def __str__(self):
		return self.title

class Calculate(models.Model):
	name = models.CharField('Имя',max_length = 255)
	email = models.EmailField('Почта')
	phone_num = models.CharField('Номер телефона', max_length = 255)
	comment_text = models.TextField('Комментарий')

	def __str__(self):
		return self.name