## ------------------------------------------------------------------------------------
## This file contains common utilities which are used in common among all test suites.
## ------------------------------------------------------------------------------------
import os
import sys
import math
import re
import time
source(findFile("scripts", "1_CommonUtils/Constant.py"))
source(findFile("scripts", "1_CommonUtils/Config.py"))

def com_CommonInclude():
    source(findFile("scripts", "1_CommonUtils/Actions.py"))
    source(findFile("scripts", "1_CommonUtils/Finder.py"))
    source(findFile("scripts", "1_CommonUtils/VerificationUtils.py"))
    source(findFile("scripts", "2_ObjectRepository/HeadwaveO.py"))
    source(findFile("scripts", "3_CommonActivities/HeadwaveC.py"))
    source(findFile("scripts", "2_ObjectRepository/ProjectO.py"))
    source(findFile("scripts", "3_CommonActivities/ProjectC.py"))
    source(findFile("scripts", "1_CommonUtils/Data.py"))

def com_processExists(processname):
    import subprocess
    tlcall = 'TASKLIST', '/FI', 'imagename eq %s' % processname
    # shell=True hides the shell window, stdout to PIPE enables
    # communicate() to get the tasklist command result
    tlproc = subprocess.Popen(tlcall, shell=True, stdout=subprocess.PIPE)
    # trimming it to the actual lines with information
    tlout = tlproc.communicate()[0].strip().split('\r\n')
    # if TASKLIST returns single line without processname: it's not running
    if len(tlout) > 1 and processname in tlout[-1]:
        print('process "%s" is running!' % processname)
        return True
    else:
        print(tlout[0])
        print('process "%s" is NOT running!' % processname)
        return False
    
def com_killHeadwaveMonitor():
    import os
    if com_isLinux():
        import __builtin__
        import subprocess, signal
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            if ('Main thread' in line) or ('internal.head' in line):
                pid = __builtin__.int(line.split(None, 1)[0])
                os.kill(pid,9)
                os.system("kill -9 pid")
    else:
        import os
        ret = True
        intCount = 0
        while ret is True and intCount < 3:
            ret = False
            import os
            os.system("taskkill /F /im VSJitDebugger.exe")
            os.system("taskkill /F /im WerFault.exe")
            os.system("taskkill /F /im HeadwaveMonitor.exe")
            os.system("taskkill /F /im headwave.exe")
            
            ret = com_processExists("headwave.exe")
            if not ret:
                ret = com_processExists("HeadwaveMonitor.exe")
            if not ret:
                ret = com_processExists("WerFault.exe")
            if not ret:
                ret = com_processExists("VSJitDebugger.exe")
                intCount += 1        
                os.system("taskkill /f /im squishcrashwatcher.exe")
    return True

def com_getHWAppName():
    if com_isLinux():
        return conf_strHeadwaveAppName_Linux()
    return conf_strHeadwaveAppName_Window()

def com_isLinux():
    import platform
    if platform.system() == "Linux":
        return True
    return False

def com_getCurrentTime():
    return time.time()

def com_isNone(object):
    try:
        return object is None or isNull(object)
    except:
        return False

def com_checkClassType(object, strType):
    if com_isNone(object):
        test.log('object is None')
        return False
    if strType == "":
        return True
    strRealType = com_getSquishType(strType)
    return com_isClassType(object,strRealType) or com_isClassType(object, strType)

def com_getSquishType(strType):
    lstQtTypeList = ("QWidget", "QScrollBar", "QBoxLayout", "QMenuBar", "QAction", "QModelIndex", "QSpinBox", "QLineEdit", "Label", "ListItem", "DataItem", "Tree", "Pane", "QScrollArea")
    if strType in lstQtTypeList:
        return strType
    else:
        return "omui::%s_c" % strType

def com_removeSquishType(strType):
    strType = strType.replace("omui::", "")
    return strType.replace("_c", "")

def com_isClassType(object, strName):
    return com_getObjectType(object) == strName

def com_getObjectType(object):
    return className(object)

def com_findChildByTypeAtIndex(objParent, strChildType, intIndex=0):
    if (com_isNone(objParent)):
        return None
    lstChildren = object.children(objParent)
    intCount = 0
    for objChild in lstChildren :
        if not com_isNone(objChild) and (com_isNone(strChildType) or com_checkClassType(objChild, strChildType)):
            if intIndex < 0 or intCount == intIndex:
                return objChild
            intCount += 1
    return None

def com_findChildByType(objParent, strChildType):
    lstChildren = object.children(objParent)
    for objChild in lstChildren :
        if not isNull(objChild) and com_checkClassType(objChild, strChildType):
            return objChild
    return None

def com_findChildByProperties(objParent, mapProp):
    lstChildren = object.children(objParent)
    for objChild in lstChildren :
        if com_hwVerifyObjectHasProperties(objChild, mapProp[const_propType()], mapProp):
            return objChild
    return None

def com_findChildrenHaveType(objParent, strChildType):
    lstList = []
    lstChildren = object.children(objParent)
    for objChild in lstChildren :
        if com_checkClassType(objChild, strChildType):
            lstList.append(objChild)
    return lstList

# def com_typeObject(obj, strValue, isReturn = True, isClick = True, strObjName = ""):
#     if strObjName != "":
#         objName = strObjName
#     else:
#         objNameFromObject =  str(objectMap.realName(obj))
#         matchObj1 = re.match("[{](name=[\w\[\]\-\'\.\/]+)", objNameFromObject, re.M|re.I)
#         matchObj2 = re.search("(type=[\w\[\]\'\.\:]+)", objNameFromObject, re.M|re.I)
#         if matchObj1:
#             objName = matchObj1.group(0)
#             if matchObj2:
#                 objName = objName + " " + matchObj2.group(0) + " visible='1'"+ "}"
#             else:
#                 objName = objName + " visible='1'"+ "}"
#         else:
#             objName = objNameFromObject  
#     #objName =  objectMap.realName(obj)
#     i = 0
#     while i < 5:
#         try:
#             if str(waitForObject(objName).text) != strValue:
#                 if isClick:
#                     mouseClick(waitForObject(objName))
#                 com_hwMustSnooze(0.5)
#                 type(waitForObject(objName), "<Ctrl+A>")
#                 com_hwMustSnooze(0.5)
#                 type(waitForObject(objName), strValue)
#             if isReturn:
#                 com_hwMustSnooze(0.5)
#                 type(waitForObject(objName), "<Return>")
#             return True
#         except:
#             i += 1
#     return False

def com_handleRemoveReadonly(func, strPath, exc):
    import errno, os, stat, shutil
    excvalue = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(strPath, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
        func(strPath)
    else:
        raise

def com_deleteFolderContent(strFolderPath, lstExceptionExt=[]):
    import os, shutil
    if os.path.isdir(strFolderPath):
        for strFile in os.listdir(strFolderPath):
            strFilepath = os.path.join(strFolderPath, strFile)
            if os.path.isdir(strFilepath):
                shutil.rmtree(strFilepath, True)
            else:
                strFilename, strExt = os.path.splitext(strFile)
                if lstExceptionExt != [] and strExt in lstExceptionExt:
                    continue
                if strFile != "headwave.log":
                    os.remove(strFilepath)

def com_deleteFile(strFilePath):
    if os.path.isfile(strFilePath):
        os.remove(strFilePath)

def com_deleteFolder(strFolderPath):
    com_deleteFolderContent(strFolderPath)
    import os, shutil
    if os.path.isdir(strFolderPath):
        shutil.rmtree(strFolderPath, ignore_errors=False, onerror=com_handleRemoveReadonly)
        
def com_deleteHWWorkspace(strWspName):
    com_deleteFile(com_getWorkspacePath(strWspName))
    com_deleteFolder(com_getWorkspaceFolderPath(strWspName))

def com_getWorkspacePath(strWorkspaceName):
    strFullWspName = "%s.hww" % (strWorkspaceName)
    if strWorkspaceName[-4:] == ".hww":
        strFullWspName = strWorkspaceName
    return "%s/%s" % (com_getHWWorkingPath(), strFullWspName)

def com_getHWWorkingPath():
    if com_isLinux():
        return conf_strWorkingPath_Linux()
    return conf_strWorkingPath_Window()

def com_getHWDataPath():
    if com_isLinux():
        return conf_strDataPath_Linux()
    return conf_strDataPath_Window()

def com_getWorkspaceFolderPath(strWorkspaceName):
    return "%s/%s.hwd" % (com_getHWWorkingPath(), strWorkspaceName)

def com_strVPName(strVPName):
    if com_isLinux():
        strName = strVPName + conf_strPostfixVPName_Linux()
    else:
        strName = strVPName + conf_strPostfixVPName_Windows()
    return strName + "_" + com_getPCNameWithReplaceDotByUnderscore()

def com_getPCNameWithReplaceDotByUnderscore():
    import socket
    strOrgName = socket.gethostname()
    return strOrgName.replace(".", "_")

def com_isVPexists(strVPName):
    return os.path.exists(com_getVPFileName(strVPName))

def com_getVPFileName(strVPName):
    strVPFileDir = os.path.join(squishinfo.testCase, 'verificationPoints')
    if not os.path.exists(strVPFileDir):
        os.makedirs(strVPFileDir)
    return os.path.join(strVPFileDir, strVPName)

def com_createScreenshotVP(objWidget, strVPName, strType, fltParam1, fltParam2):
    import os.path
    import subprocess
    
    # Delay for stable image
    actionWait(5)

    # Try to get a symbolic name for the widget:
    strObjName = objectMap.realName(objWidget)

    strObjName = com_removeHWBuildOutOfRealName(strObjName)

    # Create remote screenshot of the widget:
    objImg = grabWidget(objWidget)
    actionWait(3)
    strImgFilename = com_getFullVPImagePath(strVPName)
#     img_filename = "D:\Debug_Squish\"
#     img_filename =  'hwvp_' + strVPName + '.png';
    objImg.save(strImgFilename, "PNG")

    # Copy remote file to computer that is
    # executing this script/squishrunner:
    testData.get(strImgFilename)

    strVPFilename = com_getVPFileName(strVPName)

    # Create verification point file:
    subprocess.call([os.path.join(os.environ['SQUISH_PREFIX'], 'bin', 'convertvp'),
                     "--tovp",
                     strVPFilename,
                     strImgFilename,
                     strObjName])
    com_configVP(strVPFilename, strType, fltParam1,fltParam2)

def com_removeHWBuildOutOfRealName(strRealName):
    intPosTitle = strRealName.find("windowTitle")
    intHWPos = strRealName.find("Headwave")
    if intPosTitle > 0 and intHWPos > 0:
        strRealName = strRealName[0 : intPosTitle] + "} }"

    intPos = strRealName.find("window")
#     intPosVPE = strRealName.find("Velocity Pick Editor")
#     intPosAVO = strRealName.find("AVO Crossplot")
#     intPosAVOQC = strRealName.find("AVO QC")
#     intPosPickHor = strRealName.find("Pick horizons")
#     intPosCLSSARGB = strRealName.find("CLSSA & RGB")
#     intPosPoststackSEGYImporter = -1
#     if ('workflowWindow' in globals()):
#         global workflowWindow
#         intPosPoststackSEGYImporter = strRealName.find(workflowWindow)
#     intPosViewPoststackVolume = strRealName.find(const_ViewPoststackVolume())
#     intPosAzimuthOffset = strRealName.find(const_AzimuthOffsetWorkflow())
#     intPosInVA = strRealName.find(const_InVA_Title())
#     intPosAMAS = strRealName.find(const_AngleMuteAndStacksName())
    if (intPos > 0):
        strRealName = strRealName[0 : intPos] + " window={type='omui::PhysicalTopLevelWidget_c' visible='1' } }"
#     elif ((intPos > 0) and (intPosAVOQC >= 0)):
#         strRealName = strRealName[0 : intPos] + " window={type='omui::PhysicalTopLevelWidget_c' unnamed='1' visible='1' windowTitle='AVO QC'}}"
    return strRealName

def com_getFullVPImagePath(strVPName):
    return com_getHWVPImagePath() + '/hwvp_' + strVPName + '.png'

def com_getHWVPImagePath():
    strImagePath = com_getHWWorkingPath() + "/VP_Images"
    if not os.path.exists(strImagePath):
        os.makedirs(strImagePath)
    return strImagePath

def com_configVP(strVPFilename, strType, fltParam1, fltParam2):
    strBuffer = com_strConfigForVP(strVPFilename, strType, fltParam1, fltParam2)
    com_deleteFile(strVPFilename)
    file = open(strVPFilename, 'w')
    file.write(strBuffer)
    file.close()

def com_strDescription(strType):
    if(strType == "Histogram"):
        return '<Algorithm description="Normalized Color Histograms" name="nchcompare">'
    elif (strType == "Pixel"):
        return '<Algorithm description="Simple comparison (pixel by pixel)" name="simplecompare">'
    else:
        return '<Algorithm description="Strict mode" name="strict"/>'

def com_strParam1(strType, fltParam1):
    if(strType == "Histogram"):
        return '<Parameter description="Bin Count" name="bincount">%d</Parameter>' %fltParam1
    elif (strType == "Pixel"):
        return '<Parameter description="Threshold" name="threshold">%f</Parameter>' %fltParam1
    else:
        return ""

def com_strParam2(strType, fltParam2):
    if(strType == "Histogram"):
        return '<Parameter description="Threshold" name="threshold">%f</Parameter>'  %fltParam2
    elif (strType == "Pixel"):
        return '<Parameter description="Tolerance" name="tolerance">%f</Parameter>' %fltParam2
    else:
        return ""

def com_strConfigForVP(strVPFilename, strType, fltParam1, fltParam2):
    file = open(strVPFilename, 'r')
    strUpdate =  com_strDescription(strType) + '\n' +  com_strParam1(strType, fltParam1) +'\n' +    com_strParam2(strType, fltParam2) + '\n' + '</Algorithm>' + '\n' + '</Verification>' +'\n' + '</VerificationPoint>'
    intIndex = 0
    strOldData = ""
    for strLine in file:
        if (intIndex < 3):
            if (intIndex == 1):
                strLine = '<VerificationPoint version="3" type="Screenshot">'
            if(intIndex == 2):
                strTmp = strLine;
                pos = strLine.find("</Verification>")
                if pos > 0 :
                    strTmp = strLine[0 : pos] + "<Mask/>"
                    strLine = strTmp
            strOldData += strLine
        intIndex =  intIndex +1
    file.close()
    return strOldData + strUpdate

def com_hwVerifyObjectHasProperties(obj, objType, mxtProperties):
    # if (not com_checkClassType(obj,objType)) or (not obj.visible):
    if not com_checkClassType(obj,objType) or not com_objectExists(obj):       
        return False
    #objProperties = object.properties(obj)
    objProperties = com_getListProperty(obj, mxtProperties)
    return com_isListContainProperties(objProperties, mxtProperties)

def com_objectExists(obj):
    if com_isNone(obj): 
        return False
    try:
        if not obj.visible:
            return False
    except:
        {}
    try:
        if not obj.height:
            return False
    except:
        {}
    return True

def com_getListProperty(object, mtxProperties):
    mtxProperty = {}
    if com_isNone(object):
        return mtxProperty;
    lstCompareListProperty = com_chooseComparePropertyList(mtxProperties)
    try:
        for strProperty in lstCompareListProperty :
            if hasattr(object, strProperty):
                if strProperty == "text":
                    mtxProperty["text"] = str(object.text)
                if strProperty == "displayText":
                    mtxProperty["displayText"] = str(object.displayText)
                if strProperty == "toolTip":
                    mtxProperty["toolTip"] = str(object.toolTip)
                if strProperty == "width":
                    mtxProperty["width"] = str(object.width)
                if strProperty == "height":
                    mtxProperty["height"] = str(object.height)
                if strProperty == "objectName":
                    mtxProperty["objectName"] = str(object.objectName)
                if strProperty == "visible":
                    mtxProperty["visible"] = str(object.visible)
                    if "rue" in mtxProperty["visible"]:
                        mtxProperty["visible"] = "1"
                    elif "alse" in mtxProperty["visible"]:
                        mtxProperty["visible"] = "0"
                if strProperty == "x":
                    mtxProperty["x"] = str(object.x)
                if strProperty == "y":
                    mtxProperty["y"] = str(object.y)
                if strProperty == "id":
                    mtxProperty["id"] = str(object.id)
        return mtxProperty
    except:
        return mtxProperty
    
def com_chooseComparePropertyList(mxtProperties):
    lstDefaultCompareProperties = ["text", "displayText", "toolTip", "width", "height", "objectName", "visible", "x", "y", "id"]
    lstChooseCompareProperties = []
    for strProperty in lstDefaultCompareProperties:
        strApproximateProp = strProperty + "?"
        if strProperty in mxtProperties.keys() or strApproximateProp in mxtProperties.keys():
            lstChooseCompareProperties.append(strProperty)
    return lstChooseCompareProperties

def com_isListContainProperties(mtxList, mtxSublist):
    for strItem1, strItem2 in mtxSublist.iteritems():
        if com_isDifferentValueInList(strItem1, str(strItem2), mtxList) :
            return False
    return True

def com_isDifferentValueInList(strKey, strValue, mtxObj):
    import fnmatch
    for strKey1, strValue1 in mtxObj.iteritems():
        if strKey == strKey1 + "?":
            if not strValue.startswith("*"):
                strValue = "*" + strValue
            if not strValue.endswith("*") and not strValue.endswith("?"):
                strValue = strValue + "*"
            if not fnmatch.fnmatch(strValue1, strValue):
                return True
        if strKey1 == strKey + "?":
            if not strValue1.startswith("*"):
                strValue1 = "*" + strValue1
            if not strValue1.endswith("*") and not strValue1.endswith("?"):
                strValue1 = strValue1 + "*"
            if not fnmatch.fnmatch(strValue, strValue1):
                return True            
        if strKey == strKey1 and strValue != strValue1:
            return True
    return False

def com_getListPropertiesFromString(strInput):
    mtxDict = {}
    strInput = com_removeBracketAndWhiteSpace(strInput)
    while len(strInput) > 0 :
        lstKey, strValue, int_end_property = com_getPropertyFromString(strInput)
        if lstKey[0] == " ":
            lstKey = lstKey[1 : len(lstKey)]
        if not lstKey == "":
            mtxDict[lstKey] = strValue
            strInput = strInput[int_end_property : len(strInput)]
    return mtxDict

def com_removeBracketAndWhiteSpace(strInput):
    strRemovedBracket = strInput[1: len(strInput) - 1]
    return strRemovedBracket.strip()

def com_getPropertyFromString(strInput):
    strKey = ""
    strValue = ""
    is_begin_value = False
    int_end_property_pos = 0
    int_start_value = 0
    for intIndex in range (0, len(strInput)) :
        if strInput[intIndex] == "=" :
            strKey = strInput[0 : intIndex]
            int_start_value = intIndex+1
        if (strInput[intIndex] == "'") and is_begin_value:
            strValue = strInput[int_start_value + 1 : intIndex]
            int_end_property_pos = intIndex + 2
            break
        if (strInput[intIndex] == "}") and is_begin_value:
            strValue = strInput[int_start_value + 1 : intIndex+1]
            int_end_property_pos = intIndex + 2
            break

        if (strInput[intIndex] == "'") and (int_start_value > 0) :
            int_start_value = intIndex
            is_begin_value = True

        if (strInput[intIndex] == "{") and (int_start_value > 0) :
            int_start_value = intIndex - 1
            is_begin_value = True

    return strKey, strValue, int_end_property_pos

def com_strFileImportType(strName):
    if com_isLinux():
        return strName + " (*)"
    return strName + " (* *.*)"

def com_isStringEqual(strText, strPattern, isExactNameMatching = True):
    if isExactNameMatching:
        return strText == strPattern
    else:
        import fnmatch
        if not strPattern.startswith("*") and not strPattern.startswith("?"):
            strPattern = "*" + strPattern
        if not strPattern.endswith("*") and not strPattern.endswith("?"):
            strPattern = strPattern + "*"
        return fnmatch.fnmatch(strText, strPattern)

def com_getComboboxScrollBar(objCombobox):
    objVContainer = com_findChildByTypeAtIndex(objCombobox, "QWidget", 2)
    return com_findChildByTypeAtIndex(objVContainer, "QScrollBar", 0)

def com_listContains(lstList, objItem):
    return objItem in lstList