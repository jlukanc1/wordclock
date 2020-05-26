# SPDX-License-Identifier: LGPL-3.0-or-later
# wordclock by jlukanc1

import wasp
import icons

numtime = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 21: 'Twenty One', 22: 'Twenty Two', \
            23: 'Twenty Three', 24: 'Twenty Four', 25: 'Twenty Five', 26: 'Twenty Six', \
            27: 'Twenty Seven', 28: 'Twenty Eight', 29: 'Twenty Nine', \
            30: 'Thirty', 31: 'Thirty One', 32: 'Thirty Two', 33: 'Thirty Three', 34: 'Thirty Four', \
            35: 'Thirty Five', 36: 'Thirty Six', 37: 'Thirty Seven', 38: 'Thirty Eight', \
            39: 'Thirty Nine', 40: 'Fourty', 41: 'Fourty One', 42: 'Fourty Two', \
            43: 'Fourty Three', 44: 'Fourty Four', 45: 'Fourty Five', 46: 'Fourty Six', 47: 'Fourty Seven', \
            48: 'Fourty Eight', 49: 'Fourty Nine', 50: 'Fifty', 51: 'Fifty One', 52: 'Fifty Two', \
            53: 'Fifty Three', 54: 'Fifty Four', 55: 'Fifty Five', 56: 'Fifty Six', \
            57: 'Fifty Seven', 58: 'Fifty Eight', 59: 'Fifty Nine', 60: 'Sixty', 0: 'Zero'}

MONTH = 'JanFebMarAprMayJunJulAugSepOctNovDec'

class WordClockApp():
    NAME = 'WClock'
    ICON = icons.clock

    def __init__(self):
        """Initialize the application."""
        self.meter = wasp.widgets.BatteryMeter()

        pass

    def foreground(self):
        """Activate the application."""
        draw = wasp.watch.drawable
        self.on_screen = ( -1, -1, -1, -1, -1, -1 )
        self.draw()
        wasp.system.request_tick(1000)

    def background(self):
        """De-activate the application."""
        pass

    def sleep(self):
        """Notify the application the device is about to sleep."""
        return False

    def wake(self):
        """Notify the application the device is waking up."""
        self.update()
        pass

    def press(self, button, state):
        """Notify the application of a button-press event."""


    def swipe(self, event):
        """Notify the application of a touchscreen swipe event."""


    def tick(self, ticks):
        """Notify the application that its periodic tick is due."""
        self.update()
        pass

    def touch(self, event):
        """Notify the application of a touchscreen touch event."""


    def draw(self):
        """Draw the display from scratch."""
        draw = wasp.watch.drawable

        draw.fill()
        self.on_screen = ( -1, -1, -1, -1, -1, -1 )
        self.update()
        self.meter.draw()


    def update(self):
        """Update the dynamic parts of the application display."""
        now = wasp.watch.rtc.get_localtime()
        draw = wasp.watch.drawable

        if now[3] == self.on_screen[3] and now[4] == self.on_screen[4]:
            if now[5] != self.on_screen[5]:
                self.meter.update()
                self.on_screen = now
            return False
        minute = int(now[4])
        hour = int(now[3])

        draw.string('{}'.format(numtime[minute]), 0, 100, width=240)
        draw.string('{}'.format(numtime[hour]), 0, 60, width=240)

        self.on_screen = now
        month = now[1] - 1
        month = MONTH[month*3:(month+1)*3]
        draw.string('{} {} {}'.format(now[2], month, now[0]), 0, 180, width=240)

        self.meter.update()
        pass
