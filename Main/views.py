from django.shortcuts import render

from .testGeneration.generateTestCase import getTestCases
    
def demo(request, name, id):
    if request.method == 'GET':
        return render(request, 'demo.html', {'name': name, 'id' : id})
    
def run_evaluation(request, name, id):
    if request.method == 'GET':
        code = request.GET.get('code')
        data = getTestCases()
    
        return render(request, 'passed_failed_tests.html', {'data': data, 'id' : id, 'code': code})
    
def welcome(request, name):
    if request.method == 'GET':
        if name == "David":
            return render(request, 'welcome-prof.html', {'name': name})
        return render(request, 'welcome.html', {'name': name})

def show_courses(request, name):
    return render(request, 'view_courses.html')

def add_course(request, name):
    return render(request, 'adauga_curs.html')

def show_tests(request, name):
    pass

def add_test(request, name):
    return render(request, 'add_test.html')

def browse_courses(request, name):
    pass