import phonenumbers
from test import number


from phonenumbers import  geocoder
ch_number = phonenumbers.parse(number, "VN")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "MB")
print(carrier.name_for_number(service_number, "en"))
