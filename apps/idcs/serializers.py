from rest_framework import serializers


class IdcSerializer(serializers.Serializer):
    """
    IDC序列化类
    """
    id = serializers.IntegerField()
    name = serializers.CharField("IDC名称", required=True)
    address = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    person = serializers.CharField("联系人", required=True)

    class create():
        pass

