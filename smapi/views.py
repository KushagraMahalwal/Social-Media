from smapi.models import createPost
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from smapi.serializers import CreatePostSerializer, CommentSerializer

# create/view all posts
class CreatePostView(APIView):
    # Ensure only authenticated users can create posts
    permission_classes = [IsAuthenticated]
    def get(self,request):
        all_post=createPost.objects.all()
        serializer=CreatePostSerializer(all_post, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):    
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)  # Assign the current user to created_by
            return Response(serializer.data)
        return Response(serializer.errors)

# fetching post, deleting and updating using id
class CreatePostDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        try:
            post=createPost.objects.get(pk=pk)
            serializer=CreatePostSerializer(post)
            return Response(serializer.data)

        except:
            return Response({"Data":"Not Found"})

    def put(self,request,pk):
        user=request.user
        post=createPost.objects.get(pk=pk)
        if post:
            if user==post.created_by:
                serializer=CreatePostSerializer(post,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)
            else:
                return Response({"Data":"Not Current logged in user"})
        else:
            return Response({"Data":"Post Not Found"})


    def delete(self,request,pk):
        try:
            user=request.user
            post=createPost.objects.get(pk=pk)
            if user==post.created_by and post:
                post.delete()
                return Response({"Data":"Post Deleted Successfully"})
            else:
                return Response({"not logged in user"})
        except:
            return Response({"Data":"Post Not Found"})
    

#Comment to a particular post/ retrieving the post 
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

#View Profile of authenticated users 
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user=request.user
        data={
            "username":user.name,
            "email":user.email
        }
        return Response(data)
    
class currentUserPost(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user=request.user
        post=createPost.objects.filter(created_by=user)
        serializer=CreatePostSerializer(post, many=True)
        return Response(serializer.data)
    

