# from rest_framework import serializers
# from .models import *
# from django.contrib.auth.models import User
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','username','password','is_staff','is_superuser']
#         extra_kwargs = {'password':{'write_only':True, 'required':True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
# class StudentsSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     name = serializers.CharField(max_length=120)
#     surname = serializers.CharField(max_length=120)
#     status = serializers.CharField(max_length=120)
#     course = serializers.CharField(max_length=120)
#     class Meta:
#         model = Students
#         fields = ('id','name','surname','status','course')
#     def create(self, validated_data):
#         return Students.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.surname = validated_data.get('surname',instance.surname)
#         instance.status = validated_data.get('status',instance.status)
#         instance.course = validated_data.get('course',instance.course)
#         instance.save()
#         return instance
# # class StaffSerializer(serializers.Serializer):
# #     id = serializers.ReadOnlyField()
# #     title = serializers.CharField(max_length=120)
# #     description = serializers.CharField(max_length=120)
# #     photo = serializers.CharField(max_length=120)
# #     date = serializers.CharField(max_length=120)
# #     user = serializers.CharField(max_length=120)
# #     class Meta:
# #         model = Staff
# #         fields = ('id','title','description','photo','date','user')
# #     def create(self, validated_data):
# #         return Staff.objects.create(**validated_data)
# #     def update(self, instance, validated_data):
# #         instance.title = validated_data.get('title',instance.title)
# #         instance.description = validated_data.get('description',instance.description)
# #         instance.photo = validated_data.get('photo',instance.photo)
# #         instance.date = validated_data.get('date',instance.date)
# #         instance.user = validated_data.get('user',instance.user)
# #         instance.save()
# #         return instance
# class ProjectsSerializer(serializers.Serializer):
#     id = serializers.CharField()
#     name = serializers.CharField(max_length=120)
#     description = serializers.CharField(max_length=120)
#     isDone = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Projects.objects.create(**validated_data)