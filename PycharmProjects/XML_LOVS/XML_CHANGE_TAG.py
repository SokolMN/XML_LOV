def changeTag(root, oldValue, newValue):
    for child in root:
        if child.text == oldValue:
            child.text == newValue