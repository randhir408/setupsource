import cx_Freeze
import sys
base=None
if sys.platform=="win32":#same
    base ="Win32GUI"
shortcut_table=[
    ("DesktopShortcut", #shortcut
     "DesktopFolder",#Directory_
     "Car racing game",#Name give any name
     "TARGETDIR", #Component_
     "[TARGETDIR]\game.exe",#file name
     None, #Argument
     None, #Description
     None,#Hotkey
     None,#Icon
     None,#IconIndex
     None,#ShowCmd #all same
    "TARGETDIR", #Wkdir
   )
]
msi_date={"Shortcut":shortcut_table}

#change some default MSI option specify the use of the above table
bdist_msi_option={'data':msi_date}#same

executables=[cx_Freeze.Executable(script="game.py",icon='car.ico',base=base)]

cx_Freeze.setup(
    version="2.0",#give any version
    description="Pygame car racing game",#give any description
    author="Randhirkumar",
    name="car racing",#give any name
    option={"build_exe":{"packages":["pygame"],#same
                         "include_file":['back.jpg','back_ground.jpg','car.png','enemy_car_1.png','enemy_car_2.png','car.ico']},#tags all including file
            "bdist_msi": bdist_msi_option,
            },
    executables=executables#all same

    )
