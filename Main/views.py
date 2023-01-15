from django.shortcuts import render, redirect
from datetime import datetime
from .models import Test, Input
import json
import importlib.util
from .testGeneration.base import Literal
from django.http import JsonResponse
    
def demo(request, name, id):
    if request.method == 'GET':
        test = Test.objects.get(id = id)

        title = test.title
        descr = test.description

        return render(request, 'adauga_cod.html', {'name': title, 'descr': descr, 'data': id})

def get_output(request, id):
    test = Test.objects.get(id = id)
    inputs = Input.objects.filter(test_id = id)
    jsonData = {
        'testCases': []
    }
    spec = importlib.util.spec_from_file_location(test.output_generator, 'sources/' + test.title + '.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for i in range(test.no_test_cases):
        inputData = {}
        for item in inputs:
            generator = Literal(item.name, item.data_type, item.values)
            inputData[item.name] = generator.getValue()
        jsonData['testCases'].append(
            {
                'input': inputData,
                'output': module.solve(inputData)
            }
        )
    
    return JsonResponse(jsonData)

def welcome(request, name):
    if request.method == 'GET':
        if name == "David":
            return render(request, 'welcome-prof.html', {'name': name})

        tests = Test.objects.filter(homework=0, exercise=0)
        return render(request, 'welcome.html', {'name': name, 'tests': [i+1 for i in range(len(tests))]})

def show_courses(request, name):
    return render(request, 'view_courses.html')

def add_course(request, name):
    if name != "David":
        return render(request, 'error.html', {'err': 401}, content_type="text/html", status=401)
    return render(request, 'adauga_curs.html')

def show_tests(request, name):
    if name != "David":
        return render(request, 'error.html', {'err': 401}, content_type="text/html", status=401)

def add_test(request, name):
    if request.method == 'GET':
        if name != "David":
            return render(request, 'error.html', {'err': 401}, content_type="text/html", status=401)
        return render(request, 'add_test.html')
    
    try:
        Test.objects.get(title=request.POST['title'])
    except Test.DoesNotExist:
        start_str = request.POST['startDate'] + " " + request.POST['startHr']
        stop_str = request.POST['stopDate'] + " " + request.POST['stopHr']

        test = Test(
            title = request.POST['title'],
            description = request.POST['Description'],
            output_generator = request.POST['OutputScript'],
            no_test_cases = 6,
            save_sources = 0,
            homework = 0,
            start_date = datetime.strptime(start_str, '%Y-%m-%d %H:%M'),
            due_date = datetime.strptime(stop_str, '%Y-%m-%d %H:%M'),
        )

        with open("sources/" + test.title + ".py", "x") as f:
            f.write(test.output_generator)

        test.save()

        for item in request.POST['InputData'].split('\n'):
            arr = item.split(' ')
            val = ""

            for i in range(2, len(arr)):
                if arr[i][-1] == '\n' or arr[i][-1] == '\r':
                    arr[i] = arr[i][:-1]
                val += arr[i]

            inputD = Input(
                data_type = arr[0],
                name = arr[1],
                test = test,
                values = val
            )

            inputD.save()
    return redirect("/main/" + name)

def browse_courses(request, name):
    pass