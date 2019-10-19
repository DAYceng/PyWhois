import whois


if __name__ == '__main__':
    data = whois.whois("channel.status.request.url")
    print(data)