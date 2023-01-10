### sakinyje iesko raidziu
sakinys = "studentai sekmingai mokes su python ieskot tekste slieku..."

ieskom = input("ko ieskom?: ")

for raide in sakinys:
    if ieskom == raide:
        print("radom")
        break
else:
    print(f"neradom {ieskom}. ")
