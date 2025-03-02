import os
package_string = ""
packages_file = open("packages.txt", "r")
for package in packages_file:
    package = package.rstrip("\n")
    package = package + " "
    package_string = package_string + package

os.system
os.system("sudo pacman -Syu")
os.system("sudo pacman -S " + package_string)

#foot config install
if os.path.exists("$HOME/.config/foot/foot.ini"):
    os.system("rm -r $HOME/.config/foot/foot.ini")
    os.system("cp -rf foot.ini $HOME/.config/foot/")
else:
    os.system("mkdir $HOME/.config/foot/")
    os.system("cp -rf foot.ini $HOME/.config/foot/")

#fuzzel config install
if os.path.exists("$HOME/.config/fuzzel/"):
    os.system("rm -r $HOME/.config/fuzzel/fuzzel.ini")
    os.system("cp -rf fuzzel.ini $HOME/.config/fuzzel/")
else:
    os.system("mkdir $HOME/.config/fuzzel/")
    os.system("cp -rf fuzzel.ini $HOME/.config/fuzzel/")

#waybar config install 
os.system("cp -rf waybar $HOME/.config/")

#add waybar to autostart
if os.path.exists("$HOME/.config/autostart/waybar.desktop"):
    os.system("cp -rf waybar.desktop $HOME/.config/autostart/waybar.desktop")
else:
    os.system("cp -rf waybar.desktop $HOME/.config/autostart/")

#remove kde panels
os.system("rm $HOME/.config/plasma-org.kde.plasma.desktop-appletsrc")
