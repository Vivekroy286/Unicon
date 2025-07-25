from django.shortcuts import render

def index(request):
    featured = [
        {
            "title": "Echoes of Tomorrow",
            "artist": "Nova Keys",
            "img": "/static/images/artist1.jpg",
            "release_date": "2025-08-01",
        },
        {
            "title": "Neon Drift",
            "artist": "Synthwave Syndicate",
            "img": "/static/images/artist2.jpg",
            "release_date": "2025-08-10",
        },
        {
            "title": "Gravity Pulse",
            "artist": "DJ Orbit",
            "img": "/static/images/artist3.jpg",
            "release_date": "2025-08-15",
        },
    ]

    return render(request, "index.html", {"featured": featured})
