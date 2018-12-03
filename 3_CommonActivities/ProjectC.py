def prjC_selectObjectFromProjectTree(strObjectName, intFindOption = 0):
    intCount = 0
    while intCount < 2:
        try:
            mouseClick(findObjectInProjectTree(strObjectName, intFindOption), 0, 0, 0, Qt.LeftButton)
        except:
            actionWait(2)
            intCount += 1
            continue
        break
    return findObjectInProjectTree(strObjectName, intFindOption)

