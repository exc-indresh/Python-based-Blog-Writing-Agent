def generate_seo_metadata(title, keywords):
    return {
        "title": title,
        "description": f"A blog about {title} and related topics in tech.",
        "keywords": keywords,
        "slug": title.lower().replace(" ", "-"),
        "reading_time": "6 min"
    }
