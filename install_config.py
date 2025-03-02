import os
package_string = ""
packages_file = open("packages.txt", "r")
for package in packages_file:
    package = package.rstrip("\n")
    package = package + " "
    package_string = package_string + package

#print(package_string)
os.system("sudo pacman -Syu")
os.system("sudo pacman -S " + package_string)

#foot config install
if os.path.exists("$HOME/.config/foot/"):
    os.system("cp -rf foot.ini $HOME/.config/foot/")
else:
    os.system("mkdir $HOME/.config/foot/")
    os.system("cp -rf fuzzel.ini $HOME/.config/foot/")


#fuzzel config install
if os.path.exists("$HOME/.config/fuzzel/"):
    os.system("cp -rf fuzzel.ini $HOME/.config/fuzzel/")
else:
    os.system("mkdir $HOME/.config/fuzzel/")
    os.system("cp -rf fuzzel.ini $HOME/.config/fuzzel/")

#waybar config install 
os.system("cp -rf waybar $HOME/.config/")
