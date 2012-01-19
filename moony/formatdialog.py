# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_formatdialog
import time
import subprocess
import os.path

class formatDialog(QDialog,ui_formatdialog.Ui_formatDialog):
    def __init__(self,parent=None):
        super(formatDialog,self).__init__(parent)
        self.setupUi(self)
        self.setVisible(False)

    def findfstype(self,fsinfo):
        self.forfstype.setText(fsinfo[0])  
        self.startFormat(fsinfo)

    def startFormat(self,fsinfo):
        devfile=fsinfo[1]
        if not os.path.exists(devfile):
            QMessageBox.critical(None,"No Devices Found","Sorry, %s is not found. Check that you have plugged the device"%(fsinfo[1]))
            self.close()
        else:
            self.setVisible(True)
        for x in range(11):
            if x!=7:
                self.formatprogressBar.setValue(x)
            else:
                filesystem=fsinfo[0]
                devfile=fsinfo[1]
                option1=str(fsinfo[2]).strip()
                option2=str(fsinfo[3]).strip()
                option3=str(fsinfo[4]).strip()
                option4=str(fsinfo[5]).strip()
                option5=str(fsinfo[6]).strip()
                if filesystem=="vfat":
                    command="mkfs.vfat "+devfile+" "
                elif filesystem=="ext2":
                    command="mkfs.ext2 "+devfile+" "
                elif filesystem=="ext3":
                    command="mkfs.ext3 "+devfile+" "
                elif filesystem=="xfs":
                    command="mkfs.xfs "+devfile+" "
                if len(option1)!=0:
                    if filesystem=="vfat":
                        command=command+"-n"+option1+" "
                    elif filesystem=="ext2" or "ext3" or "xfs":
                        command=command+"-L"+option1+" "
                if len(option2)!=0:
                    if filesystem=="vfat":
                        command=command+"-i"+option2+" "
                    elif filesystem=="ext2" or "ext3":
                        command=command+"-U"+option2+" "
                    elif filesystem=="xfs":
                        command=command+"-b"+option2+" "
                if len(option3)!=0:
                    if filesystem=="vfat":
                        command=command+"-F"+option3+" "
                    elif filesystem=="ext2" or "ext3":
                        command=command+"-b"+option3+" "
                    elif filesystem=="xfs":
                        command=command+"-s"+option3+" "
                if len(option4)!=0:
                    if filesystem=="vfat":
                        command=command+"-f"+option4+" "
                    elif filesystem=="ext2" or "ext3":
                        command=command+"-f"+option4+" "
                if len(option5)!=0:
                    if filesystem=="vfat":
                        command=command+"-s"+option5+" "
                    elif filesystem=="ext2" or "ext3":
                        command=command+"-i"+option5+" "
                ret=subprocess.call([command],shell=True)
                if ret==127:
                    QMessageBox.critical(self,"Install Packages","No software package for %s is present in your system."%(command))
                    self.label_3.setText("Format Unsuccessfull")
                    self.formatprogressBar.setValue(0)
        self.formatokpushButton.setEnabled(True)
        self.label_3.setText("Format Successfully Completed")
        self.formatprogressBar.setValue(10)

    def closeEvent(self,event):
        pass    
            
if __name__=="__main__":
  import sys
  app=QApplication(sys.argv)
  form=formatDialog()
  form.show()
  app.exec_()
