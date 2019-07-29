from django.shortcuts import render

from rest_framework import generics
from .serializers import Place_Serializers, LocationSerializers, Videos_Location_Serializers
from .models import Place, Location, Videos_Location

from django.db.models import Q

# Create your views here.
# Manage places (one city eg)
class Create_Place(generics.ListCreateAPIView):

    """This class defines the create behavior of our rest api."""
    queryset = Place.objects.all()
    serializer_class = Place_Serializers

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


# Manage locations from place
class Create_Location(generics.ListCreateAPIView):
	
    """This class defines the create behavior of our rest api."""
    # queryset = Location.objects.all()
    serializer_class = LocationSerializers

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

    # Filtering query set
    def get_queryset(self):

        # get location_id
        place_id = self.kwargs['place_id']

        # Filter by location id
        queryset = Location.objects.filter(place__id__exact = place_id).order_by("-id")        

        # Return queryset
        return queryset


# View for videos location
class Create_View_Videos_Location(generics.ListCreateAPIView):
	
    """This class defines the create behavior of our rest api."""
    # queryset = Videos_Location.objects.all()
    serializer_class = Videos_Location_Serializers

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

    # Filtering query set
    def get_queryset(self):

        # if self.request.method == 'GET':

        # print('Get method')

        # get location_id
        location_id = self.kwargs['location_id']

        # Filter by location id
        queryset = Videos_Location.objects.filter(Q(location__id__exact = location_id) and Q(activate__exact = True)).order_by("-votes")

        # Return queryset
        return queryset 

        # elif self.request.method == 'POST':

        #     print('POST method')

        #     # get location_id
        #     location_id = self.kwargs['location_id']

        #     # Filter by location id
        #     queryset = Videos_Location.objects.filter(location__id__exact = location_id).order_by("-votes")

        #     # Return queryset
        #     return queryset 

# View for videos location
# class Vote_for_video(generics.UpdateAPIView):
class Vote_for_video(generics.ListCreateAPIView):
    
    """This class defines the create behavior of our rest api."""
    # queryset = Videos_Location.objects.all()
    serializer_class = Videos_Location_Serializers

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

    # Filtering query set
    def get_queryset(self):

        # get location_id
        location_id = self.kwargs['video_id']

        print(self)

        try:

            # Filter by location id
            queryset = Videos_Location.objects.filter(id__exact = location_id)

        except:

            return 'error'

        # Get video
        video = queryset[0]

        # Edit votes
        video.votes = video.votes + 1

        # Update vote in DB
        video.save()

        # Return queryset
        return queryset

# # View for videos location
# class Create_New_Video_Location(generics.ListCreateAPIView):
    
#     """This class defines the create behavior of our rest api."""
#     # queryset = Videos_Location.objects.all()
#     serializer_class = Videos_Location_Serializers

#     def perform_create(self, serializer):
#         """Save the post data when creating a new bucketlist."""
#         serializer.save()
        
#     # Filtering query set
#     def get_queryset(self):

#         # if self.request.method == 'GET':

#         # print('Get method')

#         # get location_id
#         location_id = self.kwargs['location_id']


#         new_video = Videos_Location(location = location_id, link = 'ijao', skater= 'Leo bravo' )

#         # Filter by location id
#         queryset = Videos_Location.objects.filter(location__id__exact = location_id).order_by("-votes")

#         # Return queryset
#         return queryset 