#!/usr/bin/env python
# encoding: utf-8
# by netcan @ https://github.com/netcan/Leetcode-Rust
import requests, os
import requests_cache
import re, threading
import subprocess
from requests.utils import requote_uri
from collections import Counter
from datetime import datetime
import time

CODE_TEMPLATE = \
"""// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
{code}
"""

REPO_README_TEMPLATE = """
## Leetcode-Python
本项目记录我的Python刷题经验，也是学习Python的过程。
本项目由`crawler.py`生成，代码由@Netcan提供。代码自动爬取Leetcode-cn.com网站获取个人提交记录。使用方法：登陆Leetcode后记录cookie，设置环境变量`LEETCODE_COOKIE`，然后执行本脚本就能抓取指定语言的个人提交记录。
目前已解决的题目（{solv_question_num} 个，其中简单{easy_num} 个，中等{medium_num} 个， 困难{hard_num} 个）：
{solv_question_list}
"""

QUESTION_TEMPLATE = """
### {question_name} {question_level}
- 题目地址/Problem Url: [{question_url}]({question_url})
- 执行时间/Runtime: {runtime} 
- 内存消耗/Mem Usage: {mem_usage}
- 通过日期/Accept Datetime: {time}
```{lang}
{code}
```
"""

class Leetcode:
    LEETCODE_URL = 'https://leetcode-cn.com'
    LEETCODE_LIST_URL = 'https://leetcode-cn.com/api/problems/all/'
    LEETCODE_GRAPHQL = 'https://leetcode-cn.com/graphql'
    REPO_URL = 'https://github.com/CLAY2333/CLAYleetcode'
    def __init__(self):
        Cookies='_uab_collina=153684999015102730549724; gr_user_id=392568e9-6088-41e9-a66d-461a34b80de2; grwng_uid=d006cd8b-ecd0-4e50-923f-48447532bb95; _ga=GA1.2.1958217467.1552566111; a2873925c34ecbd2_gr_last_sent_cs1=clay-13; __auc=1d5d95361698f93331e02b92d2f; __atuvc=8%7C12%2C3%7C13%2C6%7C14; O5LM_2132_nofavfid=1; O5LM_2132_ulastactivity=07abbg4SbKzWsB0TcCnALoS%2F1rKJbm3elO8yjTYtaF6iaZJff%2BaC; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1561450270; _gid=GA1.2.1668930569.1561450270; a2873925c34ecbd2_gr_session_id=cdd43a76-158c-4163-abf2-9d70efe0c8da; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=cdd43a76-158c-4163-abf2-9d70efe0c8da; a2873925c34ecbd2_gr_session_id_cdd43a76-158c-4163-abf2-9d70efe0c8da=true; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1561450556; a2873925c34ecbd2_gr_cs1=clay-13; csrftoken=TObxXeXdqo5lYsT6tYX5BJszr4PP5Mw8OaEWgZEbyDOMvi55hMG1LwUd5WJ5vH9g; messages="ec159d0b606534fa75ac89c6d91839f9d5e946c3$[[\"__json_message\"\0540\05425\054\"\\u6210\\u529f\\u901a\\u8fc7 NendoC \\u767b\\u5f55\"]]"; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNDMxMjMyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzUyMWI5YjRmY2U4YzZkMDc0NDczNGIwNTlmOTg5NzUzNGIwNzA4MyIsImlkIjo0MzEyMzIsImVtYWlsIjoiIiwidXNlcm5hbWUiOiJjbGF5LTEzIiwidXNlcl9zbHVnIjoiY2xheS0xMyIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLWNuLmNvbS9hbGl5dW4tbGMtdXBsb2FkL3VzZXJzL2NsYXktMTMvYXZhdGFyXzE1NTI1NjcwNjUucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsInRpbWVzdGFtcCI6IjIwMTktMDYtMjUgMDg6MTY6NTUuMDQ3MTk1KzAwOjAwIiwiUkVNT1RFX0FERFIiOiIxNzIuMjEuMi4xOTEiLCJJREVOVElUWSI6IjM2YjlhOTM3YzE3YzNjMjExNTFhMWRiYzFkZGU4MTA4IiwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.mS0a-Zzsv4AJWqozxBtySsZ6VVMAatbiko8-z51v_cg'
        self.cookies = Cookies
        self.headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,la;q=0.8,de;q=0.7,en;q=0.6,zh-TW;q=0.5",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "cookie": self.cookies,
            "dnt": "1",
            "pragma": "no-cache",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            }

    def get_solved_list(self):
        with requests_cache.disabled():
            # print("solved_list: ", requests.get(Leetcode.LEETCODE_LIST_URL, headers=self.headers).json())
            return [{
                "question_slug": v['stat']['question__title_slug'],
                "question_id": v['stat']['question_id'],
                "question_title": v['stat']['question__title'],
                "question_difficulty": v['difficulty']['level']
                } for v in
                    requests.get(Leetcode.LEETCODE_LIST_URL, headers=self.headers).json()['stat_status_pairs']
                if v['status'] == 'ac'
            ]

    def get_submit_list(self, question_slug):
        data = '{"operationName":"Submissions","variables":{"offset":0,"limit":0,"lastKey":null,"questionSlug":"%s"},"query":"query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {\\n  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {\\n    lastKey\\n    hasNext\\n    submissions {\\n      id\\n      statusDisplay\\n      lang\\n      runtime\\n      timestamp\\n      url\\n      isPending\\n      memory\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}' % question_slug
        return [item for item in
            requests.post(Leetcode.LEETCODE_GRAPHQL, headers=self.headers, data=data).json()['data']['submissionList']['submissions']
            if item['statusDisplay'].lower() == 'accepted']

    def get_source(self, url): # /submissions/detail/14313499/
        req_url = self.LEETCODE_URL + url
        try:
            src = re.search('submissionCode: \'(.*)\',', requests.get(req_url, headers=self.headers).text).group(1)
            return src.encode('cp1252', 'backslashreplace').decode('unicode-escape')
        except AttributeError:
            pass

    def output_source(self, lang='python', lang_suffix='py', max_threads=8):
        solved_list = self.get_solved_list()
        threads = []
        question_list = []
        for idx, question in enumerate(solved_list):
            print("processing: {}. {} ({}/{})".format(question["question_id"],
                                                      question["question_title"],
                                                      idx + 1, len(solved_list)))
            def process_submit_list(question_):
                submit_list = self.get_submit_list(question_["question_slug"])
                for submit in submit_list:
                    if submit["lang"] == lang or submit["lang"]=='python3':
                        src = self.get_source(submit['url'])
                        if not src: continue

                        src = CODE_TEMPLATE.format(code=src)
                        dir_name = "n{:04d}. {}".format(question_["question_id"], question_["question_title"])
                        if not os.path.exists(dir_name):
                            os.mkdir(dir_name)
                        with open(os.path.join(dir_name, "main.{}".format(lang_suffix)), "w") as f:
                            f.write(src)

                        with open(os.path.join(dir_name, "README.md"), "w") as f:
                            f.write(QUESTION_TEMPLATE.format(question_name = question_["question_title"],
                                                             question_level = ":star:" * question_["question_difficulty"],
                                                             question_url = self.LEETCODE_URL + "/problems/{}".format(question_["question_slug"]),
                                                             runtime = submit["runtime"],
                                                             mem_usage = submit["memory"],
                                                             time = datetime.fromtimestamp(int(submit["timestamp"])).strftime("%Y-%m-%d %H:%M"),
                                                             lang = lang,
                                                             code = src))
                        question_list.append("n{:04d}. {} {}".format(question_["question_id"],
                                                                     question_["question_title"],
                                                                     ":star:" * question_["question_difficulty"]))
                        break

            while len(threads) >= max_threads:
                for thread in threads:
                    if not thread.is_alive():
                        threads.remove(thread)
            thread = threading.Thread(target=process_submit_list, args=(question,), daemon=True)
            thread.start()
            threads.append(thread)
        time.sleep(4)
        self.__generate_readme(question_list)



    def __generate_readme(self, question_list):
        question_num = len(question_list)
        print(question_num)
        question_level = Counter(q.count(':star:') for q in question_list)
        question_list.sort(key=lambda q: int(re.search(r"(\d+)\..*", q).group(1)))
        question_list = '\n'.join(
            map(lambda u: "- [{}]({})".format(
                u.lstrip('n0'), requote_uri(
                    (Leetcode.REPO_URL + '/tree/master/{}'.format(u.replace(':star:', ''))).strip()
                )
            ) , question_list)
        )

        with open("README.md", "w") as f:
            f.write(REPO_README_TEMPLATE.format(solv_question_num=question_num,
                                                easy_num=question_level[1],
                                                medium_num=question_level[2],
                                                hard_num=question_level[3],
                                                solv_question_list=question_list))


if __name__ == '__main__':
    requests_cache.install_cache('leetcode')
    lc = Leetcode()

    lc.output_source()

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "commit by crawler.py @CLAY at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M"))])
    subprocess.run( ["git", "push", "--force", "origin", "master"])