import subprocess
import sys
import PyInstaller.__main__


def Pack(pythonfile: str, *,
         path: str | None = None,
         name: str | None = None,
         icon: str | None = None,
         nonconsole: bool = False,
         filestyle: str = 'onedir', # 或 onefile
         distpath: str | None = None,
         workpath: str | None = None,
         specpath: str | None = None,
         coverdist: bool = False,
         coverwork: bool = False,
         loglevel: str = 'ERROR', # 或 TRACE DEBUG INFO WARN ERROR CRITICAL
         datas: list[(str, str)] = [], # [(编译时文件位置, 运行时文件位置), ...]
         binaries: list[(str, str)] = [], # 同上
         moreimportpaths: list[str] = [], # 额外导入的包
         morehiddenimports: list[str] = [], # 额外隐藏导入的包
         excludemodules: list[str] = [], # 排除的包
         runtimetmpdir: str | None = None # 运行时临时目录，用于onefile且有datas或binary时
         ):

    commands = [pythonfile]

    if name is not None:
        commands.append('-n ' + name)
    if icon is not None:
        commands.append('-i ' + icon)
    if nonconsole:
        commands.append('--noconsole')

    if filestyle == 'onefile':
        commands.append('--onefile')
    elif filestyle == 'onedir':
        commands.append('--onedir')
    else:
        raise ValueError('filestyle must be onefile or onedir')

    if distpath is not None:
        commands.append('--distpath ' + distpath)
    if workpath is not None:
        commands.append('--workpath ' + workpath)
    if specpath is not None:
        commands.append('--specpath ' + specpath)

    if coverdist:
        commands.append('-y')
    if coverwork:
        commands.append('-clean')
    
    if loglevel != 'INFO':
        commands.append('--log-level ' + loglevel)

    if datas:
        for data in datas:
            commands.append(f'--add-data "{data[0]};{data[1]}"')
    if binaries:
        for binary in binaries:
            commands.append(f'--add-binary "{binary[0]};{binary[1]}"')
    
    if moreimportpaths:
        for importpath in moreimportpaths:
            commands.append('--paths ' + importpath)
    if morehiddenimports:
        for module in morehiddenimports:
            commands.append('--hidden-import ' + module)
    if excludemodules:
        for module in excludemodules:
            commands.append('--exclude-module ' + module)
    
    if runtimetmpdir is not None:
        commands.append('--runtime-tmpdir ' + runtimetmpdir)

    #PyInstaller.__main__.run(commands)
    commands = ['pyinstaller'] + commands
    commands = ' '.join(commands)
    #print(commands)
    subprocess.run(commands, cwd=path)
