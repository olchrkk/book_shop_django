from .models import Genre


def get_genres(request, params):
    try:
        genres = Genre.objects.all()
        params['genres'] = genres
    except:
        pass
    finally:
        return params
