## --------------------------------------------------------------------
## This file contains utilities for verifications of all types
## --------------------------------------------------------------------

## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def verifyObjectText(strObject, strValue):
    {}

## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def verifyObjectExistence(strObject, intTimeout = 5):
    {}
## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def verifyImageExistence(objHw, strVPName, strType = conf_defaultImageComparisonMode(), fltParam1 = conf_defaultImageComparisonParam1() ,fltParam2 = conf_defaultImageComparisonParam2(), isMoved = True):
    if isMoved:
        hwC_moveToHWStatusBar()
    strFullVPName = com_strVPName(strVPName)
    if com_isVPexists(strFullVPName) :
        actionWait(5)
        if test.vp(strFullVPName)==False:
            intInc = 1
            while True:
                strVPNameBackup = strFullVPName + "-v%d" % intInc
                if not com_isVPexists(strVPNameBackup) or test.vp(strVPNameBackup):
                    break
                intInc += 1
        return 1
    else:
        com_createScreenshotVP(objHw, strFullVPName, strType, fltParam1, fltParam2)
        actionWait(5)
        test.vp(strFullVPName)
        strImage = com_getFullVPImagePath(strFullVPName)
        com_deleteFile(strImage)
        com_deleteFolder(com_getHWVPImagePath())
        return 2

## --------------------------------------------------------------------
## Name: 
## --------------------------------------------------------------------
def verifyImageExistenceInHuespaceWindow(strViewName, strVpName, strType = conf_defaultImageComparisonMode(), fltParam1 = conf_defaultImageComparisonParam1(), fltParam2 = conf_defaultImageComparisonParam2()):
    verifyImageExistence(hwO_getViewHueSpace(strViewName), strVpName, strType, fltParam1, fltParam2)
