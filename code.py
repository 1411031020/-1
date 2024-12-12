# 創建 VBScript 檔案
vbs_content = '''
Set WScript.Shell = CreateObject("WScript.Shell")
WScript.Shell.SendKeys "^{TAB}"
'''

with open('/home/user/sendCtrlTab.vbs', 'w') as f:
    f.write(vbs_content)

# 創建 Batch 檔案
bat_content = '''
@echo off
cscript //nologo "%~dp0sendCtrlTab.vbs"
'''

with open('/home/user/pressCtrlTab.bat', 'w') as f:
    f.write(bat_content)

# 顯示檔案內容
print("=== sendCtrlTab.vbs 內容 ===")
print(vbs_content)
print("\n=== pressCtrlTab.bat 內容 ===")
print(bat_content)