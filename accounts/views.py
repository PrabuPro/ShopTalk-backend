# from django.shortcuts import render
# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from knox.models import AuthToken
# from .serializers import UserSerializers, RegisterSerializers
#
#
# # Create your views here.
# # Register API
# class RegistrationApi(generics.GenericAPIView):
#     serializer_class = RegisterSerializers
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializers(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)
#         })
