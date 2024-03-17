# Guidelines

## Icon 
`<link rel="icon" type="image/x-icon" href="/static/images/favicon.ico">`
in the header

## Media uploads
Upload in relevant folders according to the media type
- /static/images
- /static/videos
- /static/audio

## Meta tags
Use meta tags in the header

## Stylization
Use snake case (snake_case) except for CSS custom variables, use kebab case (kebab-case)


## Sections
Sections should use the `<section>` tag.

Should look like:
```
{% extends "layout.html" %}
{% block content %}
<section id="descriptive_id">
    <!-- HTML goes here -->
</section>
{% endblock %}
```
