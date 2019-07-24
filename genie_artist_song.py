from bs4 import BeautifulSoup
import requests


def genie_artist():
    result = []
    artist_input = input("Please Input Artist or song that you want")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    genie_site = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20190719&hh=21&rtm=Y&pg="
    f = open("genie_200.txt", 'w', -1, 'UTF-8')

    for i in range(1, 5):
        link = '{}{}'.format(genie_site, i)
        genie_site_extra = requests.get(link, headers=headers)
        html = genie_site_extra.text
        bsObj = BeautifulSoup(html, "html.parser")
        artist_list = bsObj.findAll("a", {"class": "artist ellipsis"})
        song_list = bsObj.findAll("a", {"class": "title ellipsis"})

        for j in range(len(song_list)):
            artist = artist_list[j + 5].text.strip()
            song = song_list[j].text.strip()

            if artist_input in artist or artist_input in song:
                result += ["{0:3d}위 {1} - {2}".format((i - 1) * 50 + j + 1, artist, song)]
                # data = "{0:3d}위 {1} - {2}".format(i + 1, artist, song)
            # f.write(data + "\n")

    if len(result) > 0:
        for file_result in result:
            print(file_result)
            f.write(file_result + "\n")
        print("파일이 정상적으로 완성되었습니다.")
        f.close()
    else:
        print("앗!" + artist_input + " 에 관한 데이터가 없어요.. 다시 한 번 더 찾아보시겠어요?")

    # for i in result:
        # f.write(i + "\n")
        # print("파일이 정상적으로 완성되었습니다.")
        f.close()
    # else:
    #     print("앗! " + artist_input+" 에 관한 데이터가 없어서 저장을 못해요ㅠㅠ 다시 한 번 더 찾아보시겠어요?")
    # else:
    #     print("앗! " + artist_input + " 에 대한 데이터가 없어서 못 만들었어요ㅠㅠ 다시 검색해주세요")


if __name__ == "__main__":
    genie_artist()
