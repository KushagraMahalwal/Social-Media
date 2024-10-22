from rest_framework.views import APIView
from smapi.models import createPost
from smapi.serializers import CreatePostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        all_post=createPost.objects.all()
        serializer=CreatePostSerializer(all_post, many=True)
        return Response(serializer.data)
    
    # Ensure only authenticated users can create posts
    def post(self, request, *args, **kwargs):    
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)  # Assign the current user to created_by
            return Response(serializer.data)
        return Response(serializer.errors)
        
class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        try:
            post=createPost.objects.get(pk=pk)
            serializer=CreatePostSerializer(post)
            return Response(serializer.data)

        except:
            return Response(serializer.errors)

    
    def post(self,request,pk):
        try:
            post=createPost.objects.get(pk=pk)
            serializer=CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(post=post, commented_by=request.user)
                return Response(serializer.data)
            
            else:
                return Response(serializer.errors)

        except:
            return Response({"data":"errors"})


    

