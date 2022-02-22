#Scanning Software

#Scans image for the RGB values at the set locations to translate to velocity values
def Scan():
    f = open('VelRGBLog.txt')
    VelRGBList = []
    for x in f:
        VelRGBList += f.read().splitlines()

    f.close()
    VelRGBDict = {}
    for x in VelRGBList:
        y = 1
        for i in x:
            try:
                a = int(x[:y])
                y += 1
            except: 
                VelRGBDict[x[:y-2]] = x[y-1:]
    return VelRGBDict
