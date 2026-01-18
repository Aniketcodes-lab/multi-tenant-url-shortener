from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_tenant_from_request

class BrandingView(APIView):
    def get(self, request):
        tenant = get_tenant_from_request(request)

        return Response({
            "app_name": tenant.app_name,
            "logo": tenant.logo.url if tenant.logo else None,
            "primary_color": tenant.primary_color,
            "name": tenant.name
        })
