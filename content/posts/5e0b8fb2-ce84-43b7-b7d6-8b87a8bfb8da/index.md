---
title: "Python's and_or operation"
date: "2013-11-06 12:00:00"
description: "Python's and_or operation"
tags: [Python]
---

<p>在Python中除了Boolean的True以外，非空的值亦視為True，反之則視為False。所謂的空值指的就是0、空字串、空集合、空的Tuple...，所以除了False以外，0、''、()、[]、{}...在Python中也都代表著False。</p>  <p> </p>  <p>因為有這樣的特性，Python中and/or運算變得非常的有趣。</p>  <p> </p>  <p>以and操作來說，and運算是條件都成立就成立，當一個條件不成立即可判斷整個條件不成立。所以假設and運算式中看到了False的值就會停止繼續往下判斷，而若是看到了True的值則會繼續往下判斷。</p>  <p> </p>  <p>所以像是下面這樣的例子：</p>  <div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:1aba90e4-2389-47e1-ac36-39d310247c5a" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="py">print "'a' and 'b': ", 'a' and 'b'                           
print "'' and 'b': ", '' and 'b'                              
print "'a' and '': ", 'a' and ''                               
print "'a' and 'b' and 'c': ", 'a' and 'b' and 'c'      </pre></div>

<p> </p>

<p>運行起來就會像下面這樣：</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\5e0b8fb2-ce84-43b7-b7d6-8b87a8bfb8da\image_thumb_1.png" width="385" height="192" /></p>

<p> </p>

<p>以'a' and 'b'來說，因為'a'為True，所以需要繼續往下判斷，而'b'亦為True，所以直接回傳'b'。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:688a732c-3df7-4f46-a539-b222b910c4f9" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="py">print "'a' and 'b': ", 'a' and 'b'</pre></div>

<p> </p>

<p>以'' and 'b'來說，因為''為False，所以整個判斷式注定為不成立，不需要繼續往下判斷，故直接回傳''。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:aaff491a-b7a2-4907-97fd-f15aad2e65d6" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="py">print "'' and 'b': ", '' and 'b'         </pre></div>

<p> </p>

<p>其它兩個以此類推。</p>

<p> </p>

<p>以or操作來說，or運算是條件一個成立就成立，當一個條件成立即可判斷整個條件成立。所以假設or運算式中看到了True的值就會停止繼續往下判斷，而若是看到了False的值則會繼續往下判斷。</p>

<p> </p>

<p>所以像是下面這樣的例子：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c0235958-f746-4304-934a-a67f664e8049" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="py">print "'a' or 'b': ", 'a' or 'b'                       		
print "'' or 'b': ", '' or 'b'                          		
print "'a' or '': ", 'a' or ''                          		
print "0 or '' or [] or {}: ", 0 or '' or [] or {}     </pre></div>

<p> </p>

<p>運行起來就會像下面這樣：</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\5e0b8fb2-ce84-43b7-b7d6-8b87a8bfb8da\image_thumb_2.png" width="361" height="176" /> </p>

<p> </p>

<p>以'a' or 'b'來說，因為'a'為True，所以不需要繼續往下判斷，直接回傳'a'。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:aa2b0898-ff8f-4767-930c-0a18f67636fa" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="py">print "'a' or 'b': ", 'a' or 'b'              </pre></div>

<p> </p>

<p>以'' or 'b'來說，因為''為False，所以需要繼續往下判斷，而'b'亦為True，所以直接回傳'b'。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5b3dfafa-1879-4153-abf7-5d1cd9e9028b" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="py">print "'' or 'b': ", '' or 'b'    </pre></div>

<p> </p>

<p>其它兩個一樣以此類推。</p>

<p> </p>

<p>不過雖然Python and/or運算有著這樣的特性，但是仍舊不完全等價本來的Boolean型別，所以無法直接將之與Boolean型別的True/False去做比對，以下面這個例子來說：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:46a22144-dc66-4a96-959b-e4ff0474e8e1" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="py">print "'a' == True: ", 'a' == True
print "'a' is True: ", 'a' is True
print "bool('a') == True: ", bool('a') == True
print "bool('a') is True: ", bool('a') is True
print "'a' == ('a' and 'b'): ", 'a' == ('a' and 'b')
print "'b' == ('a' and 'b'): ", 'b' == ('a' and 'b')
print "'a' == ('a' or 'b'): ", 'a' == ('a' or 'b')
print "'b' == ('a' or 'b'): ", 'b' == ('a' or 'b')</pre></div>

<p> </p>

<p>我們可以看到直接去用==運算子或是is關鍵字下去判斷是否為True是無效的，若需要類似這樣的判斷，我們會需要用內建的函式或是用特定的運算式去輔助處理。</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\5e0b8fb2-ce84-43b7-b7d6-8b87a8bfb8da\image_thumb_6.png" width="409" height="240" /> </p>

<p> </p>

<p>最後來看一下三元運算的部分，先來看一下程式碼的部分：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:a4458fd8-680e-432f-a8fb-ad24a77cd6fb" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="py">print "True and 'TrueValue' or 'FalseValue': ", True and 'TrueValue' or 'FalseValue'
print "False and 'TrueValue' or 'FalseValue': ", False and 'TrueValue' or 'FalseValue'
print "True and '' or 'FalseValue': ", True and '' or 'FalseValue'
print "(True and [''] or ['FalseValue'])[0]: ", (True and [''] or ['FalseValue'])[0]</pre></div>

<p> </p>

<p>其運行結果為：</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\5e0b8fb2-ce84-43b7-b7d6-8b87a8bfb8da\image_thumb_4.png" width="513" height="192" /> </p>

<p> </p>

<p>可以看到若三元運算選取的兩個值都不為空的話，我們可以簡單的用[expression] and [value1] or [value2]這樣的方式下去撰寫。因為expression與value1之間為and運算，若expression為true則會去看value1的值，而與value2之間為or運算，value1的值又不為空值，所以會直接回傳value1；若expression為false，因為[expression] and [value1]運算出來為[expression]，所以運算式等同[expression] or [value2]，故回傳value2的值。等同於我們一般看到的三元運算效果。</p>

<p> </p>

<p>但是這樣的寫法有個前提就是必須三元運算選取的兩個值都不為空，若是為空則整個效果就會不如預期，所以在使用時我們可以以陣列的方式下去封裝一下，以([expression] and [[value1]] or [[value2]])[0]這樣的方式下去撰寫。</p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Built-in Types</li>
</ul>
