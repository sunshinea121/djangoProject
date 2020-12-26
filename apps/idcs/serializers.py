from rest_framework import serializers
from .models import Idcs, Cabinet


class IdcSerializer(serializers.Serializer):
    """
    IDC序列化类
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, required=True)
    address = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    # 外键
    person = serializers.CharField(max_length=30, required=True)

    def create(self, validated_data):
        """
        前期验证好的数据
        :param validated_data:
        :return:
        """
        return Idcs.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        修改数据
        :param instance: 数据库序列化的数据
        :param validated_data: 前段传过来的数据，经过反序列化验证好的数据
        :return:
        """
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.person = validated_data.get("person", instance.person)
        instance.save()
        return instance


