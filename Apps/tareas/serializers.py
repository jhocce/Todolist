from rest_framework import serializers
from .models import tarea
from Apps.user.serialisers import UserSerializers


class TareasSerializers(serializers.ModelSerializer):

	status = serializers.BooleandField()
	create = serializers.DateTimeField(auto_now_add=True)
	modifid = serializers.DateTimeField(auto_now=True)
	description = serializers.CharField(max_length=100)
	user = UserSerializers()


	class Meta:
		model = tarea
		field = ('status', 'create', 'description', 'user')


	