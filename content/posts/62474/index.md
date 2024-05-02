---
title: "[C++]使用nsiqcppstyle輔助檢查C/C++的Coding Style"
date: "2011-12-16 11:44:07"
description: "[C++]使用nsiqcppstyle輔助檢查C/C++的Coding Style"
tags: [Software,C++,Visual Studio]
---

<p>
	nsiqcppstyle是韓國人開發的C/C++ Coding Style檢查工具，可檢查程式碼並給予編碼上的建議，使用上十分的簡易，具有許約40幾條檢查的規則，檢查的規則能自動個更新且允許自行擴充。</p>
<p>
	 </p>
<p>
	工具部分可至nsiqcppstyle - C/C++ Coding Style Checker下載。</p>
<p>
	<img alt="image" border="0" height="585" src="\images\posts\62474\image12_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="614" /></p>
<p>
	 </p>
<p>
	下載後解壓縮可以看到如下的目錄結構，其中比較要關注的，nsiqcppstyle.exe是主要要運行的主控台程式，rules目錄內則是存放著所有檢查的規則。</p>
<p>
	<img alt="image" border="0" height="701" src="\images\posts\62474\image15_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="652" /></p>
<p>
	 </p>
<p>
	內建約有47個檢查規則，都是附檔名為py的文字檔。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\62474\image18_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="635" /></p>
<p>
	 </p>
<p>
	在運行nsiqcppstyle時程式都會嚐試去更新檢查的規則，不需使用者煩惱、不需手動的更新，檢查規則就能保持在最新的狀態。</p>
<p>
	<img alt="image" border="0" height="606" src="\images\posts\62474\image_thumb_1.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="681" /></p>
<p>
	 </p>
<p>
	nsiqcppstyle是主控台程式，使用時必須依自己的需求帶入正確的參數，參數的部分可運行nsiqcppstyle後參閱列出的使用說明。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:573f9376-fb06-449a-bec1-bf835fd47b7f" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="xml" name="code">
Usage : nsiqcppstyle [Options]
           targetdirectory

[Example]
   nsiqcppstyle .
   nsiqcppstyle targetdir
   nsiqcppstyle -f filefilterpath targetfilepath

[Options]
  -h            Show this help
  -v            Show detail ouput(verbose mode)
  -r            Show rule list
  -o path       Set the output path. It's only applied when the output is csv or
 xml.
  -f path       Set the filefilter path. If not provided, it uses the default fi
lterpath
                (target/filefilter.txt)
                If you provide the file path(not folder path) for the target,
                -f option should be provided.
  --var=key:value,key:value
                provide the variables to customize the rule behavior.
  --list-rules / -r  Show all rules available.
                Add file extensions to be counted as assigned languages.
  -s            Assign Filter scope name to be applied in this analysis
  --output=     output format 'emacs', 'vs7', 'csv', 'xml' and 'eclipse'. Defaul
t value is vs7
                emacs, vs7, eclipse output the result on the stdout in the form

                that each tool recognizes.
                csv and xml outputs the result on the file "nsiqcppstyle_result.
csv"
                "nsiqcppstyle_result.xml" respectively, if you don't provide -o
option.
  --ci          Continuous Integration mode. If this mode is on, this tool only
report summary.</pre>
</div>
<p>
	 </p>
<p>
	使用上十分的簡單，最簡單的使用方式就是像使用說明說的一樣，帶入『.』檢查當前目錄下的程式碼。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e91ef18d-d251-459f-945a-36ea4048979e" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="xml" name="code">
nsiqcppstyle .</pre>
</div>
<p>
	 </p>
<p>
	也可以明確帶入要檢查的目錄讓程式去檢查目錄裡面的程式碼。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5469d207-c4e1-4ea3-ac71-26c00c5972ae" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
nsiqcppstyle "C:\Users\Larry\Documents\Visual Studio 2010\Projects\MFCApplication\MFCApplication"</pre>
</div>
<p>
	 </p>
<p>
	或是用『-f』帶入要套用的檢查規則設定檔與要檢查的單一程式碼。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ae944cd4-b3d2-4392-a325-2312ae32d4c4" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="xml" name="code">
nsiqcppstyle -f filefilter.txt Test_nsiqcppstyle.cpp</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	這邊需特別注意，在用nsiqcppstyle在做程式碼檢查時，必須先產生檢查規則設定檔，不然運行檢查時會有錯誤產生。</p>
<p>
	<img alt="image" border="0" height="350" src="\images\posts\62474\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="681" /></p>
<p>
	 </p>
<p>
	檢查規則設定檔可是用以指定在進行程式碼檢查時要套用哪些檢查的規則，最簡單的產生方式就是像是下面這樣將所有可用的檢查規則轉印到filefilter.txt檔。</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e2205f46-422e-4e64-bca3-ad2d98567342" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="xml" name="code">
nsiqcppstyle.exe -r &gt;&gt; filefilter.txt</pre>
</div>
<p>
	 </p>
<p>
	產出的filefilter.txt檔它的內容會像下面這樣：</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:329b564a-39de-490e-b20f-9bb91cd2b17b" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="xml" name="code">
~ RULE_10_1_A_do_not_use_bufferoverflow_risky_function_for_unix
~ RULE_10_1_B_do_not_use_bufferoverflow_risky_function_for_windows
~ RULE_3_1_A_do_not_start_filename_with_underbar
~ RULE_3_2_B_do_not_use_same_filename_more_than_once
~ RULE_3_2_CD_do_not_use_special_characters_in_filename
~ RULE_3_2_F_use_representitive_classname_for_cpp_filename
~ RULE_3_2_H_do_not_use_underbars_for_cpp_filename
~ RULE_3_2_H_do_not_use_uppercase_for_c_filename
~ RULE_3_3_A_start_function_name_with_is_or_has_when_return_bool
~ RULE_3_3_A_start_function_name_with_lowercase_unix
~ RULE_3_3_A_start_function_name_with_upperrcase_windows
~ RULE_3_3_B_start_private_function_name_with_underbar
~ RULE_4_1_A_A_use_tab_for_indentation
~ RULE_4_1_A_B_use_space_for_indentation
~ RULE_4_1_B_indent_each_enum_item_in_enum_block
~ RULE_4_1_B_locate_each_enum_item_in_seperate_line
~ RULE_4_1_C_align_long_function_parameter_list
~ RULE_4_1_E_align_conditions
~ RULE_4_2_A_A_space_around_operator
~ RULE_4_2_A_B_space_around_word
~ RULE_4_4_A_do_not_write_over_120_columns_per_line
~ RULE_4_5_A_brace_for_namespace_should_be_located_in_seperate_line
~ RULE_4_5_A_braces_for_function_definition_should_be_located_in_seperate_line
~ RULE_4_5_A_braces_for_type_definition_should_be_located_in_seperate_line
~ RULE_4_5_A_braces_inside_of_function_should_be_located_in_end_of_line
~ RULE_4_5_A_indent_blocks_inside_of_function
~ RULE_4_5_A_matching_braces_inside_of_function_should_be_located_same_column
~ RULE_4_5_B_use_braces_even_for_one_statement
~ RULE_5_2_C_provide_doxygen_class_comment_on_class_def
~ RULE_5_2_C_provide_doxygen_namespace_comment_on_namespace_def
~ RULE_5_2_C_provide_doxygen_struct_comment_on_struct_def
~ RULE_5_3_A_provide_doxygen_function_comment_on_function_in_header
~ RULE_5_3_A_provide_doxygen_function_comment_on_function_in_impl
~ RULE_6_1_A_do_not_omit_function_parameter_names
~ RULE_6_1_E_do_not_use_more_than_5_paramters_in_function
~ RULE_6_1_G_write_less_than_200_lines_for_function
~ RULE_6_2_A_do_not_use_system_dependent_type
~ RULE_6_4_B_initialize_first_item_of_enum
~ RULE_6_5_B_do_not_use_lowercase_for_macro_constants
~ RULE_6_5_B_do_not_use_macro_for_constants
~ RULE_7_1_B_A_do_not_use_double_assignment
~ RULE_7_1_C_do_not_use_question_keyword
~ RULE_7_2_B_do_not_use_goto_statement
~ RULE_8_1_A_provide_file_info_comment
~ RULE_9_1_A_do_not_use_hardcorded_include_path
~ RULE_9_2_D_use_reentrant_function
~ RULE_A_3_avoid_too_deep_blocks</pre>
</div>
<p>
	 </p>
<p>
	用這個檢查規則設定檔可以套用所有的檢查規則去做檢查，若有需要也可以開啟這個產生出來的檔案，將不想要檢查的規則給過濾掉。</p>
<p>
	 </p>
<p>
	檢查規則設定檔準備好後就可以開始運行了，運行後會顯示檢查的結果，檔案哪一行哪一列，違反了哪個規則都會清楚的條列出來。</p>
<p>
	<img alt="image" border="0" height="350" src="\images\posts\62474\image_thumb_3.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="681" /></p>
<p>
	 </p>
<p>
	後面還會依檢查結果做些統計，像是可以取得的檢查規則有幾項、套用的檢查規則有幾項、總共違反幾項規則、總共有幾個錯誤被檢查到、總共分析幾個檔案...等。</p>
<p>
	<img alt="image" border="0" height="238" src="\images\posts\62474\image_thumb_4.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="681" /></p>
<p>
	 </p>
<p>
	若想進一步了解每個檢查規則總共違反的檔案數，或是想要依檔案去查閱違反的檢查規則都可以。</p>
<p>
	<img alt="image" border="0" height="238" src="\images\posts\62474\image_thumb_5.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="681" /></p>
<p>
	<img alt="image" border="0" height="238" src="\images\posts\62474\image_thumb_6.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="681" /></p>
<p>
	 </p>
<p>
	在查閱程式碼檢查出來的結果時，若有不清楚的規則想要查閱更詳細的資料，我們可以回到一開始說的rules目錄將對應的rule檔開啟，或是到N'SIQ CppStyle Style Doc去查閱，這邊都寫得很清楚。</p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\62474\image21_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="614" /></p>
<p>
	 </p>
<p>
	若要將nsiqcppstyle與Visual Studio整合也可以，透過Visual Studio的外部工具就可以了，若要檢查整個專案內的程式，需將Command部分設定nsiqcppstyle的主程式，而參數部分設定$(ProjectDir)，『Use Output window』也要記得選取。</p>
<p>
	<img alt="image" border="0" height="492" src="\images\posts\62474\image_thumb_9.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="475" /></p>
<p>
	 </p>
<p>
	運行後程式碼檢查的結果就會輸出在輸出視窗。</p>
<p>
	<img alt="image" border="0" height="713" src="\images\posts\62474\image_thumb_10.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="676" /></p>
<p>
	 </p>
<p>
	若有需要檢查當前開啟的程式碼，也可以透過Visual Studio的外部程式去處理，跟剛剛一樣的步驟參數的部分設定像下面這樣指定檢查規則設定檔與當前開啟的程式碼位置就可以了。</p>
<p>
	<img alt="image" border="0" height="492" src="\images\posts\62474\image_thumb_11.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="475" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		nsiqcppstyle - C/C++ Coding Style Checker</li>
	<li>
		C/C++编码风格自动检查工具--nsiqcppstyle使用手册--中文版</li>
	<li>
		N'SIQ CppStyle</li>
	<li>
		N'SIQ CppStyle Rule Server</li>
	<li>
		N'SIQ CppStyle Style Doc</li>
</ul>
