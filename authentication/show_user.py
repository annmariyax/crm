# context processor

# here context processor is used to implement how username displays

def show_user_name(request):

    username = request.user.username

    name = username.split('@')[0]

    print (name)
    
    return {'name_of_user':name}