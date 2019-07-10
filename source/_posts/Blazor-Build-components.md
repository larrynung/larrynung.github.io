---
title: Blazor - Build components
date: 2019-07-11 00:14:38
tags: [Blazor]
---

Blazor component 是 Blazor 的元件，類似控制項，是 Blazor 中可重複使用的最小單位。  

<!-- More -->

</br>

Blazor component 以 razor 為副檔名，它跟 ASP.NET MVC 的 Razor page 很像，會用 HTML 與 Razor 語法排版畫面。程式碼放在 @code {...} 內，程式碼可定義 Component 會用到的變數與方法，在畫面排版那邊可取用程式碼區塊中定義的變數與方法。  

</br>


這邊可參閱 Blazor 範本的 Counter 程式。程式碼那邊定義了一個 currentCount 的變數，以及一個 IncrementCount 方法，IncrementCount 方法只是很單純的將 currentCount 變數值加一。畫面這邊透過 @onclick="@IncrementCount" 指定畫面元素被按下時調用 IncrementCount 方法，並透過 @currentCount 將變數的值呈現在畫面上。  

```html
<h1>Counter</h1>


<p>Current count: @currentCount</p>


<button class="btn btn-primary" @onclick="@IncrementCount">Click me</button>


@code {
    private int currentCount = 0;


    private void IncrementCount()
    {
        currentCount++;
    }
}
```

{% asset_img 1.png %}

</br>


Blazor component 做好後，可以直接將它當成 HTML element 使用，像是要將剛剛建立的 Counter component 加入使用，可以像下面這樣撰寫:  


```html
@page "/"


<h1>Hello, world!</h1>


Welcome to your new app.


<Counter/>
```

{% asset_img 2.png %}

</br>


程式跑起來就可以看到建立的 Blazor component 在我們放置的位置上。   

{% asset_img 3.png %}

</br>


Blazor component 的功能也是正常的在運作。  

{% asset_img 4.png %}
