from threading import Thread

import requests


def threadify(func):
    def wrapper(i):
        thread = Thread(target=func,args=[i])
        thread.start()
        return thread
    return wrapper

@threadify
def get_ss(i):
    link = f"https://www.kristheeyakeerthanangal.org/assets/songs/{i}.png"
    with open(f'songs_ss/{i}.png','wb') as fp:
        fp.write(requests.get(link).content)

threads = []
for i in range(1,428):
    threads.append(get_ss(i))

for thread in threads:
    thread.join()
