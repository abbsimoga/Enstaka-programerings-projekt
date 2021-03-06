import datetime as dt
from matplotlib import style
import pandas_datareader.data as web
style.use("ggplot")

fond=""

while fond != "esc":
    fond = str(input("Jag vill se information på: "))
    if fond == "esc":
        break

    tidstart = str(input("Från: "))
    tidslut = str(input("Till: "))

    start = list(map(int, tidstart.split()))
    end = list(map(int, tidslut.split()))

    df = web.DataReader(fond, "yahoo", dt.datetime(start[0],start[1],start[2]), dt.datetime(end[0],end[1],end[2]))

    print(df)

    valspara = ""
    while valspara != "ja" or valspara != "nej":
        valspara = str(input("Jag vill spara informationen "))
        if valspara == "ja":
            df.to_csv(fond+".csv")
            break
        elif valspara == "nej":
            break
        else:
            print(valspara, "är inte ett alternativ")