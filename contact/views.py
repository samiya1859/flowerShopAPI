from rest_framework import viewsets
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        send_mail(
            'New Message Form FlowerShop',
            contact.message,
            contact.email,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
