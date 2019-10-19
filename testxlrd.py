import xlrd
import whois

data = xlrd.open_workbook("website.xlsx")
sheet = data.sheet_by_index(0)
#row1 = sheet.row_values(i) 读取i行数据
# cell_A3 = sheet.cell(a,b).value 读取a行b列数据
weblist = []
def Getxldata():
    i = 0
    while(i<3):
        cell_A = sheet.cell(i, 0).value  # 读取某列数据
        i += 1
        weblist.append(cell_A)
    print(weblist)

def GetVendorFromWhoisInfo():
    i = 0
    while (i < 4):
        weblist[i]
        data = whois.whois(weblist[i])
        print("网站",i,"所在公司：", data.org)
        i += 1

if __name__ == '__main__':
    Getxldata()
    GetVendorFromWhoisInfo()
