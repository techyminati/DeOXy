# 𝔡𝓔𝐎𝕩𝕐 USERBOT
Join https://t.me/CyberJalagam for updates and tuts

Thanks To   [HardcoreUserbot](https://github.com/Hack12R/HardcoreUserbot) // [X-tra-Telegram](https://github.com/Dark-Princ3/X-tra-Telegram) \\\ [The-TG-Bot-2.0](https://github.com/PriyamKalra/The-TG-Bot-2.0) For helping me out with the codes. Thank You Buggies ;-)
### Click the button below to Deploy :P

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# Complete Guide To Enable This BOT - [HERE](https://telegra.ph/How-To-Enable-Your-%F0%9D%94%A1%F0%9D%93%94%F0%9D%90%8E%F0%9D%95%A9%F0%9D%95%90-USERBOT-06-03)


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
