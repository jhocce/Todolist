from rest_framework import serializers
from .models import User
# from django.contrib.auth.models import User



class UserSerializers(serializers.Serializer):

	username = serializers.CharField(max_length=50)
	Email = serializers.EmailField()
	first_name = serializers.CharField(max_length=50)
	last_name = serializers.CharField(max_length=50)
	password = serializers.CharField(max_length=200)
	class Meta:
		model = User
		field = ('username', 'Email', 'first_name', 'last_name', 'email', 'password' )

	





# I'm using Django 1.11

# I have created a Form and using Class based view to create a record and save to database.

# Business/models.py

# class BusinessType(models.Model):
#     title = models.CharField(max_length=100)
#     created = models.DateTimeField('date created', auto_now_add=True)
#     modified = models.DateTimeField('last modified', auto_now=True)

#     class Meta:
#         db_table = 'business_types'

#     def __str__(self):
#         return self.title


# class Business(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
#     created = models.DateTimeField('date created', auto_now_add=True)
#     modified = models.DateTimeField('last modified', auto_now=True)

#     class Meta:
#         verbose_name = 'business'
#         verbose_name_plural = 'businesses'
#         db_table = 'businesses'

#     def __str__(self):
#         return self.name
# Business/Forms.py

# class BusinessForm(ModelForm):
#     class Meta:
#         model = Business
#         fields = ['user']
# Business/views.py

# class BusinessCreate(LoginRequiredMixin, CreateView):
#     model = Business
#     form = BusinessForm

#     def form_valid(self, form):
#         messages.success(self.request, 'form is valid')
#         form.instance.user = self.request.user
#         form.save()

#     def get_success_url(self):
#         messages.success(self.request, 'Business Added Successfully')
#         return reverse('business:list')