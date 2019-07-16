---
title: Blazor - Route to components
date: 2019-07-15 19:29:20
tags: [Blazor]
---

Blazor component 在未加掛 @page directive 時只能像 HTML element 一樣嵌入頁面使用。  

<!-- More -->

{% asset_img 1.png %}

</br>


如果要能直接當成頁面透過 Routing 訪問，可在 Blazor component 最前面加掛 @page directive，指定 Blazor component 的 routing。  

```html
@page "/counter"
...
```

</br>


像是下面這樣撰寫。  

```html
@page "/counter"


<h1>Counter</h1>


<p>Current count: @currentCount</p>


<button class="btn btn-primary" @onclick="@IncrementCount">Click me</button>


@code {
    int currentCount = 0;


    [Parameter]
    private int IncrementAmount { get; set; } = 1;


    void IncrementCount()
    {
        currentCount += IncrementAmount;
    }
}
```

{% asset_img 2.png %}

</br>


就可以透過 Routing 導到該 Blazor component，像是範本內的 Counter 就可以透過 https://localhost:5001/counter 訪問。  

{% asset_img 3.png %}
