---
layout: page
title: Keywords
---

<!-- See https://blog.lanyonm.org/articles/2013/11/21/alphabetize-jekyll-page-tags-pure-liquid.html -->
<!-- With added pipe to handle lack of sort_natural -->
{% capture site_tags %}{% for tag in site.tags %}{{ tag | first | downcase }}|{{ tag | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
<!-- site_tags: {{ site_tags }} -->
{% assign tag_words = site_tags | split:',' | sort %}
<!-- tag_words: {{ tag_words }} -->

<div class="home">
  <div class="grid tags-list">
    {% for tag_pair in tag_words %}
    {% assign tag = tag_pair | split:'|' | last %}
    <a href="#{{ tag | slugify }}" class="tag-link" style="font-size: {{ site.tags[tag] | size | times: 10 | plus: 70 }}%">
      <span class="tag-name">{{ tag }}</span>
      <span class="tag-count">({{ site.tags[tag] | size }})</span>
    </a>
    {% endfor %}
  </div>

  <hr />
  
  <div class="posts-by-tag">
  {% for tag_pair in tag_words %}
  {% assign tag = tag_pair | split:'|' | last %}
  <div id="{{ tag | slugify }}" class="posts-for-tag">
  <h2 class="post-list-heading">{{ tag | capitalize }}</h2>
  <ul class="post-list">
    {% if site.tags[tag].size > 0 %}
      {% assign posts = site.tags[tag] | sort: 'year' | reverse %}
      {% for post in posts %}
        <li>
          <span class="post-meta">{{ post.year }} -- {{ post.authors }}</span>
          <h3>
            <a class="post-link" href="{{ post.url | relative_url }}">
              {{ post.title | escape }}
            </a>
          </h3>
        </li>
      {% endfor %}
    {% endif %}
  </ul>
  </div>
  {% endfor %}
  </div>
</div>
