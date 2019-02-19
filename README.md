# wox-Recall
A wox plugin - Recall for Future.

## Description:
Our time is valuable. Our brain hard disk is valuable. And **that's why** I create this little plugin on WOX to help us recall some trivial things.

## Usages:
The main idea is, this plugin stores Key-value pairs to remenber trivial things for you.

For example, if you(I) don't want to put your(my) school ID number in your(my) precious brain hard disk but you(I) still need it:
1. Download [Wox](http://www.wox.one/) and install it.
2. Type **"wpm install Recall"** and install the Plugin
3. **"Alt+space"** to call out Wox.
4. **"recall -a {key} {value}"** to add a key-value pair. If key exists, do nothing. In your case: "recall -a ID 12345678".
5. **"recall {key}"** to query a key. This key will be treated as this ".\*k.\*e.\*y.\*"(a regular expression). In your case: "recall id".
6. Select a result and hit Enter. The value will **be copied to clipboard**.
7. **"recall -d {key}"** to delete a key. This key should be exactly the same to the one in stored file.
8. **"recall -u {key} {new_value}"**. If key NOT exists, do nothing.
9. **"recall -r {RE}"**. Query in reqular expression.
10. **"recall -h"**. Get a help.
11. **"recall ."** - Get all the list.
12. To clear all the items, just go to the folder and replace all the stuff in "items.json" to "{}".

###
![Example](/Images/recall.gif)

