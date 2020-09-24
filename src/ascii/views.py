from django.http import HttpResponse

def helloworld(request, param=None):
    if param:
        return HttpResponse(f'hello world {param}', status=403)
    html_string = '''
        <html>
             <form action="localhost:8000/helloworld" method="GET">
                 <input type="text" name="username" />
                 <input type="submit" value="GO" />
             </form>
             hello
        </html>
    '''
    param_string = request.GET['username']
    return HttpResponse(html_string + param_string)
