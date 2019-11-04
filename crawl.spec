# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['crawl.py'],
             pathex=['E:\\git\\aliexpress\\aliImges'],
             binaries=[],
             datas=[],
             hiddenimports=["imagesAliexpress.items","imagesAliexpress.middlewares",'imagesAliexpress.pipelines','imagesAliexpress.settings','imagesAliexpress.spiders'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='crawl',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='crawl')
