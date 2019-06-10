#!/usr/bin/env python3
#sample method overriding
#made by Antonius Ringlayer
#www.jasaplus.com - www.ringlayer.com
#prepare new class
class Kelas:
    def Method1(self):
        print("original method code block")

#inheritance
class KelasDescendant(Kelas):
    #overriding
    def Method1(self):
        print("Method overriding")

kelas2 = KelasDescendant()
kelas2.Method1()
