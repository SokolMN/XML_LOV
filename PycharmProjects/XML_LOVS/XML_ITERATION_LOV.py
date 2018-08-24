def iterate(root):
    sub_list = []
    for child in root:#Второй уровень
        print("FFFQQQQQQQQQQ")
        print("AATTTTT ", child.tag, child.attrib)
        for subchild in child:#Третий уровень
            print("SUB CHFILD: ", subchild.tag, subchild.text)
            for sub_sub_child in subchild:
                if sub_sub_child.tag == "List_spcOf_spcValues_spcParent_spc_lprUDA_rpr":
                    sub_list.append(sub_sub_child)
    return sub_list


def lov_iterate(lov_root):
    sub_list_lov = []
    for child in lov_root:
        for sub_child in child:
                if sub_child.tag == "List_spcOf_spcValues_spcChild_spc_lprUDA_rpr":
                    sub_list_lov.append(sub_child)
    return sub_list_lov