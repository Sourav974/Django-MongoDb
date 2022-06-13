
from django.contrib import admin
from django.urls import path
from api.views import *
from component.views import *
from template.views import *
from super_template.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-component/', GetComponents.as_view()),
    path('create-component/', CreateComponents.as_view()),
    path('update-component/', UpdateComponents.as_view()),
    path('delete-component/', DeleteComponents.as_view()),
    path('get-component-by-id/', GetComponentById.as_view()),
    path('get-components/', GetComponents1.as_view()),
    path('create-components/', CreateComponents1.as_view()),
    path('update-components/', UpdateComponents1.as_view()),
    path('delete-components/', DeleteComponentsApi.as_view()),
    path('get-componentid/', GetComponentId.as_view()),
    path('get-template/', GetTemplate.as_view()),
    path('create-template/', CreateTemplate.as_view()),
    path('update-template/', UpdateTemplate.as_view()),
    path('delete-template/', DeleteTemplate.as_view()),
    path('get-templateid/', GetTemplateId.as_view()),
    path('get-super-template/', GetSuperTemplate.as_view()),
    path('create-super-template/', CreateSuperTemplate.as_view()),
    path('update-super-template/', UpdateSuperTemplate.as_view()),
    path('delete-super-template/', DeleteSuperTemplate.as_view()),
    path('get-super-templateid/', GetTemplateId.as_view())

    # path('get-templateid/', GetTemplateId.as_view()),

]
