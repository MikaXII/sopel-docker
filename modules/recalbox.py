# coding=utf-8
# Copyright 2010-2011, Michael Yanovich, Alek Rollyson, and Elsie Powell
# Copyright © 2012, Elad Alfassa <elad@fedoraproject.org>
# Licensed under the Eiffel Forum License 2.
from __future__ import unicode_literals, absolute_import, print_function, division
import os
import re
from sopel import formatting
from sopel.module import commands, priority, OWNER, ADMIN, OP, HALFOP, require_privilege, require_chanmsg, require_privmsg, require_admin
from sopel.tools import Identifier
from random import randrange, uniform

@require_chanmsg
@commands('bite')
@priority('low')
def bite(bot, trigger):

    beginStr = "c"
    for x in range(randrange(1,15)):
        beginStr += "="
    endStr = beginStr + "3"
    bot.say(trigger.nick + " " + endStr)

@require_chanmsg
@commands('boobs')
@priority('low')
def boobs(bot, trigger):
    switcher = {
            0: "( . Y . )",
            1: "( . )( . )",
            2: "(o)(o)",
            3: "(•)(•)",
            4: "\./\./",
            5: "(.)U(.)",
        }
    
    bot.say(trigger.nick + " " + switcher.get(randrange(0,5), "(.)(.)"))
