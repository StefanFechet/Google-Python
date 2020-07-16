from django.shortcuts import render, redirect
from .forms import *
import sqlite3
import os

def index(request):
	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	context = {'tasks': Task.objects.all(), 'form': form}
	return render(request, 'tasks/list.html', context)

def table(request):
	con = sqlite3.connect('db.sqlite3')
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM tasks_task ORDER BY created DESC')
	rows = cursorObj.fetchall()

	os.system('cp tasks/templates/tasks/table.html tasks/templates/tasks/final_table.html')
	with open("tasks/templates/tasks/final_table.html", "a") as myfile:
		for row in rows:
			myfile.write('\n\t\t<tr>\n')
			for el in row:
				if el == row[2]:
					el = row[2][:-7]
				s = '\t\t\t<td>' + str(el) + '</td>\n'
				myfile.write(s)
			myfile.write('\t\t</tr>\n')
		myfile.write('\t</tbody>\n')
		myfile.write('</table>\n')

	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=Task.objects.get())
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form': form}
	return render(request, 'tasks/final_table.html', context)

def up(request):
	con = sqlite3.connect('db.sqlite3')
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM tasks_task ORDER BY created ASC')
	rows = cursorObj.fetchall()

	os.system('cp tasks/templates/tasks/table.html tasks/templates/tasks/final_table.html')
	with open("tasks/templates/tasks/final_table.html", "a") as myfile:
		for row in rows:
			myfile.write('\n\t\t<tr>\n')
			for el in row:
				s = '\t\t\t<td>' + str(el) + '</td>\n'
				myfile.write(s)
			myfile.write('\t\t</tr>\n')
		myfile.write('\t</tbody>\n')
		myfile.write('</table>\n')

	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=Task.objects.get())
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form': form}
	return render(request, 'tasks/final_table.html', context)

def down(request):
	con = sqlite3.connect('db.sqlite3')
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM tasks_task ORDER BY created DESC')
	rows = cursorObj.fetchall()

	os.system('cp tasks/templates/tasks/table.html tasks/templates/tasks/final_table.html')
	with open("tasks/templates/tasks/final_table.html", "a") as myfile:
		for row in rows:
			myfile.write('\n\t\t<tr>\n')
			for el in row:
				s = '\t\t\t<td>' + str(el) + '</td>\n'
				myfile.write(s)
			myfile.write('\t\t</tr>\n')
		myfile.write('\t</tbody>\n')
		myfile.write('</table>\n')

	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=Task.objects.get())
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form': form}
	return render(request, 'tasks/final_table.html', context)

def updateTask(request, pk):
	form = TaskForm(instance=Task.objects.get(id=pk))
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=Task.objects.get(id=pk))
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form': form}
	return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
	Task.objects.get(id=pk).delete()
	return redirect('/')
