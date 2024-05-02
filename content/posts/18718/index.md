---
title: ".NET 4.0 New Feature - Complex"
date: "2010-11-01 07:55:42"
description: ".NET 4.0 New Feature - Complex"
tags: [VB.NET]
---

<p>.NET 4.0新增了Complex類別，位於System.Numerics.dll組件內的System.Numerics中，可用來描述與處理複數資料，具備數值比對、算術運算、其它數值運算 、與三角運算等複數資料運算的能力。</p>  <p> </p>  <p>使用上需先加入System.Numerics.dll組件參考</p>  <p><img style="border-top-width: 0px; border-left-width: 0px; border-bottom-width: 0px; border-right-width: 0px" height="372" alt="image" src="\images\posts\18718\image_thumb.png" width="644" border="0" /></p>  <p> </p>  <p>並將System.Numerics命名空間匯入</p>  <div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:17a37601-1da8-42ef-836e-fb8a1c392d89" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Imports System.Numerics</pre></div>

<p>加入了參考與命名空間後，我們就可以開始來使用Complex型別了。首先，我們必需建立Complex型別變數。</p>

<p> </p>

<p>Complex型別變數有三種建立方式，一種是透過Complex的建構子將數值的實數部份與虛數部份帶入建構子建構。</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:72f887d1-464d-480f-982c-f45ab98d3bce" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Dim c As New Complex(12, 6)</pre></div>

<p> </p>

<p>一種則是先宣告出Complex變數，在將值塞入後使用。</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:045264ab-f013-40d7-88a9-59f4c0da30c3" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Dim c As Complex = 3.14</pre></div>

<p> </p>

<p>這邊需注意到的是，由於Complex是用以表示複數，而複數是由實數部份與虛數部份所構成，因此採用這種直接把值塞入的作法，只能設定到複數的實數部份，虛數部份會被設定為0。</p>

<p> </p>

<p>最後一種則是透過Complex.FromPolarCoordinates靜態方法來從極座標建立Complex變數</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5b112549-9c67-4abe-aaf4-61c0ee3f5c5b" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Dim c As Complex = Complex.FromPolarCoordinates(10, .524)</pre></div>

<p> </p>

<p>建立完後可對其做些運算處理，這邊不一一詳述，自行參閱下方整理的範例：</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:83ffc766-33d0-4ec7-83f7-018f19c61fdc" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Imports System.Numerics
Module Module1

    Sub Main()
        ShowDetail("Complex.Zero", Complex.Zero)
        ShowDetail("Complex.One", Complex.One)

        Dim c1 As New Complex(1, 2)
        Dim c2 As New Complex(3, 4)

        ShowDetail("C1", c1)
        ShowDetail("C2", c2)

        'Complex +-*/
        Console.WriteLine("{0} + {1} = {2}", c1, c2, c1 + c2)
        Console.WriteLine("{0} - {1} = {2}", c1, c2, c1 - c2)
        Console.WriteLine("{0} * {1} = {2}", c1, c2, c1 * c2)
        Console.WriteLine("{0} / {1} = {2}", c1, c2, c1 / c2)

        Console.WriteLine()

        Console.WriteLine("Complex.Add({0}, {1}) = {2}", c1, c2, Complex.Add(c1, c2))
        Console.WriteLine("Complex.Subtract({0}, {1}) = {2}", c1, c2, Complex.Subtract(c1, c2))
        Console.WriteLine("Complex.Multiply({0}, {1}) = {2}", c1, c2, Complex.Multiply(c1, c2))
        Console.WriteLine("Complex.Divide({0}, {1}) = {2}", c1, c2, Complex.Divide(c1, c2))

        Console.WriteLine()

        'Other Complex operation
        Console.WriteLine("Complex.Divide({0}) = {1}", c1, Complex.Conjugate(c1))
        Console.WriteLine("Complex.Abs({0}) = {1}", c1, Complex.Abs(c1))
        Console.WriteLine("Complex.Negate({0}) = {1}", c1, Complex.Negate(c1))
        Console.WriteLine("Complex.Pow({0}, 2) = {1}", c1, Complex.Pow(c1, 2))
        Console.WriteLine("Complex.Pow({0}, {1}) = {2}", c1, c2, Complex.Pow(c1, c2))
        Console.WriteLine("Complex.Sqrt({0}) = {1}", c1, Complex.Sqrt(c1))
        Console.WriteLine("Complex.Reciprocal({0}) = {1}", c1, Complex.Reciprocal(c1))
        Console.WriteLine("Complex.Log({0}) = {1}", c1, Complex.Log(c1))
        Console.WriteLine("Complex.Log10({0}) = {1}", c1, Complex.Log10(c1))
        Console.WriteLine("Complex.exp({0}) = {1}", c1, Complex.Exp(c1))

        Console.WriteLine()

        Console.WriteLine("Complex.Sin({0}) = {1}", c1, Complex.Sin(c1))
        Console.WriteLine("Complex.Sinh({0}) = {1}", c1, Complex.Sinh(c1))
        Console.WriteLine("Complex.Cos({0}) = {1}", c1, Complex.Cos(c1))
        Console.WriteLine("Complex.Cosh({0}) = {1}", c1, Complex.Cosh(c1))
        Console.WriteLine("Complex.Tan({0}) = {1}", c1, Complex.Tan(c1))
        Console.WriteLine("Complex.Tanh({0}) = {1}", c1, Complex.Tanh(c1))
        Console.WriteLine("Complex.Asin({0}) = {1}", c1, Complex.Asin(c1))
        Console.WriteLine("Complex.Acos({0}) = {1}", c1, Complex.Acos(c1))
        Console.WriteLine("Complex.Atan({0}) = {1}", c1, Complex.Atan(c1))
    End Sub

    Private Sub ShowDetail(ByVal varName As String, ByVal c As Complex)
        Console.WriteLine("{0}: {1}", varName, c)
        ShowDetail(c)
        Console.WriteLine()
    End Sub

    Private Sub ShowDetail(ByVal c As Complex)
        Console.WriteLine("Real: {0}", c.Real)
        Console.WriteLine("Imaginary: {0}", c.Imaginary)
        Console.WriteLine("Phase: {0}", c.Phase)
        Console.WriteLine("Magnitude: {0}", c.Magnitude)
    End Sub

End Module</pre></div>

<p> </p>

<p>運行結果如下：</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:220e6c50-d731-47f0-9cd2-e77c9ac3adda" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="xml">Complex.Zero: (0, 0)
Real: 0
Imaginary: 0
Phase: 0
Magnitude: 0

Complex.One: (1, 0)
Real: 1
Imaginary: 0
Phase: 0
Magnitude: 1

C1: (1, 2)
Real: 1
Imaginary: 2
Phase: 1.10714871779409
Magnitude: 2.23606797749979

C2: (3, 4)
Real: 3
Imaginary: 4
Phase: 0.927295218001612
Magnitude: 5

(1, 2) + (3, 4) = (4, 6)
(1, 2) - (3, 4) = (-2, -2)
(1, 2) * (3, 4) = (-5, 10)
(1, 2) / (3, 4) = (0.44, 0.08)

Complex.Add((1, 2), (3, 4)) = (4, 6)
Complex.Subtract((1, 2), (3, 4)) = (-2, -2)
Complex.Multiply((1, 2), (3, 4)) = (-5, 10)
Complex.Divide((1, 2), (3, 4)) = (0.44, 0.08)

Complex.Divide((1, 2)) = (1, -2)
Complex.Abs((1, 2)) = 2.23606797749979
Complex.Negate((1, 2)) = (-1, -2)
Complex.Pow((1, 2), 2) = (-3, 4)
Complex.Pow((1, 2), (3, 4)) = (0.129009594074467, 0.0339240929051702)
Complex.Sqrt((1, 2)) = (1.27201964951407, 0.786151377757423)
Complex.Reciprocal((1, 2)) = (0.2, -0.4)
Complex.Log((1, 2)) = (0.80471895621705, 1.10714871779409)
Complex.Log10((1, 2)) = (0.349485002168008, 0.480828578784232)
Complex.exp((1, 2)) = (-1.13120438375681, 2.47172667200482)

Complex.Sin((1, 2)) = (3.16577851321617, 1.95960104142161)
Complex.Sinh((1, 2)) = (-0.489056259041294, 1.40311925062204)
Complex.Cos((1, 2)) = (2.03272300701967, -3.0518977991518)
Complex.Cosh((1, 2)) = (-0.64214812471552, 1.06860742138278)
Complex.Tan((1, 2)) = (0.0338128260798967, 1.01479361614663)
Complex.Tanh((1, 2)) = (1.16673625724092, -0.243458201185725)
Complex.Asin((1, 2)) = (0.427078586392476, 1.528570919481)
Complex.Acos((1, 2)) = (1.14371774040242, -1.528570919481)
Complex.Atan((1, 2)) = (1.33897252229449, 0.402359478108525)</pre></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Complex 結構 </li>

  <li>Complex 成員 </li>

  <li>.Net Framework 4.0: Complex numbers </li>

  <li>C# 4.0/BCL 4 Series: Complex numeric type </li>
</ul>
