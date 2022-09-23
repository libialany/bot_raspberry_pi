### Start
> install

mkdir python_bot

cd python_bot

python -m venv venv

source venv/bin/activate

pip install discord.py

> basics

app_get_token.py

app_hello.py

app_rules_talk.py

app_get_talk.py

app_make_functions.py

app_welcome.py

app_list_members.py

> errors

__discord.py is an event-driven system. This focus on events extends even to exceptions__

> types of functions

1. built-in `on_message()`

2. by your own `my_function_cats()`

>  Class Both and Client

__A Bot is a subclass of Client that adds a little bit of extra functionality that is useful when you’re creating bot users.__

__bot.event like before, you use bot.command()__

__command must be prefixed__


> module Discord.py **Info**



[the module info](https://discordpy.readthedocs.io/en/stable/)

feature

`Optimised for both speed and memory`

[The best section to read](https://discordpy.readthedocs.io/en/stable/faq.html)


> FIX 1

TypeError: __init__() missing 1 required keyword-only argument: 'intents'

https://stackoverflow.com/questions/71959420/client-init-missing-1-required-keyword-only-argument-intents

__intents in commands__

https://stackoverflow.com/questions/71950432/how-to-resolve-the-following-error-in-discord-py-typeerror-init-missing

> importance of intents

https://discordpy.readthedocs.io/en/latest/intents.html

same like skill

example : enable member list skill

``intents.members = True``

![dev](https://github.com/libialany/bot_raspberry_pi/blob/main/images/permission.PNG)


> class members

https://discordpy.readthedocs.io/en/latest/api.html?highlight=voice_state#discord.Member.system

> async 

https://stackoverflow.com/questions/56914557/nonetype-object-has-no-attribute-send-when-work-with-discord-for-python

> mixing with apis

https://realpython.com/python-api/
