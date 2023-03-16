def handle_uploaded_file(f):  
    with open('classroom/media/others/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  