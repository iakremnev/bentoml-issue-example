from mypackage.service import Service
from mypackage.model import MySVC

service = Service()
service.pack("model", MySVC())
service.save()