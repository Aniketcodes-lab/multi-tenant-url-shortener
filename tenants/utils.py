from .models import Tenant

def get_tenant_from_request(request):
    host = request.get_host().split(":")[0]

    try:
        tenant = Tenant.objects.get(domain=host)
    except Tenant.DoesNotExist:
        tenant = Tenant.objects.first()  # fallback for dev

    return tenant
