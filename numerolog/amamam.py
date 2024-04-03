def analyze_numbers(numbers):
    analysis_results = {
        1:"Number 1: Peen egoist",
        11:"Number 11: Nõrgalt väljendunud egoism",
        111:"Number 111: Kuulekas",
        1111:"Number 1111: Otsustav",
        11111:"Number 11111: Diktaator, isekas",
        111111:"Number 111111: Karm, julm",
        2:"Number 2: Tavaline",
        22:"Number 22: Piisavalt bioenergiat",
        222:"Number 222: Selgeltnägija märk",
        2222:"Number 2222: Saatana märk",
        3:"Number 3: Tahan teen, tahan ei",
        33:"Number 33: Analüütiline mõtteviis",
        333:"Number 333: Tugev kalduvus teadustele",
        3333:"Number 3333: Suured võimed, puudub soov areneda",
        4:"Number 4: Keskmiselt tervislik",
        44:"Number 44: Väga tugev inimene kõrge temperamendiga",
        444:"Number 444: Väga tugev tervis ja suured seksuaalsed võimed",
        5:"Number 5: Sidekanal on avatud",
        55:"Number 55: Väga arenenud intuitsioon",
        555:"Number 555: Peaaegu selgeltnägijad",
        5555:"Number 5555: Selgeltnägijad",
        6:"Number 6: Mingil määral maandatud",
        66:"Number 66: Väga maandatud",
        666:"Number 666: Kõrge temperamendiga",
        6666:"Number 6666: Kogunenud palju maandatust eelnevates kehastustes",
        7:"Number 7: Talent olemas",
        77:"Number 77: Tugev inglipärane märk",
        777:"Number 777: Tavaliselt maale tulnud lühikeseks ajaks",
        7777:"Number 7777: Surevad imikueas",
        8:"Number 8: Vastutustundlikud, ausad, täpsed tegudes",
        88:"Number 88: Väga arenenud kohusetunne",
        888:"Number 888: Teenimise märk rahvale",
        8888:"Number 8888: Sünnivad parapsühholoogiliste võimetega ja erakordse tundlikkusega täpsete teaduste suhtes",
        9:"Number 9: Peab kõvasti vaeva nägema",
        99:"Number 99: Sünnist alates intelligentne",
        999:"Number 999: Loodusest väga intelligentne, õpib nõrgalt, kuna kõik tuleb lihtsalt",
        9999:"Number 9999: Neile avaneb tõde"
    }
    results = []
    for number in numbers:
        if number in analysis_results:
            results.append(analysis_results[number])
        else:
            results.append(f"Number {number}: Value not found.")
    return " ".join(results)

