from data import dict_matchups

folder = "champions/"

html_intro = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
    table, th, td {
        border: 1px solid black;
    }
    </style>
</head>
<body>
<table style="width:50%">
    <tr>
        <th>Champions</th>
    </tr>
"""

html_end = """</table>
</body>
</html>"""

file = open("index.html", "w+")
file.write(html_intro)

champions = list(dict_matchups.keys())
champions = sorted(champions)

for champion in champions:
        file.write("    <tr>\n")
        file.write("        <td><a href=" + folder + champion + ".html>" + str(champion.capitalize()) + "</a></td>\n")
        file.write("    </tr>\n")

file.write(html_end)
file.close()