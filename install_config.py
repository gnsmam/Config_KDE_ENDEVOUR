import os
package_string = ""
packages_file = open("packages.txt", "r")
for package in packages_file:
    package = package.rstrip("\n")
    package = package + " "
    package_string = package_string + package

os.system("echo ###UPDATING PACKAGES###")
os.system
os.system("sudo pacman -Syu")
os.system("sudo pacman -S " + package_string)


#foot config install
os.system("echo ###INSTALLING FOOT CONFIG###")
if os.path.exists("$HOME/.config/foot/"):
    os.system("cp -rf foot.ini $HOME/.config/foot/")
else:
    os.system("mkdir $HOME/.config/foot/")
    os.system("cp -rf fuzzel.ini $HOME/.config/foot/")


#fuzzel config install
os.system("echo ###INSTALLING FUZZEL CONFIG###")
if os.path.exists("$HOME/.config/fuzzel/"):
    os.system("cp -rf fuzzel.ini $HOME/.config/fuzzel/")
else:
    os.system("mkdir $HOME/.config/fuzzel/")
    os.system("cp -rf fuzzel.ini $HOME/.config/fuzzel/")

#waybar config install 
os.system("echo ###INSTALLING WAYBAR CONFIG###")
os.system("cp -rf waybar $HOME/.config/")

#add waybar to autostart
os.system("echo ###ADDING WAYBAR TO AUTOSTART###")
if os.path.exists("$HOME/.config/autostart/waybar.desktop"):
    os.system("cp -rf waybar.dekstop $HOME/.config/autostart/waybar.desktop")
else:
    os.system("cp -rf waybar.dekstop $HOME/.config/autostart/")

#remove kde panels
os.system("echo ###REMOVING KDE PANELS###")
os.system("rm $HOME/.config/plasma-org.kde.plasma.desktop-appletsrc")

os.system("echo ###Please go into the KDE settings panel and import keybindings from 'keybindings.kksrc' file manually. \nAfter that reboot your PC###")
