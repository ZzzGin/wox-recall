# wox-Recall
A wox plugin - Recall for Future.

## Description:
Our time is valuable. Our brain hard disk is valuable. And **that's why** I create this little plugin on WOX to help us recall some trivial things.

## Usages:
For example, if you(I) don't want to put your(my) school ID number in your(my) precious brain hard disk but you(I) still need it:
1. Download [Wox](http://www.wox.one/) and install it.
2. Type "wpm install Recall" and install the Plugin
5. **"Alt+space"** to call out Wox.
6. **"recall -a {key} {value}"** to add a key-value pair. If key exists, do nothing.
7. **"recall {key}"** to query a key. This key will be treated as this ".\*k.\*e.\*y.\*"(a regular expression). 
8. Select a result and hit Enter. The value will **be copied to clipboard**.
9. **"recall -d {key}"** to delete a key. This key should be exactly the same to the one in stored file.
10. **"recall -u {key} {new_value}"**. If key NOT exists, do nothing.
11. **"recall -r {RE}"**. Query in reqular expression.
12. **"recall -h"**. Get a help.
13. **"recall ."** - Get all the list.
14. To clear all the items, just go to the folder and replace all the stuff in "items.json" to "{}".
###
![Example](/Images/recall.gif)

