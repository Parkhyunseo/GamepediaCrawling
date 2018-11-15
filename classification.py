import os

DIRECTORY_NAME = "resource"
CURRENT_DIR = os.getcwd()
cluster = dict()

def search(dirname):
    filenmaes = os.listdir(dirname)
    return filenmaes

files = search(DIRECTORY_NAME)

for f in files:
    index = f.rfind('_')
    name = f[:index]

    if name not in cluster:
        cluster[name] = []
        cluster[name].append(f)
    else:
        cluster[name].append(f)

for key, items in cluster.items():
        os.mkdir(os.path.join(CURRENT_DIR, DIRECTORY_NAME, key))
        for item in items:
                os.rename(os.path.join(CURRENT_DIR, DIRECTORY_NAME, item), os.path.join(CURRENT_DIR, DIRECTORY_NAME, key, item))

