from import_export import resources
from .models import *

class NewsLetterResource(resources.ModelResource):
    class Meta:
        model: NewsLetter