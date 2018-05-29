from account.models import Author
from django.core.exceptions import ValidationError


class EmailCheck(object):

    def authenticate(self, request, email=None, password=None):
        try:
            user = Author.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except Author.DoesNotExist:
            raise ValidationError("Invalid username or password")

    def get_user(self, user_id):
        try:
            return Author.objects.get(pk=user_id)
        except Author.DoesNotExist:
            return None
