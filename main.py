from threading import Thread

import requests


def get_ss(i):
    link = f"https://www.kristheeyakeerthanangal.org/assets/songs/{i}.png"
    with open(f'songs_ss/{i}.png','wb') as fp:
        fp.write(requests.get(link).content)

threads = []
for i in range(1,428):
    thread = Thread(target=get_ss,args=[i])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
