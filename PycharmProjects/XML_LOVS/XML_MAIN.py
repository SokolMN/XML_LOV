from xml.etree import ElementTree
import time
import os
import XML_ITERATION_LOV
import XML_EQUAL
import XML_ATC_POCHTA
import XML_LOV_MAP
import XML_FIND_ELEMENT
import XML_LIST

my_lov = 'LOV_XML'
full_file_lov = os.path.abspath(os.path.join('data', my_lov))

prod_lov  = "LOV_PROD"
full_file_prod_lov = os.path.abspath(os.path.join('data', prod_lov))

dom_lov = ElementTree.parse(full_file_lov)
prod_lov = ElementTree.parse(full_file_prod_lov)

root = dom_lov.getroot()
prod_root = prod_lov.getroot()


time.sleep(3)
#Это список блоков XML для каждой позиции лова
sub_dev_list = []
sub_dev_list = XML_ITERATION_LOV.iterate(root)

#Это список блоков XML для каждой позиции лова
sub_prod_list = []
sub_prod_list = XML_ITERATION_LOV.iterate(prod_root)

time.sleep(3)

##Начинаем сравнивать списки ловов
for sub_dev in sub_dev_list:
    for sub_prod in sub_prod_list:
        if XML_EQUAL.equal_lists(sub_prod, sub_dev) == "Y":
            print("Нашел")
            XML_ATC_POCHTA.lov_update(sub_prod, sub_dev)

print("Начинаю записывать файл")
dom_lov.write("THIS_IS_THE_END.XML", "UTF-8")
print("Записал файл")
