# -*- mode: python -*-
import os

a = Analysis(['.\\imageCodePractice.py'],
             pathex=['.\\tmp'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)


imageFolder = 'image\\10_18'
extra_datas = []

for fileName in os.listdir(imageFolder):
    print fileName
    path = os.path.join(imageFolder, fileName)
    if os.path.isfile(path):
        imgInfo = (path, path, 'DATA')
        
        extra_datas.append(imgInfo)
        
a.datas += extra_datas
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='imageCodePractice.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True)

