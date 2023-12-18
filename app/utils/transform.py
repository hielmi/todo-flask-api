def transformUsers(users):
    array = []
    for i in users:
        array.append({
            'id': i.id,
            'name': i.name,
            'email': i.email
        })
    return array

def singleTransformUser(user, withTodo=True):
    data = {
        'id': user.id,
        'name': user.name,
        'email': user.email
    }
    if withTodo:
        todos = []
        for i in user.todos:
            todos.append({
                'id': i.id,
                'todos': i.todos,
                'description': i.description,
            })
        data['todos'] = todos
        
    return data

def transformTodos(todos):
    array = []
    for i in todos:
        array.append(singleTransformTodo(i))
    return array

def singleTransformTodo(todo):
    return {
        'id': todo.id,
        'user_id': todo.user_id,
        'todos': todo.todos,
        'description': todo.description,
        'created_at': todo.created_at,
        'updated_at': todo.updated_at,
        'user': singleTransformUser(todo.users, withTodo=False)
    }