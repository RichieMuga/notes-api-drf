class UserFilterMixin:
    # This method is responsible for returning the queryset that the view will use to fetch objects from the database.
    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)
