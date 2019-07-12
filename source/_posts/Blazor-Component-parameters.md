---
title: Blazor - Component parameters
date: 2019-07-12 19:51:47
tags: [Blazor]
---

若想讓 Blazor component 在畫面上使用時帶上參數做些設定，可以為 Component 加上 Parameter。  

<!-- More -->

</br>


只要在 code 區塊中加入帶有 ParameterAttribute 的 property 即可。  

```html
...
@code{
    ...
    [Parameter]
    private int IncrementAmount { get; set;     } = 1;
    ...
}
```

</br>


在畫面上就可以透過 Component parameter 對 Component 做些設定。  

```html
...
<Counter IncrementAmount="10" />
...
```

</br>


像是 Blazor 範本的 Counter component 可以改成像下面這樣:  

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

{% asset_img 1.png %}

</br>


加入 IncrementAmount parameter 供外部設定，IncrementCount 方法會依照 IncrementAmount 的值去增加 currentCount。  

</br>


Component parameter 開好後，畫面可直接設定 Parameter 的值。像是這邊設定 IncrementAmount 為 10。 

```html
@page "/"


<h1>Hello, world!</h1>


Welcome to your new app.


<Counter IncrementAmount="10" />
```

{% asset_img 2.png %}

</br>


運行後按下 Counter component 的按鈕。  

{% asset_img 3.png %}

</br>


Counter 的值就會加 10。  

{% asset_img 4.png %}
