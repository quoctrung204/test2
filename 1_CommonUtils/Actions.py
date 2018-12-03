## --------------------------------------------------------------------
## Considering a TC as a sequence of actions and verifications, this 
## file automate all actions an end-user need to perform during his/her
## manual testing process
## --------------------------------------------------------------------

## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionLeftClick(objectOrObjectName, x=None, y=None): 
    try:
        if x == None and y == None:
            mouseClick(objectOrObjectName)
        else:
            mouseClick(objectOrObjectName, x, y, 0, Qt.LeftButton)
    except:
        if x == None and y == None:
            mouseClick(actionWaitForObject(objectOrObjectName))
        else:
            mouseClick(actionWaitForObject(objectOrObjectName), x, y, 0, Qt.LeftButton)
            
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionClickButton(objectOrObjectName):
    try:
        clickButton(objectOrObjectName)
    except:
        clickButton(actionWaitForObject(objectOrObjectName))
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionRightClick(objectOrObjectName, x=0, y=0):
    try:
        mouseClick(objectOrObjectName, x, y, 0, Qt.RightButton)
    except:
        mouseClick(actionWaitForObject(objectOrObjectName), x, y, 0, Qt.RightButton)
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionDoubleClick(objectOrObjectName, x, y):
    try:
        doubleClick(objectOrObjectName, x, y, 0, Qt.RightButton)
    except:
        doubleClick(actionWaitForObject(objectOrObjectName), x, y, 0, Qt.RightButton)
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionType(objectOrObjectName, strValue, isReturn = True, isClick = True, isCompare = True):
    i = 0
    while i < 5:
        try:
            if str(actionWaitForObject(objectOrObjectName).text) != strValue:
                if isClick:
                    actionLeftClick(objectOrObjectName)
                actionWait(1)
                type(actionWaitForObject(objectOrObjectName), "<Ctrl+A>")
                actionWait(0.5)
                type(actionWaitForObject(objectOrObjectName), strValue)
                if isCompare and str(actionWaitForObject(objectOrObjectName).text) != strValue:
                    i += 1 
                    continue
            if isReturn:
                actionWait(0.5)
                type(actionWaitForObject(objectOrObjectName), "<Return>")
            return True
        except:
            i += 1
    test.fail("Fail to type text!")
    return False
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionDragAndDrop(objectOrObjectName, fromX, fromY, toX, toY, action): # action should be Qt.CopyAction or Qt.MoveAction
    dragAndDrop(actionWaitForObject(objectOrObjectName), fromX, fromY, actionWaitForObject(objectOrObjectName), toX, toY, action)
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionWait(seconds = 5):
    snooze(seconds)
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionWaitForObjectExist(objectOrObjectName, intDelay = 3):
    count = 0
    while (not object.exists(objectOrObjectName)) and (count < intDelay):
        test.log("Object not ready yet")
        actionWait(1)
        count += 1
    if object.exists(objectOrObjectName):
        return True
    return False
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionWaitForObject(objectOrObjectName, intDelay = 3):
    try:
        actionWaitForObjectExist(objectOrObjectName, intDelay)
    except:
        {}
    return waitForObject(objectOrObjectName)
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionWaitForObjectItem(object, objectItem):
    return waitForObjectItem(object, objectItem)
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionWaitForImage(strImage):
    {}
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionMove(objectOrObjectName):
    try:
        mouseMove(objectOrObjectName, 0, 0)
    except:
        mouseMove(actionWaitForObject(objectOrObjectName), 0, 0)
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionActivateSingleItem(objectOrObjectName, itemText=""):
    if itemText == "":
        activateItem(objectOrObjectName)
    else:
        activateItem(objectOrObjectName, itemText)
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionActivateContextMenu(obj, lstAction, x=15, y=81):
    actionRightClick(obj, x, y)
    actionWait(2)
    intCount = 0
    while intCount < 3 and not actionActivateItems(lstAction):
        actionRightClick(obj, x, y)
        intCount += 1
#     strYesButtonName = popW_getYesButtonName()
#     if object.exists(strYesButtonName):
#         clickButton(waitForObject(strYesButtonName))
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionActivateItems(lstItems):
    bFirstItem = True
    strItemSaved = ""
    mapQMenu = {"type": "QMenu", "unnamed": 1, "visible": 1}
    for item in lstItems:
        if item != "":
            if bFirstItem:
                menuName = mapQMenu
#                 obj = actionWaitForObjectItem(mapQMenu, item)
                bFirstItem = False
            else:
                menuName = {"title": strItemSaved}
                menuName.update(mapQMenu)
            obj = actionWaitForObjectItem(menuName, item)
            if com_isNone(obj):
                try:
                    obj = actionWaitForObjectItem(mapQMenu, item)
                except:
                    test.log("DEBUG info for context action")
                    lstChild = com_findChildrenHaveType(actionWaitForObject(menuName), 'QAction')
                    for strChild in lstChild:
                        test.log("Child %s" % strChild.text)
                    return False
#                     obj = actionWaitForObject(realName)
#                     obj = waitForObjectItem(strTopContextMenuRealName, item)
#             test.log("Real name of menu item:  %s" % objectMap.realName(obj)) # good for debug
            strItemSaved = obj.text
            actionActivateSingleItem(obj)
        actionWait(0.5)
    return True
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def actionSelectCombobox(objCombobox, strTextLabel, isExactText = False):
    if not com_objectExists(objCombobox):
        return False
    strComboboxName = objectMap.realName(objCombobox)
    mapName = {"type" : "QModelIndex", "text?" : strTextLabel}
    if isExactText:
        mapName = {"type" : "QModelIndex", "text" : strTextLabel}
    count = 0
    while count < 5:
        count += 1
        try:
            if com_isLinux():
                mousePress(actionWaitForObject(strComboboxName), 5, 5, MouseButton.LeftButton)
            else:
                mouseClick(actionWaitForObject(strComboboxName), 5, 5, 0, MouseButton.LeftButton)
            com_hwMustSnooze(1)
            objScrollBar = com_getComboboxScrollBar(actionWaitForObject(strComboboxName))
            lstChild = object.children(actionWaitForObject(strComboboxName))
            if com_isNone(lstChild) or len(lstChild) == 0:
                continue
            lstChild = lstChild[::-1]
            if not hasattr(lstChild[0], 'row'):
                continue
            nMaxItem = lstChild[0].row + 1
            objItem = com_hwFindObject(actionWaitForObject(strComboboxName), mapName)
            if not objItem.enabled:
                intScrollPos = objScrollBar.maximum * objItem.row / nMaxItem
                objScrollBar.setValue(intScrollPos)
                continue
            else:
                mouseClick(objItem, 5, 5, 0, MouseButton.LeftButton)
                return True
        except:
            continue
    return False