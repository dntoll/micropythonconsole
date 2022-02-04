#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#
from ANSIEscape import ANSIEscape
from Value import Value
from ValueView import ValueView



class Console:
    #https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#8-colors
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear()
        self.values = []
    
    def show(self):
        for val in self.values:
            self.buffer += val.get(self.height)
        script = ""
        script += ANSIEscape.goToXY(0,0)
        script += self.buffer
        print(script + ANSIEscape.goToXY(0, self.height) )
        self.clear()

    def frame(self, char='*'):
        self.buffer += ANSIEscape.goToXY(0,0)
        self.printAt( '/' + (self.width-2) *  '-' + '\\', 0,0, "Blue", "Black")
        for n in range(2, self.height):
            self.printAt('|', 0, n, "Blue", "Black")
            self.printAt('|', self.width, n, "Blue", "Black")
        self.printAt('\\' + (self.width-2)*'-' + '/', 0, self.height, "Blue", "Black")
        ##for y in range(0, self.height):
        #    self.buffer
    def createValue(self, title, unit, decimals, x, y, color, background, detail):

        val = Value()
        valueView = ValueView(val, title, unit, decimals, x, y, color, background, detail)
        
        self.values.append(valueView)
        return val
    
    def clearScreen(self):
        print(ANSIEscape.clearScreen())

    def clear(self):
        self.buffer = "";

    def printAt(self, text, x, y, color="White", background="Black"):
        self.buffer += ANSIEscape.goToXY(x, y)
        self.buffer += ANSIEscape.getBackgroundColor(background) + ANSIEscape.getTextColor(color) + text + ANSIEscape.getResetCode()
    
    


    