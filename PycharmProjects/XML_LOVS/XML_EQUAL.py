def equal_lists(prod_lov, dev_lov):
    for sub_prod_lov in prod_lov:
        for sub_sub_prod_lov in sub_prod_lov:
            if sub_sub_prod_lov.tag == "Name":
                prod_lov_type = sub_sub_prod_lov.text

    for sub_dev_lov in dev_lov:
        for sub_sub_dev_lov in sub_dev_lov:
            if sub_sub_dev_lov.tag == "Name":
                dev_lov_type = sub_sub_dev_lov.text

    if prod_lov_type == dev_lov_type:
        return "Y"