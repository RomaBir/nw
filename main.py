# import requests
# import flask
#
# # URL = "https://api.telegram.org/bot%s/" % BOT_TOKEN
# # MyURL = "https://example.com/hook"
# #
#
#
# import os
# token = "5934007503:AAHIlCler9UKE9LCEqPivN8-szxl2uZaOUo"
#
# a = """curl --location --request GET 'https://api.ngrok.com/tunnels' --header 'Authorization: Bearer {2M5zJYFsCF9yuFaBiKUr2SCScL4_86ZvZNea8NBiFRoXecPHi}' --header 'Ngrok-Version: 2'"""
#
# b = f"""curl --location --request POST "https://api.telegram.org/bot{token}/setwebhook" --header "Content-Type: application/json" --data-raw "url": {"https://09a1-77-43-209-121.eu.ngrok.io"} --ssl-no-revoke"""
#
# c = """POST https://api.telegram.org/bot5934007503:AAHIlCler9UKE9LCEqPivN8-szxl2uZaOUo/sendMessage"""
#
# os.system(b)
import asyncio
import time


async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    await fun1(4)
    await fun2(4)


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))

main()
