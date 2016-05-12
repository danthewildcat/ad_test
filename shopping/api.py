from django.contrib.auth import get_user_model
from tastypie import fields
from tastypie.authentication import MultiAuthentication, SessionAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.resources import ModelResource

from shopping.models import ShoppingList, ListItem

user_model = get_user_model()

class ListAuthorization(Authorization):
    """Only want users to see their own content"""
    
    def read_list(self, object_list, bundle):
        if bundle.request.user.is_superuser:
            return object_list
            
        return object_list.filter(owner=bundle.request.user)
    
    def read_detail(self, object_list, bundle):
        return (bundle.request.user.is_superuser or
                bundle.obj.owner == bundle.request.user)

    def create_list(self, object_list, bundle):
        # Assuming they're auto-assigned to ``user``.
        return object_list

    def create_detail(self, object_list, bundle):
        return (bundle.request.user.is_superuser or
                bundle.obj.owner == bundle.request.user)

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if (obj.owner == bundle.request.user or
                    bundle.request.user.is_superuser):
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return (bundle.request.user.is_superuser or
                bundle.obj.owner == bundle.request.user)

    def delete_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if (obj.owner == bundle.request.user or
                    bundle.request.user.is_superuser):
                allowed.append(obj)

        return allowed

    def delete_detail(self, object_list, bundle):
        return (bundle.request.user.is_superuser or
                bundle.obj.owner == bundle.request.user)  

class ShoppingListResource(ModelResource):
    class Meta:
        queryset = ShoppingList._default_manager.all()
        resource_name = 'shopping'
        authentication = MultiAuthentication(SessionAuthentication(), )
        authorization = ListAuthorization()

class ListItemResource(ModelResource):
    class Meta:
        queryset = ListItem._default_manager.all()
        resource_name = 'item'
        authentication = MultiAuthentication(SessionAuthentication(), )
        authorization = DjangoAuthorization()
