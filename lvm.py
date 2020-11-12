import os
import sys
while True:
	print('#############################-LVM Partitions-#############################')
	y=input('where to run a program\n press 1: for remotely \n press 2: for local vm\n press 3: to exit \n##########################################################\n')
	if (int(y)==1):
		ip=input('enter the ip address : ')
		w=0
		while w == 0:
			print('#############################-LVM Partitions-###########################')
			print("""press 1: To see the available disk
press 2: To create Physical Volume (PV)
press 3: To create Volume Group (VG)
press 4: To create Logical Volume (LV)
press 5: To extend Volume Group (VG)
press 6: To extend Logical Volume(LV)
press 7: To Format Logical Volume(LV)
press 8: To Mount Logical Volume(LV)
press 9: To UMount Logical Volume(LV)
press 10: To clean/scan Inode Table (to clean unwanted garbage path from Inode Table)
press 11: To resize the Logical Volume(LV)
press 12: To reduce the Logical Volume(LV) 	
press 13: To Display Physical Volume (PV)
press 14: To Display Volume Group (VG)
press 15: To Display Logical Volume(LV)
press 16: To resize the Logical Volume(LV)(To formate the remaining part)
press 17: To see the disk part
press 18: To remove the Physical Volume (PV)
press 19: To remove the Volume Group (VG)
press 20: To remove the Logical Volume (LV)""")
			print('########################################################################')
			c=int(input('Enter the choice : '))
			if (c == 1):
				os.system("ssh {} fdisk -l".format(ip))
			elif (c == 2):
				dn=input('enter the disk name :')
				os.system("ssh {} pvcreate {}".format(ip,dn))
			elif (c == 3):
				dn=input('enter the disk name :')
				os.system("ssh {} vgcreate {}".format(ip,dn))
			elif (c == 4):
				s=input('enter the size :')
				ln=input('give the name to LV :')
				dn=input('enter the VG name :')
				os.system("ssh {} lvcreate --size {} --name {} {}".format(ip,s,ln,dn))
			elif (c == 5):
				dn=input('enter the VG name :')
				n=input('enter the disk name :')
				os.system("ssh {} vgextend {} {}".format(ip,dn,n))
			elif (c == 6):
				s=input('enter the size :')
				dn=input('enter the LV name :')
				os.system("ssh {} lvextend --size +{} {}".format(ip,s,dn))
			elif (c == 7):
				dn=input('enter the LV name :')
				os.system("ssh {} mkfs.ext4 {}".format(ip,dn))
			elif (c == 8):
				fn=input('enter the dir name to mount :')
				os.system("ssh {} mkdir /{}".format(ip,fn))
				dn=input('enter LV name to mount :')
				os.system("ssh {} mount {} /{}".format(ip,dn,fn))
			elif (c == 9):
				fn=input('enter the dir name to umount :')
				os.system("ssh {} umount /{}".format(ip,fn))
			elif (c == 10):
				dn=input('enter the disk name :')
				os.system("ssh {} e2fsck -f {}".format(ip,dn))	
			elif (c == 11):
				dn=input('enter the  LV disk name :')
				s=input('enter the size to resize :')
				os.system("ssh {} resize2fs {} {}G".format(ip,dn,s))
			elif (c == 12):
				dn=input('enter the  LV disk name :')
				s=input('enter the size to reduce :')
				os.system("ssh {} lvreduce --size -{}GB {}".format(ip,s,dn))
			elif (c == 13):
				dn=input('enter the  PV name to display :')
				os.system("ssh {} pvdisplay {}".format(ip,dn))
			elif (c == 14):
				dn=input('enter the  VG name to display :')
				os.system("ssh {} vgdisplay {}".format(ip,dn))
			elif (c == 15):
				dn=input('enter the  VG name :')
				ln=input('enter the LV name :')
				os.system("ssh {} lvdisplay {}/{}".format(ip,dn,ln))
			elif (c == 16):
				ln=input('enter the LV name :')
				os.system("ssh {} resize2fs {}".format(ip,ln))
			elif (c == 17):
				os.system("ssh {} lsblk".format(ip))
			elif (c == 18):
				dn=input('enter the  PV name to delete :')
				os.system("ssh {} pvremove {}".format(ip,dn))
			elif (c == 19):
				dn=input('enter the  VG name to delete :')
				os.system("ssh {} vgremove {}".format(ip,dn))
			elif (c == 20):
				dn=input('enter the  LV name to delete :')						
				os.system("ssh {} lvremove {}".format(ip,dn))
			else:
				print('chose correct option')
			w=int(input('press 0 to continue or 1 for main menu :'))
	elif (int(y)==2):
		w=0
		while w == 0:
			print('#############################-LVM Partitions-############################')
			print("""press 1: To see the available disk
press 2: To create Physical Volume (PV)
press 3: To create Volume Group (VG)
press 4: To create Logical Volume (LV)
press 5: To extend Volume Group (VG)
press 6: To extend Logical Volume(LV)
press 7: To Format Logical Volume(LV)
press 8: To Mount Logical Volume(LV)
press 9: To UMount Logical Volume(LV)
press 10: To clean/scan Inode Table (to clean unwanted garbage path from Inode Table)
press 11: To resize the Logical Volume(LV)
press 12: To reduce the Logical Volume(LV) 	
press 13: To Display Physical Volume (PV)
press 14: To Display Volume Group (VG)
press 15: To Display Logical Volume(LV)
press 16: To resize the Logical Volume(LV)(To formate the remaining part)
press 17: To see the disk part
press 18: To remove the Physical Volume (PV)
press 19: To remove the Volume Group (VG)
press 20: To remove the Logical Volume (LV)""")
			print('#########################################################################')
			c=int(input('Enter the choice : '))
			if (c == 1):
				os.system("fdisk -l")
			elif (c == 2):
				dn=input('enter the disk name :')
				os.system("pvcreate {}".format(dn))
			elif (c == 3):
				dn=input('enter the disk name :')
				os.system("vgcreate {}".format(dn))
			elif (c == 4):
				s=input('enter the size :')
				ln=input('give the name to LV :')
				dn=input('enter the VG name :')
				os.system("lvcreate --size {} --name {} {}".format(s,ln,dn))
			elif (c == 5):
				dn=input('enter the VG name :')
				n=input('enter the disk name :')
				os.system("vgextend {} {}".format(dn,n))
			elif (c == 6):
				s=input('enter the size :')
				dn=input('enter the LV name :')
				os.system("lvextend --size +{} {}".format(s,dn))
			elif (c == 7):
				dn=input('enter the LV name :')
				os.system("mkfs.ext4 {}".format(dn))
			elif (c == 8):
				fn=input('enter the dir name to mount :')
				os.system("mkdir /{}".format(fn))
				dn=input('enter LV name to mount :')
				os.system("mount {} /{}".format(dn,fn))
			elif (c == 9):
				fn=input('enter the dir name to umount :')
				os.system("umount /{}".format(fn))
			elif (c == 10):
				dn=input('enter the disk name :')
				os.system("e2fsck -f {}".format(dn))	
			elif (c == 11):
				dn=input('enter the  LV disk name :')
				s=input('enter the size to resize :')
				os.system("resize2fs {} {}G".format(dn,s))
			elif (c == 12):
				dn=input('enter the  LV disk name :')
				s=input('enter the size to reduce :')
				os.system("lvreduce --size -{}GB {}".format(s,dn))
			elif (c == 13):
				dn=input('enter the  PV name to display :')
				os.system("pvdisplay {}".format(dn))
			elif (c == 14):
				dn=input('enter the  VG name to display :')
				os.system("vgdisplay {}".format(dn))
			elif (c == 15):
				dn=input('enter the  VG name :')
				ln=input('enter the LV name :')
				os.system("lvdisplay {}/{}".format(dn,ln))
			elif (c == 16):
				ln=input('enter the LV name :')
				os.system("resize2fs {}".format(ln))
			elif (c == 17):
				os.system("lsblk")
			elif (c == 18):
				dn=input('enter the  PV name to delete :')
				os.system("pvremove {}".format(dn))
			elif (c == 19):
				dn=input('enter the  VG name to delete :')
				os.system("vgremove {}".format(dn))
			elif (c == 20):
				dn=input('enter the  LV name to delete :')						
				os.system("lvremove {}".format(dn))
			else:
				print('chose correct option')
			w=int(input('press 0 to continue or 1 for main menu :'))
	elif(int(y) == 3):
		sys.exit()		
	else:
 		print('chose correct option')
