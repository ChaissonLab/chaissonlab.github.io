---
permalink: /publications/
title: "Publications"
layout: single
author_profile: true

# This tells the page to gather all entries in the "publications" collection
toc: true
---

{% assign pubs = site.publications | sort: 'date' | reverse %}
{% for pub in pubs %}
- **{{ pub.title }}**, {{ pub.authors}}
   {{ pub.venue }} ({{ pub.date | date: "%Y" }})
  {% if pub.link %}<a href="{{ pub.link }}">link</a>{% endif %}
  {% if pub.doi %} • <a href="https://doi.org/{{ pub.doi }}">doi</a>{% endif %}
{% endfor %}

