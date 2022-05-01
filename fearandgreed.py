from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date
import numpy as np

page = requests.get("https://alternative.me/crypto/fear-and-greed-index/")

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id = "main")

results_num = results.find_all("div", class_ = "fng-circle")
results_desc = results.find_all("div", class_ = "status")
results_when = results.find_all("div", class_ = "gray")

res_num_all = []
res_desc_all = []
res_when_all = []
for x in range(len(results_num)):
    res_num_all.append(results_num[x].get_text())
    res_desc_all.append(results_desc[x].get_text())
    res_when_all.append(results_when[x].get_text())

dict = {"when": res_when_all,
        "desc": res_desc_all,
        "num": res_num_all,
        "date_pulled": np.repeat(date.today(), len(res_num_all))}

fear_greed = pd.DataFrame(data = dict)
