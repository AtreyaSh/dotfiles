#!/usr/bin/env python3
#
# Copyright (C) 2016 James Murphy
# Licensed under the GPL version 2 only
#
# A battery indicator blocklet script for i3blocks

from subprocess import check_output

status = check_output(['acpi'], universal_newlines=True)

if not status:
    # stands for no battery found
    fulltext = "<span color='red'><span font='FontAwesome'>\uf00d \uf240</span></span>"
    percentleft = 100
else:
    # if there is more than one battery in one laptop, the percentage left is 
    # available for each battery separately, although state and remaining 
    # time for overall block is shown in the status of the first battery 
    batteries = status.split("\n")
    state_batteries=[]
    commasplitstatus_batteries=[]
    percentleft_batteries=[]
    for battery in batteries:
        if battery!='':
            state_batteries.append(battery.split(": ")[1].split(", ")[0])
            commasplitstatus = battery.split(", ")
            percentleft_batteries.append(int(commasplitstatus[1].rstrip("%\n")))
            commasplitstatus_batteries.append(commasplitstatus)
    state = state_batteries[0]
    commasplitstatus = commasplitstatus_batteries[0]
    percentleft = int(sum(percentleft_batteries)/len(percentleft_batteries))
    # stands for charging
    FA_LIGHTNING = "<span color='yellow'><span font='FontAwesome'>\uf0e7</span></span>"

    # stands for plugged in
    FA_PLUG = "<span font='FontAwesome'>\uf1e6</span>"

    fulltext = ""
    timeleft = ""

    if state == "Discharging":
        time = commasplitstatus[-1].split()[0]
        time = ":".join(time.split(":")[0:2])
        if time != "rate":
           timeleft = " ({})".format(time)
        else:
           timeleft = ""
    elif state == "Full":
        fulltext = FA_PLUG + " "
    elif state == "Unknown":
        fulltext = "<span font='FontAwesome'>\uf128</span> "
    else:
        fulltext = FA_LIGHTNING + " " + FA_PLUG + " "

    def color(percent):
        if percent < 10:
            # exit code 33 will turn background red
            return "#FFFFFF", "<span font='FontAwesome'>\uf244</span> "
        if percent < 20:
            return "#FF3300", "<span font='FontAwesome'>\uf243</span> "
        if percent < 30:
            return "#FF6600", "<span font='FontAwesome'>\uf243</span> "
        if percent < 40:
            return "#FF9900", "<span font='FontAwesome'>\uf243</span> "
        if percent < 50:
            return "#FFCC00", "<span font='FontAwesome'>\uf242</span> "
        if percent < 60:
            return "#FFFF00", "<span font='FontAwesome'>\uf242</span> "
        if percent < 70:
            return "#FFFF33", "<span font='FontAwesome'>\uf241</span> "
        if percent < 80:
            return "#FFFF66", "<span font='FontAwesome'>\uf241</span> "
        return "#FFFFFF", "<span font='FontAwesome'>\uf240</span> "

    form =  '<span color="{}">{}%</span>'
    col, icon = color(percentleft)
    if state == "Discharging":
        fulltext += icon
    fulltext += form.format(col, percentleft)
    fulltext += timeleft

print(fulltext)
print(fulltext)
if percentleft < 10:
    exit(33)