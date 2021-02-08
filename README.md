# Nerd Deck
*I wanted to challenge myself to recreate Crunchyroll with tools and technology that wasnt taught in class*

## Technologies Used
- HTML
- CSS
- Python
- Django
- Amazon AWS
- Git / GitHub / GitBash
- Thoughts and Prayers

## Existing Features
- Creation of Users/Profiles
- Add/Remove Favorites to User Profile

- Creation of Anime
- Update Anime
- Upload Anime Photo
- Delete Anime
- Read Individual Anime

- Creation of Episodes
- Update Episode
- Upload Episode Photo
- Delete Episode
- Read Individual Episode

- Create Articles (Admin)
- Fueatured boolean for home page

## Planned Features
- Expand Anime Library
- Mobile Friendly
- Random Episode Generator
- User preference algorithm
- Non-admin Anime creation request form (submits to admin user)

## Code Snippets
``` Python
def search(request):
    query=None
    results = []
    results2 = []
    if request.method == 'GET':
        query = request.GET.get('search')
        results = Anime.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        results2 = Episode.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context = {
        'query': query,
        'results': results,
        'results2': results2
    }
    return render(request, 'search.html', context)
```

``` Python
def add_photo_anime(request, anime_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, anime_id=anime_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('anime_detail', anime_id=anime_id)
```