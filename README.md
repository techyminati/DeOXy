# 𝔡𝓔𝐎𝕩𝕐 USERBOT
## Dev- [MrMobTechYT](https://t.me/CyberJalagam) 

# Thanks To   [HardcoreUserbot](https://github.com/Hack12R/HardcoreUserbot) // [X-tra-Telegram](https://github.com/Dark-Princ3/X-tra-Telegram) \\\ [The-TG-Bot-2.0](https://github.com/PriyamKalra/The-TG-Bot-2.0) For helping me out with the codes. Thank You Buggies ;-)


 ### DECLARATION/LICENCE AGREEMENT

I herby confirm that the base of this userbot is made by SNAPDRAGON and i am making a complete custom userbot using it. I Credit to all the Respective Develelopers for creating the base modules. This userbot is currently in ALPHA stage and i don't mind creating a custom fork of my repository. I will takedown the repository if the credits of the developers are removed. use this userbot at your Own RISK

and don't blame me for spammers. the modules in this userbot are made for fun purposes and at the same time they are very Powerful. So, don't misuse.

Thank You

-RB INTERNATIONAL TEAM



# Complete Guide To Enable This BOT - 

DO NOT SKIP ANY STEPS

👉 Install this application Termux from Google Play



👉 Open Termux


```
termux-setup-storage
```

```
pkg install python git
```

```
 apt install git python -y && pip install telethon
```

```
 python -m venv venv && . ./venv/bin/activate
```

```
cd /sdcard/Telegram
```

```
git clone https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy
```

```
cd DeOXy
```

```
pip install telethon
```

```
python3 telesetup.py
```

```
Follow these OnScreen prompts-
```


Enter your phone number including your country code, Enter The OTP

Copy and keep the long text produced (eg, bybdiqebcuiqhdoj2k) at a secure place.





N.B.: Keep this string safe! Anyone with this string can use it to login into your account and do anything they want to to do.



👉 Open this link https://my.telegram.org/auth?to=apps



👉 Create an app with the necessary infos and copy the ID and HASH for the next step



Click On Deploy To Heroku Button-

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


[IF YOU DON'T HAVE Heroku ACCOUNT, JUST CREATE ONE PLOXX]



👉 Add The Following Mandatory Feilds

         App name - Any Of Your Choice

         APP_ID-  From https://my.telegram.org/auth?to=apps

        API_HASH- From https://my.telegram.org/auth?to=apps

        STRING_SESSION- The long code you generated in TERMUX

        TG_BOT_TOKEN_BF_HER- Create A Bot Using @BotFather On TELEGRAM And Generate A Token

        TG_BOT_USER_NAME_BF_HER- Username Of The Created Bot [Using @BotFather]

Rest of the fields can be left with the default values.



Now go to https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy

👉 Fork and star repository (if on android, enable desktop site to fork)

 

👉 Tap on Deploy app



👉 Wait for deploy to finish.



👉 After deploy press Manage App then go to Resources



👉 Enable the worker dyno, by toggling the slide-toggle.



👉 Done. Your UserBot is alive. Check with .help in any chat.

------------------------------------------------------------------------------------------------------------------------

# TO Enable AFK And PMPermit

Create A Group And Add Haruka Or Rose

* Go To the group and use the command 
```
.get_id
```

Copy the whole value

Enable Inlinie From BotFather

Go To dashboard.heroku.com

Go To your app

Tap on settings

Click on REVEAL CONFIG VARS

* Add two vars- 
```
PRIVATE_GROUP_ID 
```
```
PRIVATE_GROUP_BOT_API_ID
```

Add the value as the number you got from the group for both vars

DO NOT ADD ADMINS TO THE GROUP, IT WILL CHANGE THE ID



------------------------------------------------------------------------------------------------------------------------

How To SETUP Custom Alive Name

Go to heroku and add the following vars: 

Key: 
```
ALIVE_NAME
```
Value: The name you want to show

------------------------------------------------------------------------------------------------------------------------

How To Setup INBUILT Updater Module

⏩You need to set these two variables in heroku vars.. 


```
HEROKU_APP_NAME
```
It's the name of your app on heroku. 


```
HEROKU_API_KEY
```
You can get the value for this on https://dashboard.heroku.com/account look for api key there

After That Just .update now to update your DeOXY

In Case You Aren't Able To Update, PM @MrMobTech_Bot

------------------------------------------------------------------------------------------------------------------------



Send Your Feedback @MrMobTech_Bot

If You Like My Project, Contribute To The Development

https://www.paypal.me/RBINTERNATIONALNET



   𝔡𝓔𝐎𝕩𝕐 USERBOT TEAM





  〰️ @DeOXyOFFICIAL 〰️

----------------------------------------------------------------------------------------------------------------------------------------



### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Check [Line 111](https://github.com/Total-Noob-69/X-tra-Telegram/blob/master/userbot/uniborgConfig.py#L111) and start adding your vars there.
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
