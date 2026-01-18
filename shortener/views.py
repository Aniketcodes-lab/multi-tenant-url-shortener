from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect, get_object_or_404

from .models import ShortURL
from .utils import generate_code
from tenants.utils import get_tenant_from_request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny


@method_decorator(csrf_exempt, name='dispatch')
class ShortenURLView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    def post(self, request):
        tenant = get_tenant_from_request(request)

        original_url = request.data.get("url")
        if not original_url:
            return Response({"error": "url is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate unique code per tenant
        code = generate_code()
        while ShortURL.objects.filter(tenant=tenant, short_code=code).exists():
            code = generate_code()

        short = ShortURL.objects.create(
            tenant=tenant,
            original_url=original_url,
            short_code=code
        )

        short_url = f"http://{request.get_host()}/{code}"

        return Response({
            "short_url": short_url,
            "code": code,
            "original_url": original_url
        })


def redirect_view(request, code):
    tenant = get_tenant_from_request(request)

    short = get_object_or_404(ShortURL, tenant=tenant, short_code=code)

    short.clicks += 1
    short.save(update_fields=["clicks"])

    return redirect(short.original_url)

def home_view(request):
    tenant = get_tenant_from_request(request)

    return render(request, "shortener/home.html", {
        "tenant": tenant
    })
