# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

py_files = [
    'main.py',
    'render_html.py',
    'writeXLSX.py',
    'config.py',
    'UIGF_converter.py',
    'gachaMetadata.py',
]
exe_name = 'genshin-gacha-export'
icon_path = 'ys.ico'

a = Analysis(py_files,
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['capture'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=exe_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon=icon_path)
