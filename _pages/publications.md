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
  {% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}"> **{{pub.title}}** </a> {% else %} {{ **pub.title** }} {% endif %}
{{ pub.authors}}, 
   _{{ pub.venue }}_ ({{ pub.date | date: "%Y" }})
  {% if pub.pmid %} PMID: {{ pub.pmid }} {% endif %}
{% endfor %}

#  {% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">doi</a>{% endif %}
