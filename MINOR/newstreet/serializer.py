from django.core import serializers


with open("file.json", "w") as out:
     data = serializers.serialize("json", rango_newws.objects.all())
     out.write(data)
