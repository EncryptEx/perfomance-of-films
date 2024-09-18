from utils import cnct


def do(screen):
    conn, cur = cnct()
    if screen: 
        print(
            """Finally, it calculates the country film average and it displays it.
        Also it saves on a file called: results.txt"""
        )
    cur.execute("""SELECT * FROM movies""")
    movies = list()
    for row in cur:
        if float(row[2]) == 0.0:
            continue
        movies.append((str(row[1]), str(row[2])))
    average = dict()
    timescountry = dict()
    final = dict()
    for country, rating in movies:
        average[country] = average.get(country, float(rating)) + float(rating)
        timescountry[country] = timescountry.get(country, 1) + 1
    for country, rating in movies:
        final[country] = float(average[country]) / float(timescountry[country])
    
    if screen: 
        print("__________________")
    f = open("results.txt", "a")
    f.write("\n__________________\n")
    
    final = {k: v for k, v in sorted(final.items(), key=lambda item: item[1])}

    for country, rating in final.items():
        # if country in ["/", "", "\\N",]:
        #    continue
        av = final[country]
        el = timescountry[country]
        rsum = average[country]
        toprint = (
            "Country:",
            country,
            "Average:",
            av,
            "Elements:",
            el,
            "Ratings sum:",
            rsum,
        )
        if screen:
            print(toprint)
        f.write(str(toprint) + "\n")

    if screen:
        print("__________________")
    f.write("\n__________________\n")
    f.close()
