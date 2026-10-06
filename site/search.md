---
layout: page
title: Search
permalink: /search/
---

Search the PHRAISE publication corpus by title, author, abstract, keyword,
journal, DOI, or cited reference. Results are generated entirely in your
browser; no query is sent to a server.

<link rel="stylesheet" href="{{ '/pagefind/pagefind-component-ui.css' | relative_url }}">
<script src="{{ '/pagefind/pagefind-component-ui.js' | relative_url }}" type="module"></script>

<pagefind-config
  base-url="{{ site.baseurl }}/"
  bundle-path="{{ '/pagefind/' | relative_url }}"
  excerpt-length="40">
</pagefind-config>

<pagefind-input placeholder="Search publications…"></pagefind-input>
<pagefind-summary></pagefind-summary>
<pagefind-results></pagefind-results>
