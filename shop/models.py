from django.db import models
from account.models import User



class Gender(models.Model):
	GENDER_CHOICE = (
			('ma' , 'مرد'),
			('fe' , 'زن'),
		)

	gender = models.CharField(max_length=2, choices=GENDER_CHOICE, verbose_name='جنسیت' )


	def __str__(self):
		return self.gender


class Category(models.Model):
	title = models.CharField(max_length=30, verbose_name='عنوان')
	status = models.BooleanField(verbose_name='وضعیت انتشار', default=True)


	def __str__(self):
		return self.title


class Condition(models.Model):
	title = models.CharField(max_length=30, verbose_name='عنوان')
	status = models.BooleanField(verbose_name='وضعیت انتشار', default=True)


	def __str__(self):
		return self.title



class Product(models.Model):
	STATUS_CHOICE = (
			('p',"انتشار"),
        ('d',"پیش نویس"),
        ('l',"درحال برسی"),
        ('b',"برگشت داده شده"),
		)


	title = models.CharField(max_length=50, verbose_name='عنوان')
	slug = models.SlugField(max_length=20, null=True, unique=True, allow_unicode=True)
	gender = models.ManyToManyField(Gender ,verbose_name='جنسیت', )
	description = models.TextField(verbose_name='توضیحات')
	price = models.PositiveIntegerField(verbose_name='قیمت')
	image = models.ImageField(default=None, upload_to='images')
	created = models.DateTimeField(auto_now_add=True, verbose_name='زمان اجاد')
	status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name='وضعیت انتشار')
	condition = models.ManyToManyField(Condition, verbose_name='حالت')
	owner = models.ForeignKey(User, verbose_name='مالک', null=True, on_delete=models.SET_NULL)
	category = models.ManyToManyField(Category ,verbose_name='دسته بندی' )	


	def __str__(self):
		return self.title

