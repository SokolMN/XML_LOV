from xml.etree import ElementTree
import os
import XML_ITERATION_LOV
import XML_LOV_MAP
import XML_FIND_ELEMENT
import XML_LIST
import XML_CHANGE_TAG
import time



def lov_update(lov_prod, lov_dev):
    time.sleep(3)

    #Это список блоков XML для каждой позиции лова
    sub_list_dev = []
    sub_list_dev = XML_ITERATION_LOV.lov_iterate(lov_dev)

    #Это список блоков XML для каждой позиции лова
    sub_prod_list = []
    sub_prod_list = XML_ITERATION_LOV.lov_iterate(lov_prod)
    print("ok")


    time.sleep(3)



    #Тут мы формируем мапы Name - Value
    print("Начинаю формировать мапы")
    time.sleep(5)
    dev_lov_map = XML_LOV_MAP.createLovMap(sub_list_dev)
    prod_lov_map = XML_LOV_MAP.createLovMap(sub_prod_list)

    general_map = XML_LOV_MAP.createLovMap(sub_list_dev)
#prod_lov_map_copy = XML_LOV_MAP.createLovMap(sub_prod_list)
    print("Сформировал мапы")
    time.sleep(10)

    print("Удаляю совпадающие теги")
    #Удаляем совпадающие теги
    for lov_name in prod_lov_map:
        if lov_name in dev_lov_map:
            if prod_lov_map[lov_name] == dev_lov_map[lov_name]:
                print("Есть несовпадение")
                del general_map[lov_name]
                #del prod_lov_map_copy[lov_name]
    print("Удалил совпадающие теги")
    time.sleep(3)

    print("Начинаю сравнивать мапы дева и прода")
    #Начинаем сравнивать мапы дева и прода
    for lov_name in prod_lov_map:
        try:
            if lov_name not in dev_lov_map:
                general_map[lov_name] = prod_lov_map[lov_name]
            if dev_lov_map[lov_name] != prod_lov_map[lov_name]:
                print("Есть несовпадение")
                general_map[lov_name] = prod_lov_map[lov_name]
        except KeyError as err:
            continue
    print("Сравнил мапы дева и прода")
    time.sleep(3)

    print("Начинаю апдейтить XML deva")
    ##Начинаем апдейтить XML deva
    for sub_el in sub_list_dev:
        for lov_namer in general_map:
            print("Новый элемент массива XML!!!!!!!!!!!!!!!!!!")
            if XML_FIND_ELEMENT.findValue(sub_el, lov_namer) == "Y":  ##Ищем лик
                if XML_FIND_ELEMENT.findValue(sub_el, general_map[lov_namer]) != "Y":  ##Ищем значение лова
                    tagName = XML_FIND_ELEMENT.getTag(sub_el, lov_namer)
                    XML_FIND_ELEMENT.chahgeTagValue(sub_el, "Value", general_map[lov_namer])
                    print("ОХУЕННОООО В ДВОЙНЕ")
    print("ЗАапдейтил XML deva")
    time.sleep(3)

    print("Обновляю лист Deva")
    for sub_prod in sub_prod_list:
        for sub_dev in sub_list_dev:
            if XML_LIST.list_equals(sub_list_dev, sub_prod) != "Y":
                sub_list_dev.append(sub_prod)
                break;
    print("Обновил лист Deva")
   # time.sleep(3)

    print("ПОЕХААААААААААААААААААААААААЛИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИ")
    sub_list = []
    print("ПОЕХААААААААААААААААААААААААЛИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИ")
    sub_list = []
    err = "good"
    index = 0
    time.sleep(3)
    for child in lov_dev:#Птяый уровень
        print(child.tag, " ", child.text)
        #if child.tag == "ListOfList_spcOf_spcValues_spcChild_spc_lprUDA_rpr":
            #index = index + 1
        for sub_child in child:
            print(sub_child.tag, " ", sub_child.text)
            if child.tag == "ListOfList_spcOf_spcValues_spcChild_spc_lprUDA_rpr":
                index = index + 1


    print("kkk")
    sub_index = 0
    while sub_index < index:
        try:
            del(child[0])
        except IndexError as err:
            break

    for okk in sub_list_dev:
        child.append(okk)