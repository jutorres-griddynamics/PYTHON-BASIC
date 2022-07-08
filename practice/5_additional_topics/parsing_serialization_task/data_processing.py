import json
import sys
import unittest
import os, json
import pandas as pd
import numpy as np
from xml.etree.ElementTree import Element,tostring

def Average(lst):
    return sum(lst) / len(lst)


# convert a simple dictionary
# of key/value pairs into XML
def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        # create an Element
        # class object
        child = Element(key)
        child.text = str(val)
        elem.append(child)

    return elem

path_to_json_root = '/Users/julitorresma/PycharmProjects/PYTHON-BASIC/practice/5_additional_topics/parsing_serialization_task/source_data/'


#################################################################  PRE PROCESSING JASON FILES
json_files = [pos_json for pos_json in os.listdir(path_to_json_root + 'Barcelona') if pos_json.endswith('.json')]
# here I define my pandas Dataframe with the columns I want to get from the json
os.chdir(path_to_json_root)
cities = sorted([name for name in os.listdir('.') if os.path.isdir(name)])
jsons_data = pd.DataFrame(columns=['weather'])

for i in range(len(cities)):
    path_to_json = path_to_json_root + cities[i]
    with open(os.path.join(path_to_json, json_files[0])) as json_file:
        json_text = json.load(json_file)
        weather = json_text['hourly']
        # here I push a list of data into a pandas DataFrame at row given by its respective city
        jsons_data.loc[cities[i]] = [weather]
#################################################################

jsons_data_characteristics = pd.DataFrame(columns=['Information'])

dict_city_info = {}
dict_city_mean_temp = {}
dict_city_mean_windSpeed ={}
for city in cities:
    #print(city)
    for info in jsons_data.loc[city]:
        temp_key = "temp"
        wind_key = "wind_speed"
        list_temperatures = [a_dict[temp_key] for a_dict in info]
        list_wind_speeds = [a_dict[wind_key] for a_dict in info]

        min_temp = str(round(min(list_temperatures),2))
        min_windSpeeds = str(round(min(list_wind_speeds),2))

        max_temp = str(round(max(list_temperatures),2))
        max_windSpeed = str(round(max(list_wind_speeds),2))

        mean_temp = round(Average(list_temperatures),2)
        mean_wind = round(Average(list_wind_speeds),2)

        dict_city_mean_temp[city] = mean_temp
        dict_city_mean_windSpeed[city] = mean_wind

        dict_city_info[city] = {'min_temp':min_temp,'min_wind_speed':min_windSpeeds,
                            'max_temp':max_temp,'max_wind_speed':max_windSpeed,'mean_temp':str(mean_temp),'mean_wind_speed':str(mean_wind)}



mean_temp_country= str(round(Average(dict_city_mean_temp.values()),2))
mean_windSpeed_country= str(round(Average(dict_city_mean_windSpeed.values()),2))
dict_country_info = {'mean_temp':mean_temp_country,'mean_wind_speed':mean_windSpeed_country
                     ,'coldest_place':str(min(dict_city_mean_temp, key=dict_city_mean_temp.get)),
                     'warmest_place':str(max(dict_city_mean_temp, key=dict_city_mean_temp.get)),
                     'windiest_place':str(max(dict_city_mean_windSpeed, key=dict_city_mean_windSpeed.get))}

xml_dictionary = {'country':'Spain','date':'2021-09-25','summary':dict_country_info,'cities':dict_city_info}



import xml.etree.cElementTree as ET

root = ET.Element("weather",  country="Spain", date="2021-09-25")

summary = ET.SubElement(root, "summary", dict_country_info)
cities = ET.SubElement(root, "cities")
for i in dict_city_info.keys():
    dict_city_info[i]['mean_temp'] = str(dict_city_info[i]['mean_temp'])
    dict_city_info[i]['mean_wind_speed'] = str(dict_city_info[i]['mean_wind_speed'])
    ET.SubElement(cities, str(i) , dict_city_info[i])

tree = ET.ElementTree(root)
tree.write("filename.xml")
