# -*- mode: python -*-

block_cipher = None


a = Analysis(['../a/translate_GUI.py'],
             pathex=['/home/pipidi/Downloads/PyInstaller-3.3.1/translate_GUI'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='translate_GUI',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
