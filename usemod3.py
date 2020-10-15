from cja.db.utils.mymod import *  # import everything that does NOT start with _

spam()
ham()
print(ANIMALS)

print(Thing())


# import MODULE
# from MODULE import name1, name2, ...
# from MODULE import *
# import MODULE as ALIAS
# from MODULE import name1 as alias1, name2, name3 as alias3

from cja.db.utils import mymod as mm

mm.spam()

