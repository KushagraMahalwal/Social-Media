from rest_framework import status
from rest_framework.views import APIView
from smapi.models import createPost,comment
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from smapi.serializers import CreatePostSerializer, CommentSerializer

# create/view all post
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

class CommentViewDetails(APIView):
    # updating the comment
    def put(self,request,post_pk, comment_pk):
        try:
            post=createPost.objects.get(pk=post_pk)
            comment_instance=comment.objects.get(pk=comment_pk, post=post)
            serializer=CommentSerializer(comment_instance,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({'Data':'Not Found'})
        
     # deleting the comment     
    def delete(self,request,post_pk, comment_pk):
        try:
            # get the post by pk
            post=createPost.objects.get(pk=post_pk)
            # get the comment that belong to specified post
            comment_instance=comment.objects.get(pk=comment_pk, post=post)
            comment_instance.delete()
            return Response({'Data':'Post Deleted Successfully'})
        except createPost.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        except comment.DoesNotExist:
            return Response({"error": "Comment not found for this post"}, status=status.HTTP_404_NOT_FOUND)

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

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, post_id):
        try:
            # post = get_object_or_404(createPost,id=post_id)
            post=createPost.objects.get(id=post_id)
            user = request.user

            # Toggle like/unlike based on whether the user already liked the post
            if post.liked_by.filter(id=user.id).exists():
                post.liked_by.remove(user)
                message = "You have unliked the post."
            else:
                post.liked_by.add(user)
                message = "You have liked the post."

            # Fetch all names of users who liked the post
            liked_by_names = post.liked_by.values_list('name', flat=True)
            return Response({
                'message': message,
                'likes_count': post.liked_by.count(),
                'liked_by': list(liked_by_names)  # List of usernames who liked the post
            }, status=status.HTTP_200_OK)
        
        except:
            return Response({'Data':'No post found'})