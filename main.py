import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By

site_list = ['https://las.op.gg/champion/jax/statistics/top',
             'https://las.op.gg/champion/jayce/statistics/top',
             'https://las.op.gg/champion/jhin/statistics/bot', 
             'https://las.op.gg/champion/jinx/statistics/bot',
             'https://las.op.gg/champion/kaisa/statistics/bot', 
             'https://las.op.gg/champion/kalista/statistics/bot',
             'https://las.op.gg/champion/karma/statistics/support',
             'https://las.op.gg/champion/kassadin/statistics/mid', 
             'https://las.op.gg/champion/katarina/statistics/mid',
             'https://las.op.gg/champion/kayle/statistics/top', 
             'https://las.op.gg/champion/kennen/statistics/top',
             'https://las.op.gg/champion/kled/statistics/top', 
             'https://las.op.gg/champion/kogmaw/statistics/bot',
             'https://las.op.gg/champion/leblanc/statistics/mid', 
             'https://las.op.gg/champion/leona/statistics/support',
             'https://las.op.gg/champion/lissandra/statistics/mid', 
             'https://las.op.gg/champion/lucian/statistics/bot',
             'https://las.op.gg/champion/lulu/statistics/support', 
             'https://las.op.gg/champion/lux/statistics/support',
             'https://las.op.gg/champion/malphite/statistics/top', 
             'https://las.op.gg/champion/malzahar/statistics/mid',
             'https://las.op.gg/champion/maokai/statistics/top',
             'https://las.op.gg/champion/missfortune/statistics/bot',
             'https://las.op.gg/champion/mordekaiser/statistics/top',
             'https://las.op.gg/champion/morgana/statistics/support',
             'https://las.op.gg/champion/nami/statistics/support', 
             'https://las.op.gg/champion/nasus/statistics/top',
             'https://las.op.gg/champion/nautilus/statistics/support',
             'https://las.op.gg/champion/neeko/statistics/mid', 
             'https://las.op.gg/champion/nocturne/statistics/mid',
             'https://las.op.gg/champion/orianna/statistics/mid', 
             'https://las.op.gg/champion/ornn/statistics/top',
             'https://las.op.gg/champion/pantheon/statistics/mid', 
             'https://las.op.gg/champion/poppy/statistics/top',
             'https://las.op.gg/champion/pyke/statistics/support', 
             'https://las.op.gg/champion/qiyana/statistics/mid',
             'https://las.op.gg/champion/quinn/statistics/top',
             'https://las.op.gg/champion/rakan/statistics/support',
             'https://las.op.gg/champion/renekton/statistics/top',
             'https://las.op.gg/champion/rengar/statistics/top',
             'https://las.op.gg/champion/riven/statistics/top',
             'https://las.op.gg/champion/rumble/statistics/mid',
             'https://las.op.gg/champion/ryze/statistics/mid',
             'https://las.op.gg/champion/senna/statistics/support',
             'https://las.op.gg/champion/sett/statistics/top',
             'https://las.op.gg/champion/shen/statistics/top',
             'https://las.op.gg/champion/singed/statistics/top',
             'https://las.op.gg/champion/sion/statistics/top',
             'https://las.op.gg/champion/sivir/statistics/bot',
             'https://las.op.gg/champion/sona/statistics/top',
             'https://las.op.gg/champion/soraka/statistics/top',
             'https://las.op.gg/champion/swain/statistics/support',
             'https://las.op.gg/champion/sylas/statistics/mid',
             'https://las.op.gg/champion/syndra/statistics/mid',
             'https://las.op.gg/champion/tahmkench/statistics/support',
             'https://las.op.gg/champion/talon/statistics/mid',
             'https://las.op.gg/champion/taric/statistics/support',
             'https://las.op.gg/champion/teemo/statistics/top',
             'https://las.op.gg/champion/thresh/statistics/support',
             'https://las.op.gg/champion/tristana/statistics/bot',
             'https://las.op.gg/champion/tryndamere/statistics/top',
             'https://las.op.gg/champion/twistedfate/statistics/mid',
             'https://las.op.gg/champion/twitch/statistics/bot',
             'https://las.op.gg/champion/urgot/statistics/top',
             'https://las.op.gg/champion/varus/statistics/bot',
             'https://las.op.gg/champion/vayne/statistics/bot',
             'https://las.op.gg/champion/veigar/statistics/mid',
             'https://las.op.gg/champion/velkoz/statistics/support',
             'https://las.op.gg/champion/viktor/statistics/mid',
             'https://las.op.gg/champion/vladimir/statistics/top',
             'https://las.op.gg/champion/volibear/statistics/top',
             'https://las.op.gg/champion/xayah/statistics/bot',
             'https://las.op.gg/champion/xerath/statistics/support',
             'https://las.op.gg/champion/yasuo/statistics/mid',
             'https://las.op.gg/champion/yorick/statistics/top',
             'https://las.op.gg/champion/yuumi/statistics/support',
             'https://las.op.gg/champion/zed/statistics/mid',
             'https://las.op.gg/champion/zeri/statistics/bot',
             'https://las.op.gg/champion/ziggs/statistics/mid',
             'https://las.op.gg/champion/zilean/statistics/support',
             'https://las.op.gg/champion/zoe/statistics/mid',
             'https://las.op.gg/champion/zyra/statistics/support']


dict_matchups = {}
session = webdriver.Chrome()
try:
    for site in site_list:
        if "jungle" in site:
            continue
        champion = site.split("/")[4]
        dict_matchups[champion] = {}

        session.get(site + "/matchup")
        scroll_box = session.find_element(By.XPATH, '//div[@class="champion-matchup-champion-list"]')
        matchups = session.find_elements(By.XPATH, '//div[@class="champion-matchup-champion-list"]/div')

        for page in matchups:
            session.execute_script("arguments[0].scrollIntoView();", page)
            page.click()
            time.sleep(2)
            matchup = session.find_elements(By.XPATH, '//div[@class="champion-matchup-champion__name"]')
            element = session.find_elements(By.XPATH, '//table[@class="champion-matchup-table"]/tbody/tr/td')
            dict_matchups[champion][matchup[1].text] = float(element[0].text.strip('%'))

        print(dict_matchups)
except:
    traceback.print_exc()
finally:
    session.close()
    print(dict_matchups)
