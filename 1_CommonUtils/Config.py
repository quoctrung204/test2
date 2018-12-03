def conf_strSquishHomeFolder_Linux(strUser):
    return "/Headwave/Software/Squish6/ver1"

def conf_strHeadwaveHomeFolder_Linux_Root():
    return "/root"

def conf_strHeadwaveHomeFolder_Linux_NotRoot(strUser):
    return "/home/%s" % strUser

def conf_strDefaultDataDirectory_Windows():
    return conf_strDataPath_Window() + "/"

def conf_strDefaultDataDirectory_Linux():
    return conf_strDataPath_Linux() + "/"

def conf_strHWDataDirectory_Windows():
    return "//172.16.9.1/Headwave/Data/"

def conf_strHWDataDirectory_Linux():
    return "/home/headwave/Desktop/Headwave/Data"

def conf_strHeadwaveAppName_Window():
    return "headwave"

def conf_strHeadwaveAppName_Linux():
    return "headwave"

def conf_strWorkingPath_Window():
    return "D:/Headwave/Workdir"

def conf_strWorkingPath_Linux():
    return "/home/headwave/Desktop/Workplace/WorkDir"

def conf_strPostfixVPName_Windows():
    return "_Windows"

def conf_strPostfixVPName_Linux():
    return "_Linux"

def conf_defaultImageComparisonMode():
    return "Histogram"

def conf_defaultImageComparisonParam1():
    return 256

def conf_defaultImageComparisonParam2():
    return 0.1

def conf_strWorkpacePath_Windows():
    return "//172.16.9.1/Headwave/Data/Testing/Workspaces_and_Data/Workspaces-TestScripts"

def conf_strWorkpacePath_Linux():
    return "/home/headwave/Desktop/Headwave/Data/Testing/Workspaces_and_Data/Workspaces-TestScripts"

def conf_strDataPath_Window():
    return "//172.16.9.1/Headwave"

def conf_strDataPath_Linux():
    return "/home/wesley.khiem.pham/Desktop/headwave"