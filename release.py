#!/usr/bin/env python

#======================================
# Disactive  screensaver start version 2.0
#=====================================

import os
import shutil
import re

#=======================================================
# SUBROUTINES
#=======================================================

def reset_SSD_LDOT(FileName):
    if(os.path.isfile(FileName)):
	TargetFile = open(FileName, "r")
	FileLines = TargetFile.read().splitlines()
	TargetFile.close()
	print "Lines in {0}: {1}".format(FileName, len(FileLines))
	
	IsModified = 0
	Pointer = 0 
	for CurrentString in FileLines:
	    #print CurrentString
	    compiled_exp_ssd = re.compile(reScreenSaverDelay)
	    compiled_exp_ldot = re.compile(reLockerDpmsOffTimeout)
	    qty_ssd = compiled_exp_ssd.search(CurrentString)
	    qty_ldot = compiled_exp_ldot.search(CurrentString)
	    IsWatchAble = 0
	    if(qty_ssd != None):
		NewString = "ScreenSaverDelay=0"
		print "{0} --> {1}".format(CurrentString, NewString) 
		FileLines[Pointer] = NewString
		IsWatchAble = 1
	    if(qty_ldot != None):
		NewString = "LockerDpmsOffTimeout=0"
		print "{0} --> {1}".format(CurrentString, NewString)
		FileLines[Pointer] = NewString
		IsWatchAble = 1
	    # Watch current value
	    if(IsWatchAble == 1):
		IsModified = 1
		#print "!!!Check current value: {0} Pointer: {1}".format(CurrentString, Pointer)
	    Pointer = Pointer + 1
	# End of for cycle
	#
	# Check file modification
	if(IsModified > 0):
	    # Create backup file
	    FileNameBackup = FullFileName + "_"
	    shutil.copy2(FileName, FileNameBackup)
	    # Store current file
	    #FileName = FileName + "X"
	    TargetFile = open(FileName, "w")
	    for Item in FileLines:
		TargetFile.write("{0}\n".format(Item))
	    TargetFile.close()
	        
    else:
	print "File {0} not exist".format(FileName)

#=======================================================
# MAIN PROGRAM
#======================================================

#================================================================
#Create file "10-monitor.conf" in directory "/etc/X11/xorg.conf.d"
#================================================================

FileName1 = "10-monitor.conf"
DirName1 = "/etc/X11/xorg.conf.d"

FileBody = ""
FileBody += 'Section "Monitor"\n'
FileBody += '  Identifier "LVDS0"\n'
FileBody += '  Option "DPMS" "false"\n'
FileBody += 'EndSection\n'
FileBody += '\n'
FileBody += 'Section "ServerLayout"\n'
FileBody += '  Identifier "ServerLayout0"\n'
FileBody += '  Option "StandbyTime" "0"\n'
FileBody += '  Option "SuspendTime" "0"\n'
FileBody += '  Option "BlankTime" "0"\n'
FileBody += 'EndSection\n'


#print "\n FileName1: %s" % FileName1
#print "\n DirName1: %s" % DirName1
#print FileBody

# Check directory existance
if os.path.exists(DirName1):
    print "Target directory %s exists\n" % DirName1
else:
    print "Target directory %s not found\n" % DirName1
    os.mkdir(DirName1)
    print "Target directory %s created\n" % DirName1

# Create or owerwrite file
  
FullFileName = DirName1 + '/' + FileName1
#print "FullFileName: %s " % FullFileName

TargetFile = open(FullFileName, "w")
TargetFile.write(FileBody)
TargetFile.close()
print "Target file %s created\n" % FullFileName

#=======================================================
# Append string "/usr/bin/xset -dpms" to file "/etc/X11/fly-dm/Xsetup"
#=======================================================

FileName2 = "/etc/X11/fly-dm/Xsetup"
BackupFileName = FileName2 + "_"
AppendString = "/usr/bin/xset -dpms"

if os.path.isfile(FileName2):
    TargetFile = open(FileName2, "r")
    ViewString = TargetFile.read()
#    print ViewString
    BackupFile = open(BackupFileName, "w")
    BackupFile.write(ViewString)
    BackupFile.close()
    TargetFile = open(FileName2, "a")
    TargetFile.write("\n")
    TargetFile.write(AppendString)
    TargetFile.write("\n")
    TargetFile.close()
    print"Append string '%s' to %s file"% (AppendString, FileName2)
else:
    print "Target file %s not exist\n" % FileName2

#=======================================================
# Set ScreenSaverDelay=0 in files directory "~/.fly/theme"
#=======================================================

DirName3 = "/home/user/.fly/theme"
DirName4 = "/usr/share/fly-wm/theme"

FileName1 = "default.themerc.mini"
FileName2 = "default.themerc"
FileName3 = "current.themerc"
FileName4 = "default.themerc.fly-mini"
FileName5 = "default.themerc.fly-mobile"
FileName6 = "default.themerc.fly-tablet"

reScreenSaverDelay = "^ScreenSaverDelay=[^0][0-9]*\w*"
reLockerDpmsOffTimeout = "^LockerDpmsOffTimeout=[^0][0-9]*\w*"

#FileList = os.listdir(DirName4)
#print FileList
#exit(0)

FullFileName = DirName3 + '/' + FileName1
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName3 + '/' + FileName2
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName3 + '/' + FileName3
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName3 + '/' + FileName4
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName3 + '/' + FileName5
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName3 + '/' + FileName6
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName4 + '/' + FileName1
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName4 + '/' + FileName2
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName4 + '/' + FileName3
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName4 + '/' + FileName4
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName4 + '/' + FileName5
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)

FullFileName = DirName4 + '/' + FileName6
print "> Operate {0}".format(FullFileName)
reset_SSD_LDOT(FullFileName)



