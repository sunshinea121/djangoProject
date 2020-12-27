from rest_framework import serializers


class NetworkSerializer(serializers.Serializer):
    """
    网卡序列化
    """

    def create(self, validated_data):
        """
        根据提供得验证过的数据创建并返回一个新的Snippet实例
        :param validated_data:
        :return:
        """
        # return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        根据提供得验证过得数据更新和返回一个已经存在得Snippet实例
        :param instance:
        :param validated_data:
        :return:
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
