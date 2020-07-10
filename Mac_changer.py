#! usr/bin/env python3

import platform
import subprocess
import argparse
import re


def get_argument():  # Argparse use for Argument which you follow as an instruction
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="Interface of the Network", action="store")
    parser.add_argument("-m", "--mac", help="Introduce the new Mac Address", action="store")
    parser.add_argument("-a", "--about", help="About the Developer of this Program")
    return parser.parse_args()


args = get_argument()


def change_mac(interface, new_mac):  # Subprocess use for Linux Command
    subprocess.call(["ifconfig " + str(interface) + " down"], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " hw ether " + str(new_mac)], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " up"], shell=True)


def current_mac():
    ifconfig_result = subprocess.check_output(["ifconfig ", args.interface], shell=True)
    current_mac0 = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w ", str(ifconfig_result))
    return current_mac0


def main():
    if platform.system() != 'Linux':       # Check the Operating System
        print("This Program only developed for Linux Destro.")
    if args.about is True:
        print("[*] I am Akash Developer of this Program")
        print("[*] It was Developed for python3")

    elif args.interface is not None and args.mac is not None:   # Interface and Mac is not empty
        current_mac0 = current_mac()
        print("[*] Your Mac Address for " + str(args.interface) + " is " + str(current_mac0.group(0)))
        change_mac(args.interface, args.mac)
        current_mac1 = current_mac()
        if current_mac0.group(0) != current_mac1.group(0):
            print("[+] Mac Address Successfully changed ")
            print("[+] Your New Mac_Address is " + str(current_mac1.group(0)))
            print("[+] Your Original Mac Address return after Reboot ")
            print("[+] Script created by Akash. ")
        else:
            print("[-] something went wrong")
            print("[-] Make sure that you are running it as Root")

    elif args.interface is None:  # when interface is empty
        print("[-] Please specify the Correct Mac_Address or an Interface")
        print("[-] Make sure you use -i / --interface(eth0 or Wlan) for Interface")

    elif re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w ", str(args.mac)) is None and args.mac is None:
        print("[-] You didn't pass the Valid Mac Address")
        print("[-] Make sure you use -m / --mac XX:XX:XX:XX:XX:XX for MAC Address")
        print("[-] Make sure you use alphanumeric characters for Ex- 11:22:33:44:55:66")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("[-] Something went wrong")
        print("[-] It might be a wrong interface name")
        print("[-] If ifconfig is not found try- sudo apt install net-tools")
