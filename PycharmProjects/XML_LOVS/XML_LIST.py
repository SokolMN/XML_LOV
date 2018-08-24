from xml.etree import ElementTree

def list_equals(list_dev, list_prod):
    for prod_child in list_prod:
        for prod_sub_child in prod_child:
            if prod_sub_child.tag == "Name":
                prod_name = prod_sub_child.text
                break

    for k in list_dev:
        for dev_child in k:
            for dev_sub_child in dev_child:
                if dev_sub_child.text == prod_name:
                    return "Y"

#    if prod_name == dev_name:
 #       return "Y"