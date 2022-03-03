# jupyhtml_ver.1.0.0

import os, sys, subprocess

try:
    # パス取得
    paths = sys.argv[1:]
    
    for path in paths:
        # ディレクトリの移動
        os.chdir(os.path.dirname(path))
        # html変換
        subprocess.run("jupyter nbconvert --to html --template full " + path, shell = True)
        # プレビュー
        subprocess.run("start " + os.path.splitext(os.path.basename(path))[0] + ".html", shell = True)
        
except:
    pass