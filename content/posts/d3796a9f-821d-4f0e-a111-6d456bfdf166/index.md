---
title: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (五) 介面合約與抽象方法合約"
date: "2013-11-06 12:00:00"
description: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (五) 介面合約與抽象方法合約"
tags: [CSharp]
---

<p>介面合約主要功用為為實作介面的類別提供統一的驗證合約，當我們為介面定義好了介面合約以後，所有實作該介面的類別都會享有到合約驗證的好處，不需每個類別各自撰寫，可減少撰寫重覆的驗證合約程式、增加程式中合約驗證覆蓋完整度、與加快實現合約式編程。</p>  <p> </p>  <p>要使用介面契約，我們必須要加入對應該介面的驗證合約抽象類別，為介面提供對應的合約。透過使用成對的屬性ContractClass與ContractClassFor修飾驗證合約抽象類別與介面，其中ContractClass屬性表示所修飾的類別為介面，並指定介面對應的驗證合約抽象類別，而ContractClassFor屬性則表示所修飾的類別為驗證合約抽象類別，並指出該驗證合約抽象類別所對應的介面。</p>  <p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="clip_image002" width="578" height="453" src="\images\posts\d3796a9f-821d-4f0e-a111-6d456bfdf166