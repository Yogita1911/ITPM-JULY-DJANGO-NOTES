'''from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def home(request):
    return Response({
        'status': 200,
        'message': 'Yes! DjangoRestFramework Working...'
    })

    
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(['GET', 'POST'])
def post_list(request):

    # GET request → fetch all posts
    if request.method == 'GET':
        posts = Post.objects.all()#to store object of post model
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # POST request → create new post
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Post Created Successfully',
                'data': serializer.data
            })
        return Response(serializer.errors)'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
def student_list(request):

    # GET → Show all students
    if request.method == 'GET':
        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data)

    # POST → Insert new student
    if request.method == 'POST': #if user send me post req.
        serializer = StudentSerializer(data=request.data)
     # add data and store this in serializer varible
        if serializer.is_valid(): #if data is valid
            serializer.save() # then save
            return Response({
                'status': 200,
                'message': 'Data added successfully!',
                'data': serializer.data
            })

        return Response({
            'status': 400,
            'errors': serializer.errors
        })


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    try:
        std = Student.objects.get(id=id) #id store
    except Student.DoesNotExist:
        return Response({'message': 'Student not found'}, status=404)

    # GET → Show one student
    if request.method == 'GET':
        serializer = StudentSerializer(std)
        return Response(serializer.data)

    # PUT → Update student
    if request.method == 'PUT':
        serializer = StudentSerializer(std, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Student updated successfully!',
                'data': serializer.data
            })
        return Response(serializer.errors, status=400)

    # DELETE → Delete student
    if request.method == 'DELETE':
        std.delete()
        return Response({
            'status': 200,
            'message': 'Student deleted successfully!'
        })
