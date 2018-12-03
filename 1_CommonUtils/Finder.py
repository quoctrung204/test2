## --------------------------------------------------------------------
## This file contains utilities for finding objects
## Most of HW dependent object recognition methods will be included here
## --------------------------------------------------------------------
def findObjectInPropertyView(mapRealNameOfRef, lstContParseInfo=[], isLeftScrollArea=True, intIndex=0, objToReturn=None):
    if not com_isNone(objToReturn):
        return objToReturn
    try:
        if not isinstance(mapRealNameOfRef, dict):
            mapRealNameOfRef = com_getListPropertiesFromString(mapRealNameOfRef)
        obj = hwC_getObjectInPropertyViewByReference(mapRealNameOfRef, lstContParseInfo, isLeftScrollArea, intIndex)
        if not com_isNone(obj):
            return obj
        intScrollMax = hwO_getCurrentScrollBar(isLeftScrollArea).maximum
        intScrollPos = 0
        while com_isNone(obj) and not com_isNone(hwO_getCurrentScrollBar(isLeftScrollArea)):
            hwO_getCurrentScrollBar(isLeftScrollArea).setValue(intScrollPos)
            obj = hwC_getObjectInPropertyViewByReference(mapRealNameOfRef, lstContParseInfo, isLeftScrollArea, intIndex)
            if intScrollPos >= intScrollMax:
                break
            intScrollPos += 80
        return obj
    except:
        return None
    return None

def findObjectInProjectTree(strObjectName, intFindOption = 0):
    objScrollBar = prjO_getScrollBar()
    intFirstScrollPos = objScrollBar.value
    intScrollMax = objScrollBar.maximum
    intScrollPos = intFirstScrollPos
    isFindFromTop = True 
    obj = None
    while com_isNone(obj):
        if intScrollMax < intScrollPos:
            intScrollPos = intScrollMax
        prjO_getScrollBar(objScrollBar).setValue(intScrollPos)
        obj = prjO_getObjectByName(strObjectName, intFindOption)
        if not com_isNone(obj):
            return obj
        if intScrollPos == intScrollMax:
            if isFindFromTop:
                intScrollPos = 0
                intScrollMax = intFirstScrollPos
                isFindFromTop = False
                continue
            return None
        intScrollPos += 80
    return obj

def recursiveFindObject(objParent, mtxProperty, intIndex = 0, indent = "***"):
    objectType = ""
    for key, value in mtxProperty.iteritems():
        if key == 'type' :
            objectType = value
            break
    if com_isNone(objParent):
        return
    try:
        lstChildren = object.children(objParent)
        intCount = 0
        for objChild in lstChildren:
            if com_isNone(objChild):
                continue
            if com_hwVerifyObjectHasProperties(objChild, objectType, mtxProperty):
                if intCount == intIndex:
                    return objChild
                intCount += 1               
            objFound = recursiveFindObject(objChild, mtxProperty, intIndex, indent = "%s***" % indent) 
            if not com_isNone(objFound):
                return objFound
    except:
        return None
    return None

def findObjectByParent(objParent, mapRealName, intIndex = 0):
    if not com_objectExists(objParent):
        return None
    if not isinstance(mapRealName, dict):
        lstProperty = com_getListPropertiesFromString(mapRealName)
    else:
        lstProperty = mapRealName
    try:
        lstProperty["type"] = com_removeSquishType(lstProperty["type"])
    except:
        {}
#     if "name" in lstProperty.keys() and "objectName" not in lstProperty.keys():
#         lstProperty["objectName"] = lstProperty["name"]
#     elif "name?" in lstProperty.keys() and "objectName" not in lstProperty.keys():
#         lstProperty["objectName?"] = lstProperty["name?"]
    return recursiveFindObject(objParent, lstProperty, intIndex)