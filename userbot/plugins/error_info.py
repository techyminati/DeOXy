# Exclusive for PhoeniX Userbot.
# By @Techy05 (DON'T REMOVE THESE LINES)
#Ported to DeOXy
## Don't modify this module

from global_variables_sql import SYNTAX, MODULE_LIST, ERROR, ERROR_LIST

MODULE_LIST.append("errors")
SYNTAX.update({
    "errors": "\
**Getting issues while using 𝔡𝓔𝐎𝕩𝕐? Or a modules aren't working?**\
\nDon't worry, Let's fix them\
\n\n• `.errors`\
\nUsage: __Shows the list of known errors in Userbots__\
\n\n• `.solution <error_name>`\
\nUsage: __Shows the solution for the requested error/problem__\
"
})

ERROR_LIST.append("updater error")
ERROR.update({
    "updater error": "\
**So, you're having problems with updater. 𝔡𝓔𝐎𝕩𝕐 Service will fix it.**\
\n\nERROR: `Unfortunately, the directory /app does not seem to be a git repository.`\
\nSolution: __Use “.update now” and check again if it works.__\
\n__If it still doesn't work, then use “.chl” once.__\
\n\nERROR: `[UPDATER]: Looks like you are using your own custom branch (master). in that case, Updater is unable to identify which branch is to be merged. please checkout to any official branch`\
\nSolution: __Delete 𝔡𝓔𝐎𝕩𝕐 repo from your account. Refork__ [𝔡𝓔𝐎𝕩𝕐](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy). __Then Manual Deploy from Heroku to fix__\
\nIf you use custom fork, then please don't mess with branches.\
"
})
