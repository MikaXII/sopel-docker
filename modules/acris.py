# coding=utf-8
# Copyright 2010-2011, Michael Yanovich, Alek Rollyson, and Elsie Powell
# Copyright © 2012, Elad Alfassa <elad@fedoraproject.org>
# Licensed under the Eiffel Forum License 2.
from __future__ import unicode_literals, absolute_import, print_function, division
import os
import re
from sopel import formatting
from sopel.module import commands, priority, OWNER, ADMIN, OP, HALFOP, require_privilege, require_chanmsg, require_privmsg
from sopel.tools import Identifier


@require_chanmsg
@commands('toolboxfr')
@priority('low')
def toolboxfr(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/toolsbox-%28FR%29")

@require_chanmsg
@commands('toolboxen')
@priority('low')
def toolboxen(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/toolbox-%28EN%29")

@require_chanmsg
@commands('arcadefr')
@priority('low')
def arcadefr(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/L%27arcade-facile-sur-Recalbox-%28FR%29")
    bot.say("https://github.com/recalbox/recalbox-os/wiki/L%27arcade-avanc%C3%A9e-sur-Recalbox-%28FR%29")
    bot.say("https://github.com/recalbox/recalbox-os/wiki/V%C3%A9rifier-la-version-de-vos-roms-avec-clrmamepro-%28FR%29")

@require_chanmsg
@commands('arcadeen')
@priority('low')
def arcadeen(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/Easy-Arcade-on-Recalbox-%28EN%29")
    bot.say("https://github.com/recalbox/recalbox-os/wiki/Advanced-Arcade-on-Recalbox-%28EN%29")
    bot.say("https://github.com/recalbox/recalbox-os/wiki/Check-your-roms-version-with-clrmamepro-%28EN%2")

@require_chanmsg
@commands('moonlightfr')
@priority('low')
def moonlightfr(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/Configuration-moonlight-%28FR%29")

@require_chanmsg
@commands('moonlighten')
@priority('low')
def moonlighten(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/Setup-moonlight-%28EN%29")

@require_chanmsg
@commands('winscpfr')
@priority('low')
def winscpfr(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/acces-via-WinSCP-%28FR%29")

@require_chanmsg
@commands('rwfr')
@priority('low')
def rwfr(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/partition-en-ecriture-%28FR%29")

@require_chanmsg
@commands('usbkeyfr')
@priority('low')
def usbkeyfr(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/Utiliser-un-p%C3%A9riph%C3%A9rique-USB-de-stockage-sur-recalbox-%28FR%29")

@require_chanmsg
@commands('usbkeyen')
@priority('low')
def usbkeyen(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/Use-an-external-usb-storage-device-on-recalbox-%28EN%29")

@require_chanmsg
@commands('managerfr')
@priority('low')
def managerfr(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/recalbox-manager-WEB-interface-%28FR%29")

@require_chanmsg
@commands('videoen')
@priority('low')
def videoen(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/Video-configuration-detailled-%28EN%29")

@require_chanmsg
@commands('supportfr')
@priority('low')
def supportfr(bot, trigger):
    bot.say("https://github.com/recalbox/recalbox-os/wiki/Recalbox-support--%28FR%29")
