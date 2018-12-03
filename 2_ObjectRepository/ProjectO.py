## intFindOption = 0: Exact text matching, 1: Closest text matching 
def prjO_getObjectByName(strName, intFindOption = 0):
    objViewCanvas = prjO_getObjectViewCanvas()
    lstChild = object.children(objViewCanvas)
    intZeroHeightObjectCount = 0
    for obj in lstChild : 
        if com_isLinux() and not com_isNone(obj):
            try:
                if hasattr(obj, 'height') and obj.height == 0:
                    intZeroHeightObjectCount += 1
                    if intZeroHeightObjectCount > 22 :                     
                        return None
            except:
                snooze(1)
                continue
        if com_objectExists(obj) and com_checkClassType(obj, "ObjectPlaceholderWidget"):
            try:
                objContainer1 = com_findChildByType(obj, "TextPropertyWidget")
                objLineEdit = com_findChildByType(objContainer1, "CustomLineEditWidget")
                strText = str(objLineEdit.text)         
                if intFindOption == 0:
                    if strName == str(objLineEdit.text) or strName.strip() == strText.strip():
                        return objContainer1
                else:
                    if fnmatch.fnmatch(strText, "*%s*" % strName):
                        return objContainer1
            except:
                {}      
    return None

def prjO_getProjectObjectColumnName():
    return {"text": "Object", "type": "omui::ColumnHeadingButtonWidget_c", "unnamed": 1, "visible": 1}

def prjO_getScrollBar(objScrollBar = None):
    if com_isNone(objScrollBar):
        objProjectColumn = actionWaitForObject(prjO_getProjectObjectColumnName())
        objCanvasParent = object.parent(objProjectColumn)    
        objScrollArea = com_findChildByType(objCanvasParent, "CustomScrollArea")    
        objVContainer = com_findChildByTypeAtIndex(objScrollArea, "QWidget", 2)
        objScrollBar = com_findChildByType(objVContainer, "QScrollBar")
    return objScrollBar

def prjO_getObjectViewCanvas():
    objProjectColumn = actionWaitForObject(prjO_getProjectObjectColumnName())
    objCanvasParent = object.parent(objProjectColumn)
    objScrollArea = com_findChildByType(objCanvasParent, "CustomScrollArea")    
    objViewPort = com_findChildByTypeAtIndex(objScrollArea, "QWidget", 0)
    return com_findChildByType(objViewPort, "ObjectViewCanvasWidget")