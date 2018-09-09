import math


def sort_property_list(property_list, location):
    latitude = location[0]
    longitude = location[1]
    d = dict()
    for element in property_list:
        distance = math.hypot(latitude - float(element.get('LATITUDE')), longitude - float(element.get('LONGITUDE')))
        d[distance] = element
    sorted_dict = sorted(d.iteritems(), key= lambda x: x[0])
    return list(map(lambda x: x[1], sorted_dict))