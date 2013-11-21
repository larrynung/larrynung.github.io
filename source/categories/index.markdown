---
layout: page
title: "categories"
date: 2013-11-10 23:56
comments: false
sharing: false
footer: false
---

<ul>
{% for item in site.categories %}
    <li><a href="/blog/categories/{{ item[0] }}/">{{ item[0] | capitalize }}</a> [ {{ item[1].size }} ]</li>
{% endfor %}
</ul>
