
import sys



import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boss.settings")
django.setup()

from django.core import serializers
from boss_echarts.models import  refined_boss

q=refined_boss.objects.all()
XMLSerializer = serializers.get_serializer("xml")
xml_serializer = XMLSerializer()
# xml_serializer.serialize(q, stream=sys.stdout)
# with open("file.xml", "w") as out:
#     xml_serializer.serialize(q, stream=out)
xml_serializer.serialize(q)
data = xml_serializer.getvalue()
print(data)
