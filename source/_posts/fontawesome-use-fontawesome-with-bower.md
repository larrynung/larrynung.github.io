---
layout: post
title: "FontAwesome - Use FontAwesome with bower"
date: 2016-02-17 05:33:00
comments: true
tags: [FontAwesome]
keywords: "FontAwesome"
description: "FontAwesome - Use FontAwesome with bower"
---

當我們透過 Bower 來使用 FontAwesome。  

<!-- More -->

{% img /images/posts/FontAwesomeWithBower/1.png %}

<br/>


下載下來的 FontAwesome CSS 內會用相對路徑指定所要使用的 Font 位置，但這樣在載入 CSS 時會指不到正確的 Font。  

```css
...
@font-face {
  font-family: 'FontAwesome';
  src: url('../fonts/fontawesome-webfont.eot?v=4.5.0');
  src: url('../fonts/fontawesome-webfont.eot?#iefix&v=4.5.0') format('embedded-opentype') , url('../fonts/fontawesome-webfont.woff2?v=4.5.0') format('woff2'), url('../fonts/fontawesome-webfont.woff?v=4.5.0') format('woff') , url('../fonts/fontawesome-webfont.ttf?v=4.5.0') format('truetype') , url('../fonts/fontawesome-webfont.svg?v=4.5.0#fontawesomeregular') format('svg') ;
  font-weight: normal;
  font-style: normal;
}
...
```

<br/>


{% img /images/posts/FontAwesomeWithBower/2.png %}

<br/>


當然我們可以透過 Grunt、Gupl 之類的自動化工具將路徑改掉，但這樣的做法感覺並不是很好，因此這邊筆者是使用自己的 CSS 將 Font 的位置改掉。  

```css
...
@font-face {
  font-family: 'FontAwesome';
  src: url('/wwwroot/lib/fontawesome/fonts/fontawesome-webfont.eot?v=4.5.0');
  src: url('/wwwroot/lib/fontawesome/fonts/fontawesome-webfont.eot?#iefix&v=4.5.0') format('embedded-opentype') , url('/wwwroot/lib/fontawesome/fonts/fontawesome-webfont.woff2?v=4.5.0') format('woff2'), url('/wwwroot/lib/fontawesome/fonts/fontawesome-webfont.woff?v=4.5.0') format('woff'), url('/wwwroot/lib/fontawesome/fonts/fontawesome-webfont.ttf?v=4.5.0') format('truetype'), url('/wwwroot/lib/fontawesome/fonts/fontawesome-webfont.svg?v=4.5.0#fontawesomeregular') format('svg') ;
}
...
```

<br/>


{% img /images/posts/FontAwesomeWithBower/3.png %}

<br/>


這樣改完後 FontAwesome 就可以正常使用。  
