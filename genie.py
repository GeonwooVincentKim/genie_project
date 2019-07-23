from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def genie_list():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    get_element = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20190719&hh=21&rtm=Y&pg="
    file = open("GenieTop200.txt", 'w', -1, 'UTF-8')

    for i in range(1, 5):
        link = '{}{}'.format(get_element, i)

        get_element_2 = requests.get(link, headers=header)
        html = get_element_2.text
        bsObj = BeautifulSoup(html, "html.parser")
        artist_list = bsObj.findAll("a", {"class": "artist ellipsis"})
        rank_list = bsObj.findAll("a", {"class": "title ellipsis"})

        for j in range(len(rank_list)):
            artist_chart = artist_list[j+5].text.strip()
            rank_chart = rank_list[j].text.strip()
            # print("{0:3d}위 {1} - {2}".format((i-1) * 50 + j+1, artist_chart, rank_chart))
            # 첫 번째 Page 에서는 (i-1) * 50 = 1 ~ 50
            # 두 번째 Page 에서는 (i-1) * 50 = 51 ~ 100
            # 세 번째 Page 에서는 (i-1) * 50 = 101 ~ 150
            # 네 번째 Page 에서는 (i-1) * 50 = 151 ~ 200

            print("{0:3d}위 {1} - {2}".format((i-1) * 50 + j+1, artist_chart, rank_chart))
            data = "{0:3d}위 {1} - {2}".format((i-1) * 50 + j+1, artist_chart, rank_chart)
            file.write(data + "\n")
    print("파일 쓰기 완료")
    file.close()


if __name__ == "__main__":
    genie_list()
