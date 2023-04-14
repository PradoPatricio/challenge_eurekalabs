from rest_framework import serializers

from .models import ApiUser


class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = ApiUser
        fields = ["email", "name", "last_name", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        user = ApiUser(
            email=self.validated_data["email"],
            name=self.validated_data["name"],
            last_name=self.validated_data["last_name"],
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        user.set_password(password)
        user.save()
        return user
