from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import F
from .models import Contact
from .serializers import ContactSerializer


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_update(self, serializer):
        contact_id = self.kwargs['pk']
        contact = get_object_or_404(Contact, id=contact_id)

        provided_version = self.request.data.get('version', None)
        if provided_version is not None and int(provided_version) != contact.version:
            response_data = {'error': 'Conflict - Contact has been updated by another user.'}
            return Response(response_data, status=status.HTTP_409_CONFLICT)

        Contact.objects.filter(id=contact_id, version=contact.version).update(version=F('version') + 1)

        contact.refresh_from_db()

        serializer.save()
