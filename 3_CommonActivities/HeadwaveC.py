def hwC_startHWApplication(intTypeOfWorkspace = 0):
    if not com_killHeadwaveMonitor():
        test.log("Cannot kill headwave process!")
    ctx = startApplication(com_getHWAppName())
    #ctx_1 = waitForApplicationLaunch()
    setApplicationContext(ctx)
    if not com_isLinux():
        nativeMouseClick(1021,606,MouseButton.LeftButton)
    snooze(1)  
    hwC_invalidateCacheData()
    #setApplicationContext(ctx)
#     global isPetrelTestCase
#     isPetrelTestCase = False
    intTime = com_getCurrentTime()
    return [ctx, intTime]

def hwC_invalidateCacheData():
    mapInvalidateOKButtonName = hwO_mapInvalidateCacheDataName()
    if actionWaitForObjectExist(mapInvalidateOKButtonName, 1):
        actionClickButton(actionWaitForObject(mapInvalidateOKButtonName))

def hwC_createWorkspace(strWspName):
    objWspNameLineEdit = actionWaitForObject(hwO_objWorkspaceName())
    actionType(objWspNameLineEdit, strWspName)
#     clickButton(waitForObject(hwO_strCreateWorkspace()))
#     objWspNameLineEdit = waitForObject(hwO_getWorkspaceNameLineEdit())
#     com_typeObject(objWspNameLineEdit, strWspName)
#     com_hwMustSnooze(1)
#     wspC_closeIssueWarningView()

def hwC_closeWorkspace(isSave=True):
#     intTimeToWait = 10
#     if not com_isNone(wspO_getDisableSaveButtonName()):
#         intTimeToWait = 3
    actionActivateSingleItem(actionWaitForObject(hwO_mapTopMenuBar()), "File")
    actionWait(0.5)
    try:
        actionActivateItems(["Close workspace"])
    except:
        actionActivateItems(["Close Workspace"])
    actionWait(2)
    if not hwC_existWarningWindow():
        return True
    actionClickButton(actionWaitForObject(hwO_strYesNoWarning(isSave)))
        
#     strOKButton = popW_getInvalidateCacheDataName()
#     lstButton = [strYesNoButton, strOKButton]
    
#     i = com_objectListExistsWithTimeout(lstButton, intTimeToWait)  
#     if i > -1:
#         clickButton(waitForObject(lstButton[i]))
#     
#     if i != 1:
#         if com_objectExistsWithTimeout(strOKButton, 3):
#             clickButton(waitForObject(strOKButton))
#         com_hwMustSnooze(3)
    return False

def hwC_importFile(strFilePath, strFileType):
    actionClickButton(actionWaitForObject(hwO_strImportButton()))
#     objSelectInputFileLineEdit = actionWaitForObject(hwO_strInputFileLineEdit())
#     actionWaitForObject(hwO_strInputFileLineEdit()).setText(strFilePath)
    if not com_isNone(strFileType):
        objInputFileType = actionWaitForObject(hwO_strInputFileType())
        for index in range(objInputFileType.count):
            strItemText = str(objInputFileType.itemText(index))
            if strFileType in strItemText:
                objInputFileType.setCurrentIndex(index)
                break
    actionType(actionWaitForObject(hwO_strInputFileLineEdit()), strFilePath, isCompare=False)

def hwC_enableDisableRendering(isEnable):
    hwC_clickVisualizationTab()
    if isEnable:
        actionClickButton(findObjectInPropertyView(hwO_mapEnableVisualizationLabel(), data_getParseInfoByType(const_parseInfoBoolButton(), [{}, {const_propText(): "{Misc:Yes}"}])))
    else:
        actionClickButton(findObjectInPropertyView(hwO_mapEnableVisualizationLabel(), data_getParseInfoByType(const_parseInfoBoolButton(), [{}, {const_propText(): "{Misc:No}"}])))
        
def hwC_closeHeadwave(isSave):
    actionLeftClick(hwO_objCloseHWButton())
    if hwC_existWarningWindow():
        actionClickButton(actionWaitForObject(hwO_strYesNoWarning(isSave)))
    
def hwC_existWarningWindow():
    if not object.exists(hwO_strYesNoWarning()):
        actionWait(2)
        return object.exists(hwO_strYesNoWarning())
    return True

def hwC_moveToHWStatusBar():
    if not com_isNone(hwO_objStatusBarLineEdit()):
        objParent = object.parent(hwO_objStatusBarLineEdit())
        actionMove(objParent)
        actionLeftClick(objParent)

def hwC_getObjectInPropertyView(isLeftScrollArea, mapName, intIndex=0):
    objContainer = hwO_getVisibleObjectCanvas(isLeftScrollArea)
    obj = hwO_objCustomLineEditExistInViewCanvas(objContainer, mapName, intIndex)
    return obj

def hwC_getObjectInPropertyViewByReference(mapRealNameOfRef, lstContParseInfo=[], isLeft=True, intIndex=0): 
    objRet = hwC_getObjectInPropertyView(isLeft, mapRealNameOfRef, intIndex)
    if com_isNone(objRet):
        test.log("Reference %s not found!" % str(mapRealNameOfRef))
        return None
    for mapParseInfo in lstContParseInfo:
        if mapParseInfo[const_keyParentLevel()] == const_relationSibling():
            objParent = object.parent(objRet)
            objRet = com_findChildByProperties(objParent, mapParseInfo)
        elif mapParseInfo[const_keyParentLevel()] == const_relationChild():
            objRet = com_findChildByProperties(objRet, mapParseInfo)
        elif mapParseInfo[const_keyParentLevel()] == const_relationParent():
            objRet = object.parent(objRet)
        if com_isNone(objRet):
            test.log("Object not found! Info: %s" % str(mapParseInfo))
            return None
    return objRet

def hwC_clickTabByTabObjectName(tabName):
    count = 0
    while True:
        if count > 2:
            break
        bReturn = False
        count += 1
        try:
            lstChilden = object.children(object.parent(actionWaitForObject(hwO_getTabByTabName())))
        except:
            continue
        index = 0
        while True:
            if index >= len(lstChilden):
                break
            if object.exists(hwO_getTabByTabName(tabName)):
                try:
                    temp = actionWaitForObject(hwO_getTabByTabName(tabName))
                    mouseClick(temp, 0, 0, 0, Qt.LeftButton)
                    if not com_objectExists(temp) or not com_isStringEqual(tabName, str(temp.toolTip), False):
                        raise Exception("error", "tab not ready")
                    bReturn = True
                    actionWait(2)
                    break
                except:
                    index = 0
                    lstChilden = object.children(object.parent(actionWaitForObject(hwO_getTabByTabName())))
            obj = lstChilden[index]
            index += 1
            try:
                mouseClick(obj, 0, 0, 0, Qt.LeftButton)
            except:
                continue
    return bReturn

def hwC_clickInputTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("Input")

def hwC_clickParametersTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("Parameters")

def hwC_clickDataTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("Data")

def hwC_clickGeneralTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("General")

def hwC_clickBehaviorTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("Behavior")

def hwC_clickLatticeTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("Lattice")

def hwC_clickCRSTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("CRS")

def hwC_clickGeometryTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("Geometry")

def hwC_clickInfoTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("Info")

def hwC_clickPlacementTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("Placement")

def hwC_clickVisualizationTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("Visualization")

# def hwC_click2WayVisualizationTab(strReferenceKey=""):
#     return hwC_clickTabByTabObjectName("Parameters")
# 
# def hwC_click3WayVisualizationTab(strReferenceKey=""):
#     return hwC_clickTabByTabObjectName("Parameters")

def hwC_clickOutputTab(strReferenceKey=""):
    return hwC_clickTabByTabObjectName("Output")

def hwC_getOverallCompleteFactor():
    hwC_clickOutputTab()
    return str(findObjectInPropertyView(hwO_mapOverallCompleteFactorLabel(), data_getParseInfoByType(const_parseInfoNumberLineEdit())).text)

def hwC_showAdvancedProperties():
    actionClickButton(hwO_mapShowAdvancedProperties())

def hwC_setValueForItem(strKeyName, strTabName, itemValue, isLeft=True, isLeftSplitter=True, isExactTextCompare=False):
    if itemValue == [] or itemValue == "":
        return
    mapLabelName, strParseInfoType, lstMapProp = data_getTabConfigData(strTabName)[strKeyName]
    isAdvanced = False
    if com_isNone(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft)):
        isAdvanced = True
        hwC_showAdvancedProperties()
        hwC_clickTabByTabObjectName(strTabName)

    if strParseInfoType == const_parseInfoEnumCombobox() or strParseInfoType == const_parseInfoReferenceCombobox():
        hwC_setValueForCombobox([mapLabelName, strParseInfoType, lstMapProp], itemValue, isLeft, isExactTextCompare)
    elif strParseInfoType == const_parseInfoBoolButton() or strParseInfoType == const_parseInfoEnumButton():
        hwC_clickButton([mapLabelName, strParseInfoType, lstMapProp], itemValue, isLeft)
    elif strParseInfoType == const_parseInfoFilenameButton():
        hwC_clickFilenameButton([mapLabelName, strParseInfoType, lstMapProp], itemValue, isLeft)
    elif strParseInfoType == const_parseInfoNumber():
        hwC_setValueForNumber([mapLabelName, strParseInfoType, lstMapProp], itemValue, isLeft)
    elif strParseInfoType == const_parseInfoNumberx2():
        hwC_setValueForNumberx2([mapLabelName, strParseInfoType, lstMapProp], itemValue, isLeft)
    elif strParseInfoType == const_parseInfoNumberx3():
        hwC_setValueForNumberx3([mapLabelName, strParseInfoType, lstMapProp], itemValue, isLeft)
    elif strParseInfoType == const_parseInfoFilenameLineEdit() or strParseInfoType == const_parseInfoNumberLineEdit() or strParseInfoType == const_parseInfoTextLineEdit():
        hwC_setValueForLineEdit([mapLabelName, strParseInfoType, lstMapProp], itemValue, isLeft)
    elif strParseInfoType == const_parseInfoColorButton():
        {}

    if isAdvanced:
        hwC_showAdvancedProperties()

def hwC_setValueForNumberx3(lstID, lstValue, isLeft=True):
    if lstValue[0] == "" and lstValue[1] == "" and lstValue[2] == "":
        return
    mapLabelName, strParseInfoType, lstMapProp = lstID
    if com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0).readOnly:
        hwC_clickCheckboxOnLabel(lstID, isLeft)
        hwC_invalidateCacheData()
    if com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0).text != str(lstValue[0]) and lstValue[0] != "":
        actionType(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0), lstValue[0])
        hwC_invalidateCacheData()
    if com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 1).text != str(lstValue[1]) and lstValue[1] != "":
        actionType(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 1), lstValue[1])
        hwC_invalidateCacheData()
    if com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 2).text != str(lstValue[2]) and lstValue[2] != "":
        actionType(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 2), lstValue[2])
        hwC_invalidateCacheData()

def hwC_setValueForNumberx2(lstID, lstValue, isLeft=True):
    if lstValue[0] == "" and lstValue[1] == "":
        return
    mapLabelName, strParseInfoType, lstMapProp = lstID
    if com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0).readOnly:
        hwC_clickCheckboxOnLabel(lstID, isLeft)
        hwC_invalidateCacheData()
    if com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0).text != str(lstValue[0]) and lstValue[0] != "":
        actionType(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0), lstValue[0])
        hwC_invalidateCacheData()
    if com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 1).text != str(lstValue[1]) and lstValue[1] != "":
        actionType(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 1), lstValue[1])
        hwC_invalidateCacheData()

def hwC_setValueForNumber(lstID, value, isLeft=True):
    if value == "":
        return
    mapLabelName, strParseInfoType, lstMapProp = lstID
    if com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0).readOnly:
        hwC_clickCheckboxOnLabel(lstID, isLeft)
        hwC_invalidateCacheData()
    if com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0).text != str(value):
        actionType(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0), value)
        hwC_invalidateCacheData()

def hwC_setValueForLineEdit(lstID, value, isLeft=True):
    if value == "":
        return
    mapLabelName, strParseInfoType, lstMapProp = lstID
    if findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft).readOnly:
        hwC_clickCheckboxOnLabel(lstID, isLeft)
        hwC_invalidateCacheData()
    if findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft).text != str(value):
        actionType(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), value)
        hwC_invalidateCacheData()

def hwC_clickButton(lstID, buttonIndex="", isLeft=True):
    if buttonIndex == "":
        buttonIndex = 0
    mapLabelName, strParseInfoType, lstMapProp = lstID
    actionClickButton(actionWaitForObject(com_findChildByTypeAtIndex(object.parent(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft)), const_typeCustomButtonWidget(), buttonIndex)))
    if hwC_existWarningWindow():
        actionClickButton(actionWaitForObject(hwO_strYesNoWarning(True)))
    hwC_invalidateCacheData()

def hwC_clickFilenameButton(lstID, strValue, isLeft=True):
    mapLabelName, strParseInfoType, lstMapProp = lstID
    actionClickButton(actionWaitForObject(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft)))
    actionWaitForObject(hwO_strInputFileLineEdit()).setText(strFilePath)
    actionType(actionWaitForObject(hwO_strInputFileLineEdit()), "<Return>")

def hwC_setValueForCombobox(lstID, strValue, isLeft=True, isExactTextCompare=False):
    if strValue == "":
        return
    mapLabelName, strParseInfoType, lstMapProp = lstID
    if not com_isStringEqual(str(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft).currentText), strValue, isExactTextCompare):
        actionSelectCombobox(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), strValue, isExactTextCompare)
        hwC_invalidateCacheData()

def hwC_clickCheckboxOnLabel(lstID, isLeft=True):
    mapLabelName, strParseInfoType, lstMapProp = lstID
    obj = findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft)
    objParent = object.parent(object.parent(obj))
    actionLeftClick(com_findChildByTypeAtIndex(objParent, const_typeCustomObjectBrowserLineWidget(), 0), 5, 5)

def hwC_getItemValue(strKeyName, strTabName, isLeft=True):
    mapLabelName, strParseInfoType, lstMapProp = data_getTabConfigData(strTabName)[strKeyName]
    isAdvanced = False
    if com_isNone(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft)):
        isAdvanced = True
        hwC_showAdvancedProperties()
        hwC_clickTabByTabObjectName(strTabName)
    itemValue = None
    if strParseInfoType == const_parseInfoEnumCombobox() or strParseInfoType == const_parseInfoReferenceCombobox():
        itemValue = str(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft).currentText)
    elif strParseInfoType == const_parseInfoNumber():
        itemValue = str(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0).text)
    elif strParseInfoType == const_parseInfoNumberx2():
        strValue1 = str(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0).text)
        strValue2 = str(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 1).text)
        itemValue = [strValue1, strValue2]
    elif strParseInfoType == const_parseInfoNumberx3():
        strValue1 = str(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 0).text)
        strValue2 = str(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 1).text)
        strValue3 = str(com_findChildByTypeAtIndex(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft), const_typeCustomLineEditWidget(), 2).text)
        itemValue = [strValue1, strValue2, strValue3]
    elif strParseInfoType == const_parseInfoFilenameLineEdit() or strParseInfoType == const_parseInfoNumberLineEdit() or strParseInfoType == const_parseInfoTextLineEdit():
        itemValue = str(findObjectInPropertyView(mapLabelName, data_getParseInfoByType(strParseInfoType, lstMapProp), isLeft).text)
    if isAdvanced:
        hwC_showAdvancedProperties()
    return itemValue
        
def hwC_getDisplayNameOfSelectedObject(strName=""):
    hwC_clickGeneralTab()
    return hwC_getItemValue(const_keyDisplayName(), const_tabGeneral(), True)

def hwC_getDisplayNameOfObjectInMultipleSelection(strNameToCompare, strName = ""):
    if strName == "":
        strName = hwC_getDisplayNameOfSelectedObject()
    lstNames = strName.split(' /')
    for strName in lstNames:
        strName = strName.strip()
        if strNameToCompare in strName:
            return strName
    return None

def hwC_getDisplayNamesForListOfObjectInMultpleSelection(lstObjNames):
    strFullName = hwC_getDisplayNameOfSelectedObject()
    lstObj = list()
    for strObj in lstObjNames:
        lstObj.append(hwC_getDisplayNameOfObjectInMultipleSelection(strObj, strFullName))
    return lstObj