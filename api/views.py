from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *

class PostView(APIView):
    """
    A view for handling CRUD operations on Post objects.

    Methods:
        - get: Retrieve all posts.
        - post: Create a new post.
        - put: Update an existing post.
        - delete: Delete a post.
    """

    def get(self, request):
        """
        Retrieve all posts.

        Parameters:
            request (HttpRequest): The HTTP request object.

        Returns:
            JsonResponse: A JSON response containing the serialized data of all posts.
        """
        try:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def post(self, request):
        """
        Create a new post.

        Parameters:
            request (HttpRequest): The HTTP request object.

        Returns:
            JsonResponse: A JSON response containing the serialized data of the created post.
                If the request data is invalid, returns a JSON response with the serializer errors and status 400.
        """
        try:
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def put(self, request, pk):
        """
        Update an existing post.

        Parameters:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the post to be updated.

        Returns:
            JsonResponse: A JSON response containing the serialized data of the updated post.
                If the request data is invalid, returns a JSON response with the serializer errors and status 400.
        """
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def delete(self, request, pk):
        """
        Delete a post.

        Parameters:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the post to be deleted.

        Returns:
            JsonResponse: A JSON response with status 204 indicating successful deletion.
        """
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return JsonResponse(status=204)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
