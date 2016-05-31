---
layout: post
title: "Bootstrap - Use Glyphicons with bower"
date: 2016-02-18 05:46:00
comments: true
tags: [Bootstrap]
keywords: "Bootstrap, Bower, Glyphicons"
description: "Bootstrap - Use Glyphicons with bower"
---

當我們透過 Bower 來使用 Bootstrap Glyphicons。  

<!-- More -->

{% img /images/posts/GlyphiconsWithBower/1.png %}

<br/>


下載下來的 Glyphicons CSS 內會用相對路徑指定所要使用的 Font 位置，但這樣在載入 CSS 時會指不到正確的 Font。  


{% codeblock lang:css %}
...
@font-face {
  font-family: 'Glyphicons Halflings';

  src: url('../fonts/glyphicons-halflings-regular.eot');
  src: url('../fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype') , url('../fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../fonts/glyphicons-halflings-regular.woff') format('woff') , url('../fonts/glyphicons-halflings-regular.ttf') format('truetype') , url('../fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
...
{% endcodeblock %}

<br/>


{% img /images/posts/GlyphiconsWithBower/2.png %}

<br/>



當然我們可以透過 Grunt、Gupl 之類的自動化工具將路徑改掉，但這樣的做法感覺並不是很好，因此這邊筆者是使用自己的 CSS 將 Font 的位置改掉。  

{% codeblock lang:css %}
...
@font-face {
  font-family: 'Glyphicons Halflings';

  src: url('/wwwroot/lib/bootstrap/dist/fonts/glyphicons-halflings-regular.eot');
  src: url('/wwwroot/lib/bootstrap/dist/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype') , url('/wwwroot/lib/bootstrap/dist/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('/wwwroot/lib/bootstrap/dist/fonts/glyphicons-halflings-regular.woff') format('woff'), url('/wwwroot/lib/bootstrap/dist/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('/wwwroot/lib/bootstrap/dist/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg') ;
}
...
{% endcodeblock %}

<br/>


{% img /images/posts/GlyphiconsWithBower/3.png %}

<br/>


這樣改完後 Glyphicons 就可以正常使用。 
