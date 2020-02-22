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
<a href="../"><button type="button">Home</button></a>
<table style="width:50%">
    <tr>
        <th>Opponent</th>
        <th>Lane Kill Rate</th>
    </tr>
"""

html_end = """</table>
</body>
</html>"""

for champion in dict_matchups:
    opponent_list = []
    for opponent in dict_matchups[champion]:
        opponent_list.append((dict_matchups[champion][opponent], opponent))
    opponent_list = sorted(opponent_list, key=lambda tup: tup[0])
    file = open(folder + champion + ".html", "w+")
    file.write(html_intro)
    for opponent in opponent_list:
        file.write("    <tr>\n")
        file.write("        <td>" + str(opponent[1]) + "</td>\n")
        file.write("        <td>" + str(opponent[0]) + "</td>\n")
        file.write("    </tr>\n")
    file.write(html_end)
    file.close()
