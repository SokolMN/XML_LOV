def createLovMap(lov_list):
    lov_map = {}
    for dev_obj in lov_list:
        for k in dev_obj:
            for ll in k:
                if ll.tag == "Value":
                    lov_value = ll.text
                if ll.tag == "Name":
                    lov_name = ll.text
                    lov_map[lov_name] = lov_value
    return lov_map