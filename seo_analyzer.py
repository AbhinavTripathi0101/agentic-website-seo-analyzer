def seo_analyzer(keywords, content):
    issues = []

    if len(content.split()) < 300:
        issues.append("Content is too short for SEO")

    if not keywords:
        issues.append("No strong keywords detected")

    return issues
