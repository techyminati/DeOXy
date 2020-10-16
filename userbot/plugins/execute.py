from telethon import errors, functions, types
import inspect
import traceback
import asyncio
import sys
import os


@client.on(events(pattern="execute"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    cmd = event.text.split(" ", maxsplit=1)[1]
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "**EXEC**: `{}` \n\n **OUTPUT**: \n`{}` \n".format(cmd, evaluation)

    if len(final_output) > 4096:
        with open("evaluation.txt", "w") as f:
            f.write(final_output)
        await client.send_file(
            event.chat_id,
            f.name,
            force_document=True,
            allow_cache=False,
            caption=f"**PROCCESSED**: `{cmd}`",
            reply_to=reply_to_id
        )
        await event.delete()
        os.remove(f.name)
    else:
        await event.edit(final_output)


async def aexec(code, event):
    exec(
        f'async def __aexec(event): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](event)

HELPER.update({
    "": "\
**Requested Module --> Executer**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.execute```\
\nUsage: Executes the given code\
"
})  
HELPER.
