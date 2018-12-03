def hwO_strTopHW():
    return "{type='omui::PhysicalTopLevelWidget_c' unnamed='1' visible='1' windowTitle?='Headwave*'}"

def hwO_mapTopMenuBar():
    return {"type": "QMenuBar", "unnamed": 1, "visible": 1}

def hwO_objCloseHWButton():
    objTopHW = actionWaitForObject(hwO_strTopHW())
    objPhyContainer = com_findChildByType(objTopHW, "PhysicalContainerWidget")
    objPhyObjTitlebar = com_findChildByType(objPhyContainer, "PhysicalObjectTitlebarWidget")
    objObjViewCanvas = com_findChildByType(objPhyObjTitlebar, "ObjectViewCanvasWidget")
    objTitlePlaceholder = com_findChildByType(objObjViewCanvas, "TitlePlaceholderWidget")
    lstChildren = object.children(objTitlePlaceholder)
    for child in lstChildren:
        objActionProp = com_findChildByType(child, "ActionPropertyWidget")
        if not com_isNone(objActionProp):
            objButton = com_findChildByType(objActionProp, "CustomButtonWidget")
            if not com_isNone(objButton) and objButton.toolTip == "Close":
                return objButton
    return None

def hwO_mapInvalidateCacheDataName():
    return hwO_mapButtonName("Ok")

def hwO_mapButtonName(strText, strWindowTitle="", mapProp={}):
    mapRealName = {"type": "omui::CustomButtonWidget_c", "unnamed": 1, "visible": 1}
    if strText != "":
        mapRealName["text"] = strText
    if strWindowTitle != "":
        mapRealName["window"] = {"type": "omui::PhysicalTopLevelWidget_c", "unnamed": 1, "visible": 1, "windowTitle": strWindowTitle}
    if mapProp != {}:
        mapRealName.update(mapProp)
    return mapRealName

def hwO_mapCreateWorkspace():
    return hwO_mapButtonName("Create workspace")

def hwO_strWorkspaceNameParent2():
    return "{type='omui::ObjectBrowserLinePlaceholderWidget_c' unnamed='1' visible='1' toolTip?='*name*workspace*create*'}"
#     return "{'type': 'omui::ObjectBrowserLinePlaceholderWidget_c', 'unnamed': 1, 'visible': 1, 'toolTip': 'The name of the workspace to create'}""

def hwO_objWorkspaceName():
    objWspNameParent2 = actionWaitForObject(hwO_strWorkspaceNameParent2())
    objTextProp = com_findChildByType(objWspNameParent2, "TextPropertyWidget")
    return com_findChildByType(objTextProp, "CustomLineEditWidget")

def hwO_strImportButton():
    return hwO_mapButtonName("", mapProp={"toolTip?": "Import*load dataset"})

def hwO_strInputFileLineEdit():
    return "{name='fileNameEdit' type='QLineEdit' visible='1'}"

def hwO_strInputFileType():
    return "{name='fileTypeCombo' type='QComboBox' visible='1'}"

def hwO_strYesNoWarning(isYes=True):
    if isYes:
        return hwO_mapButtonName("Yes", "Warning")
    return hwO_mapButtonName("No", "Warning")

def hwO_objPhysicalContainer_3():
    objHw = actionWaitForObject(hwO_strTopHW())    
    objContainer1 = com_findChildByTypeAtIndex(objHw, "PhysicalContainerWidget",0)
    objContainer2 = com_findChildByTypeAtIndex(objContainer1, "PhysicalContainerWidget",0)
    objContainer3 = com_findChildByTypeAtIndex(objContainer2, "PhysicalContainerWidget",0)
    return objContainer3

def hwO_objPhysicalContainer_4():
    objContainer3 = hwO_objPhysicalContainer_3()
    return com_findChildByTypeAtIndex(objContainer3, "PhysicalContainerWidget",0)  

def hwO_objStatusBarLineEdit():
    try:
        objPhyContainer = hwO_objPhysicalContainer_4()
        objPhysicalObjectStatusbar = com_findChildByTypeAtIndex(objPhyContainer, "PhysicalObjectStatusbarWidget", 0)
        objObjectViewCanvas = com_findChildByTypeAtIndex(objPhysicalObjectStatusbar, "ObjectViewCanvasWidget", 0)
        objToolbarBackground = com_findChildByTypeAtIndex(objObjectViewCanvas, "CustomToolbarBackgroundWidget", 1)
        objTextProperty = com_findChildByTypeAtIndex(objToolbarBackground, "TextPropertyWidget", 0)    
        return com_findChildByTypeAtIndex(objTextProperty, "CustomLineEditWidget", 0)
    except:
        return None

def hwO_strViewTitleLineEdit(viewName, strWindow = ""):
    strName = "{type='omui::CustomLineEditWidget_c' visible='1' text?='*%s*' toolTip?='*window*2D*3D*'}" % viewName
    if strWindow != "" and len(strName) > 1 and strName[len(strName) - 1] == '}':
        strName = strName[0:len(strName) - 1] + " window={type='omui::PhysicalTopLevelWidget_c' windowTitle='%s' visible='1'}}" % strWindow
    return strName

def hwO_getViewTitlePlaceholder(strViewName, strWindow = ""):
    objViewTitleLineEdit = actionWaitForObject(hwO_strViewTitleLineEdit(strViewName, strWindow))
    if com_isNone(objViewTitleLineEdit):
        return None
    objTextPropertyParent = object.parent(objViewTitleLineEdit)
    if com_isNone(objTextPropertyParent):
        return None
    objToolbarBackgroundParent = object.parent(objTextPropertyParent)
    if com_isNone(objToolbarBackgroundParent):
        return None
    return object.parent(objToolbarBackgroundParent)

def hwO_getTopViewContainer(strViewName, strWindow = ""):
    objViewTitlePlaceholder = hwO_getViewTitlePlaceholder(strViewName, strWindow)
    if com_isNone(objViewTitlePlaceholder):
        return None
    objObjectViewCanvasParent = object.parent(objViewTitlePlaceholder)
    objPhysicalObjectTitleBarParent = object.parent(objObjectViewCanvasParent)
    return object.parent(objPhysicalObjectTitleBarParent)

def hwO_getViewHueSpace(strViewName):
    objTopViewContainer = hwO_getTopViewContainer(strViewName)
    if com_isNone(objTopViewContainer):
        return None
    objViewContainer = com_findChildByTypeAtIndex(objTopViewContainer, "PhysicalContainerWidget", 0)
    objViewContainer2 = com_findChildByTypeAtIndex(objViewContainer, "PhysicalContainerWidget", 0)
    objPhysicalHueSpace = com_findChildByTypeAtIndex(objViewContainer2, "PhysicalHuespaceWidget", 0)
    if com_isNone(objPhysicalHueSpace):
        objViewContainer3 = com_findChildByTypeAtIndex(objViewContainer2, "PhysicalContainerWidget", 0)
        objPhysicalHueSpace = com_findChildByTypeAtIndex(objViewContainer3, "PhysicalHuespaceWidget", 0)
    return com_findChildByTypeAtIndex(objPhysicalHueSpace, "BasicHuespaceWidget", 0)

def hwO_getVisibleObjectCanvas(isLeftCanvas):
    objObjectContainer = hwO_objListTabsContainer_11()
    lstObjectCanvas = com_findChildrenHaveType(objObjectContainer, "PhysicalObjectCanvasWidget")
    for objObjectCanvas in lstObjectCanvas :
        if objObjectCanvas.visible and objObjectCanvas.height > 0:
            return objObjectCanvas    
    lstContainer = com_findChildrenHaveType(objObjectContainer, "PhysicalContainerWidget")
    for objContainer in lstContainer:
        if objContainer.visible and objContainer.height > 0:
            if isLeftCanvas:
                objContainer1  = com_findChildByTypeAtIndex(objContainer, "PhysicalContainerWidget", 0)
                objLeftObjectCanvas = com_findChildByTypeAtIndex(objContainer1, "PhysicalObjectCanvasWidget", 0)
                return objLeftObjectCanvas
            else:
                objContainer1  = com_findChildByTypeAtIndex(objContainer, "PhysicalContainerWidget", 1)                
                objLeftObjectCanvas = hwO_objVisibleCanvas(objContainer1)
                return objLeftObjectCanvas
    objLeftObjectCanvas = None
    return None

def hwO_objVisibleCanvas(objPhyContainer):
    lstObjectCanvas = com_findChildrenHaveType(objPhyContainer, "PhysicalObjectCanvasWidget")
    for objObjectCanvas in lstObjectCanvas :
        if com_objectExists(objObjectCanvas):
            return objObjectCanvas    
    lstContainer = com_findChildrenHaveType(objPhyContainer, "PhysicalContainerWidget")
    for objContainer in lstContainer:
        if com_objectExists(objContainer):
            objCanvas = hwO_objVisibleCanvas(objContainer)
            if com_objectExists(objCanvas):
                return objCanvas
    return None

def hwO_objPhysicalContainer_5():
    objContainer4 = hwO_objPhysicalContainer_4()
    return com_findChildByTypeAtIndex(objContainer4, "PhysicalContainerWidget",0)

def hwO_objPhysicalContainer_6():
    objContainer5 = hwO_objPhysicalContainer_5()
    objContainer = com_findChildByTypeAtIndex(objContainer5, "PhysicalContainerWidget", 0)
    return objContainer

def hwO_objPhysicalContainer_7():
    objContainer =  hwO_objPhysicalContainer_6()  
    return com_findChildByTypeAtIndex(objContainer, "PhysicalContainerWidget", 0)

def hwO_objPhysicalContainer_8():
    objContainer1 = hwO_objPhysicalContainer_7()
    objContainer2 =  com_findChildByTypeAtIndex(objContainer1, "PhysicalContainerWidget", 0)
    return objContainer2

def hwO_objPropertiesViewWindow_9():
    objApplicationObject = hwO_objPhysicalContainer_8()
    objContainer1 = com_findChildByTypeAtIndex(objApplicationObject, "PhysicalContainerWidget", 1)
    return objContainer1

def hwO_objPropertiesViewContent_10():
    objContainer =  hwO_objPropertiesViewWindow_9()
    objContainer10 = com_findChildByTypeAtIndex(objContainer, "PhysicalContainerWidget", 0)
    return objContainer10

def hwO_objListTabsContainer_11():
    objContainer = hwO_objPropertiesViewContent_10()
    objContainer100 = com_findChildByTypeAtIndex(objContainer, "PhysicalContainerWidget", 0)
    return objContainer100

def hwO_objCustomLineEditExistInViewCanvas(objPhysicalObjectCanvas, mapRealName, intIndex = 0):
    objCanvas = hwO_getViewCanvas(objPhysicalObjectCanvas)
    if com_isNone(objCanvas):
        return None   
    if const_propType() in mapRealName and const_typeObjectBrowserLinePlaceholderWidget() in mapRealName[const_propType()]:
        return findObjectByParent(objCanvas, mapRealName)
    lstPlaceholder = object.children(objCanvas)
    for objPlaceholder in lstPlaceholder:
        if com_objectExists(objPlaceholder):
            objLineEdit = findObjectByParent(objPlaceholder, mapRealName, intIndex)
            if not com_isNone(objLineEdit):
                return objLineEdit
    return None

def hwO_getViewCanvas(objCanvas):
    objScrollArea = com_findChildByTypeAtIndex(objCanvas, "CustomScrollArea",0)
    objWidget = com_findChildByTypeAtIndex(objScrollArea, "QWidget",0)
    objViewCanvas = com_findChildByTypeAtIndex(objWidget, "ObjectViewCanvasWidget", 0)
    return objViewCanvas

def hwO_getCurrentScrollBar(isLeft):
    objObjectCanvas = hwO_getVisibleObjectCanvas(isLeft)
    if com_isNone(objObjectCanvas):
        return None
    objScrollArea = com_findChildByTypeAtIndex(objObjectCanvas, "CustomScrollArea",0)
    if com_isNone(objScrollArea):
        return None
    objContainer = com_findChildByTypeAtIndex(objScrollArea, "QWidget", 2)
    if com_isNone(objContainer):
        return None
    objScrollBar = com_findChildByType(objContainer, "QScrollBar")
    return objScrollBar

def hwO_getDisableSaveButtonName():
    objSaveAsButton = waitForObject(hwO_mapSaveAsButton())
    objSaveAsActionPropertyWidget = object.parent(objSaveAsButton)
    objCustomToolbar = object.parent(objSaveAsActionPropertyWidget)
    objViewCanvas = object.parent(objCustomToolbar)
    lstCustomToolBarList = object.children(objViewCanvas)
    for objChild in lstCustomToolBarList:
        objActionPropertyWidget = com_findChildByTypeAtIndex(objChild, "ActionPropertyWidget", 0)
        if objActionPropertyWidget and "Save the workspace" in str(objActionPropertyWidget.toolTip) and "disabled" in str(objActionPropertyWidget.toolTip):
            return com_findChildByTypeAtIndex(objActionPropertyWidget, "CustomButtonWidget", 0)
    return None

def hwO_mapSaveAsButton():
    return hwO_mapButtonName("", mapProp={"toolTip?": "Save*workspace*new*name"})
    
def hwO_getTabByTabName(strTabName=""):
    mapRealName = {"type": "omui::PhysicalContainerDecorationWidget_c", "unnamed": 1, "visible": 1}
    if strTabName != "":
        mapRealName["toolTip?"] = strTabName
    return mapRealName

def hwO_mapLabelNameByText(strText, isExact=True):
    mapRealName = {"type": "omui::CustomObjectBrowserLineWidget_c", "unnamed": 1, "visible": 1}
    if isExact:
        mapRealName["text"] = strText
    else:
        mapRealName["text?"] = strText
    return mapRealName

def hwO_mapOverallCompleteFactorLabel():
    return hwO_mapLabelNameByText("Overall complete factor")

def hwO_mapEnableVisualizationLabel():
    return hwO_mapLabelNameByText("Enable visualization")
    
def hwO_mapShowAdvancedProperties():
    return hwO_mapButtonName("", mapProp={"toolTip?": "Whether to show advanced"})

def hwO_mapInlineBytePositionLabel():
    return hwO_mapLabelNameByText("Inline byte position")

def hwO_mapCrosslineBytePositionLabel():
    return hwO_mapLabelNameByText("Crossline byte position")

def hwO_mapEastingBytePositionLabel():
    return hwO_mapLabelNameByText("Easting byte position")

def hwO_mapNorthingBytePositionLabel():
    return hwO_mapLabelNameByText("Northing byte position")

def hwO_mapDisplayNameLabel():
    return hwO_mapLabelNameByText("Name")

def hwO_mapMenuByText(strText):
    return {"text": strText, "type": "QAction", "unnamed": 1, "visible": 1}

def hwO_mapFileMenu():
    return hwO_mapMenuByText("File")