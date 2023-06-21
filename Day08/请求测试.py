import requests
import csv
import os

url = f"https://movie.douban.com/subject/1292052/comments?start=2200&limit=20&status=P&sort=new_score"
headers = {
    'user-agent':
        "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'"
    ,
    'cookie':
        'bid=IvtJHpetnDo; __yadk_uid=DFV1ZTyivH9ZbPq3MFJQUVWZcBNYM566; ll="108258"; __utmz=30149280.1686793317.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1686793321.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=5737f89bf3526cf1.1681452459.; _vwo_uuid_v2=D0141D5CCE68AEB41C766B408768FB3A4|3b438585d5e7d6f65d2af226ce626fe1; __gads=ID=9bdc14de8e1a2959-2240c51394de002a:T=1681452459:RT=1686793345:S=ALNI_MZD1_aD7LqfrUOMeMqYvydFFGhHJw; __gpi=UID=00000bf4641d88a5:T=1681452459:RT=1686793345:S=ALNI_MYKd2nmI437u9xtmQy4ACXQW7xktg; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1687173941%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.573424069.1681452459.1686798082.1687173942.6; __utmb=30149280.0.10.1687173942; __utmc=30149280; __utma=223695111.255182283.1681452459.1686798082.1687173942.5; __utmb=223695111.0.10.1687173942; __utmc=223695111; ap_v=0,6.0; ucf_uid=553f38e2-4761-4e22-ae3e-c9629f76ee0d; _pbjs_userid_consent_data=3524755945110770; cto_bundle=mu-kkF9UM2glMkZrbjhuN3JPamMlMkJOMDdsb0w0ckVCektyVGRwczUzeTJPVUN3QW5CbFdkVG5VY2NST255OUtFcmZqODNDTEVlWlhkUGxyd21ITTE1YkR6ZU5EQVdQWG9ZN05ZemlCbWU0dlNYZXhSSDZVU1FGeTg4UlJRZG9FZENTWnR4QXBnMmdrcG80WE94ZEluQkdMSTIwQXpBJTNEJTNE; cto_bidid=ryCfeV9Fc2U5b1gyVlFUSFB4ZkRZZTVoRTlaY3dNVUpQQ2k1aGZ4Q0xMUUlSZFZKejhEUUVCU1lXdWxoUzFZSEdoJTJCcG0xaWJQbWQ1cVlicG9QTWRURkVRUmlSM0glMkIlMkJyWmZBWUNKUCUyRmFWdHJDemlRJTNE'
}
response = requests.get(url, headers=headers)
print(response)
