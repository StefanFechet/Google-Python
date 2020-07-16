import sqlite3
import os

con = sqlite3.connect('db.sqlite3')


cursorObj = con.cursor()
cursorObj.execute('SELECT * FROM tasks_task ORDER BY created DESC')
rows = cursorObj.fetchall()

os.system('cp tasks/templates/tasks/table.html tasks/templates/tasks/final_table.html')
with open("tasks/templates/tasks/final_table.html", "a") as myfile:
    for row in rows:
        myfile.write('\n\t\t<tr>\n')
        for el in row:
            s = '\t\t\t<td>'+ str(el)+ '</td>\n'
            myfile.write(s)
        myfile.write('\t\t</tr>\n')
    myfile.write('\t</tbody>\n')
    myfile.write('</table>\n')