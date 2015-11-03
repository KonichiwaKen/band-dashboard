from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from authentication.models import Account
from members.models import BandMember
from members.serializers import BandMemberSerializer


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    band_member = BandMemberSerializer()

    class Meta:
        model = Account
        fields = ('id',
            'email',
            'created_at',
            'updated_at',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
            'band_member',)
        read_only_fields = ('created_at', 'updated_at',)

    def create(self, validated_data):
        band_member_data = validated_data.pop('band_member')
        account = Account.objects.create_user(**validated_data)
        BandMember.objects.create(account=account, **band_member_data)
        return account

    def update(self, instance, validated_data):
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

        update_session_auth_hash(self.context.get('request'), instance)
        return instance