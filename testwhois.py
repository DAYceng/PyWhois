import whois

weblist = ['www.hao123.com', ' www.ali213.net', 'www.bilibili.com', 'github.com', 'www.people.com.cn']


def GetVendorFromWhoisInfo():
    i = 0
    while (i < 4):
        weblist[i]
        data = whois.whois(weblist[i])
        print("网站查询结果：", data)
        print("网站所在国家：", data.org)
        i += 1


if __name__ == '__main__':
    GetVendorFromWhoisInfo()