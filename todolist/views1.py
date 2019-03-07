from django.shortcuts import render, redirect
# Create your views here.


lst = [
    {'待办事项': '遛狗', '已完成': False},
    {'待办事项': '打架', '已完成': True},
    {'待办事项': '买菜', '已完成': False},
    {'待办事项': '做饭', '已完成': False},
    {'待办事项': '遛狗1', '已完成': False},
    {'待办事项': '遛狗2', '已完成': False},
    {'待办事项': '遛狗3', '已完成': False},
    {'待办事项': '遛狗4', '已完成': False},
    {'待办事项': '遛狗5', '已完成': False},
]


def home(request):
    global lst
    if request.method == 'POST':
        # content = {'名字': str(request.POST), '是什么': str(type(request.POST))}
        if request.POST['待办事项'] == '':
            content = {'清单': lst, '警告': '请输入内容！'}
            return render(request, 'todolist/home.html', content)
        else:
            lst.append({'待办事项': request.POST['待办事项'], '已完成': False})
            content = {'清单': lst, '信息': '添加成功！'}
            return render(request, 'todolist/home.html', content)
    elif request.method == 'GET':
        content = {'清单': lst}
        return render(request, 'todolist/home.html', content)


def about(request):
    return render(request, 'todolist/about.html')


def edit(request, forloop_counter):
    global lst
    if request.method == "POST":
        if request.POST['已修改事项'] == '':
            return render(request, 'todolist/edit.html', {'警告': '请输入内容！'})
        else:
            lst[int(forloop_counter) - 1]['待办事项'] = request.POST['已修改事项']
            return redirect('todolist:待办清单')

    elif request.method == "GET":
        content = {'待修改事项': lst[int(forloop_counter) - 1]['待办事项']}
        return render(request, 'todolist/edit.html', content)


def delete(request, forloop_counter):
    global lst
    if request.method == "POST":
        lst.pop(int(forloop_counter) - 1)
        return redirect('todolist:待办清单')
    else:
        return redirect('todolist:待办清单')


def cross(request, forloop_counter):
    global lst
    if request.POST['完成状态'] == '已完成':
        lst[int(forloop_counter) - 1]['已完成'] = True
        return redirect('todolist:待办清单')
    else:
        lst[int(forloop_counter) - 1]['已完成'] = False
        return redirect('todolist:待办清单')
