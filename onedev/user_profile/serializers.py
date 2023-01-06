from rest_framework import serializers

from utils.calculations import calculate_age


class ProfileSerializer(serializers.Serializer): # noqa
    avatar = serializers.ImageField(
        required=False
    )
    username = serializers.CharField(
        required=False
    )
    email = serializers.EmailField(
        required=False
    )
    bio = serializers.CharField(
        required=False
    )
    birth_date = serializers.DateField(
        required=False
    )

    age = serializers.SerializerMethodField()

    def get_age(self, obj): # noqa
        return calculate_age(obj.birth_date)

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()
        return instance
