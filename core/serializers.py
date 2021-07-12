from rest_framework import serializers

class CompanySafeRelatedField(serializers.HyperlinkedRelatedField):
    def get_queryset(self):
        request = self.context['request']
        company_id = request.user.company_id
        return super().get_queryset().filter(company_id=company_id)


class CompanySafeSerializerMixin(object):
    serializer_related_field = CompanySafeRelatedField
