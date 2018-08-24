def findValue(root, elName):
    for child in root:
        for sub_child in child:
            print("DDDAAAAA", child.tag)
            if sub_child.text == elName:
                return "Y"

def findName(root, elName):
    for child in root:
        print("DDDAAAAA", child.tag)
        if child.tag == elName:
            return "Y"

def getTag(root, elValue):
    for child in root:
        print("FIND TAG", child.tag)
        for sub_child in child:
            if sub_child.text == elValue:
                return sub_child.tag

def chahgeTagValue(root, tagName, tagValue):
    for child in root.iter(tagName):
        #for sub_child in child:
        child.text = tagValue