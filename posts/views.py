from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse

# Create your views here.





posts = [
    {
        "id" : 1,
        'title' : 'Let\'s Learn Django',
        'content' : 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.',
    }
    ,
    {
        "id" : 2,
        'title' : 'Let\'s Learn Javascript',
        'content' : 'Javascript is a programming language that conforms to the ECMAScript specification. Javascript is high-level, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.',
    }
    ,
    {
        "id" : 3,
        'title' : 'Django is the best framework',
        'content' : 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.',
    }

]


def home(request):
    #print(reverse('home'))
    html = ""
    for post in posts:
        html+= f'''
        <div>
        <a href="/post/{post['id']}"> 
        <h1>{post['id']} - {post['title']}</h1>
        </a> 
        <p>{post['content']}</p>
        </div>
'''
    return render(request,'posts/index.html',{'posts': posts,})
    # return HttpResponse(html)



def post(request,id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break

    if not valid_id:
        return HttpResponseNotFound(f'<h1>Post with id {id} not found</h1>')
        # raise Http404(f'Post with id {id} not found')
    else:
        html = f'''
            <h1>{post_dict['id']} - {post_dict['title']}</h1>
            <p>{post_dict['content']}</p>
    '''
    print(type(id))
    return render(request,'posts/post.html',{'post': post_dict})



def google(request,id):

       url = reverse('post',args=[id]) # reverse function will take the name of the url and return the url path with the given arguments it will see the urls.py file and find the url with the name 'post' and return the url path with the given arguments
       
       return HttpResponseRedirect(url)
   
   
   
# def globals(request):
#     return render(request,'global.html')