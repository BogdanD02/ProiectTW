from django.shortcuts import render

from .testGeneration.generateTestCase import getTestCases
    
def demo(request, name, id):
    if request.method == 'GET':
        return render(request, 'demo.html', {'name': name, 'id' : id})
    
def run_evaluation(request, name, id):
    if request.method == 'GET':
        code = request.GET.get('code')
        data = getTestCases()
        print(data)
    
        return render(request, 'passed_failed_tests.html', {'data': data, 'id' : id, 'code': code})
    
def welcome(request, name):
    if request.method == 'GET':
        return render(request, 'welcome.html', {'name': name})