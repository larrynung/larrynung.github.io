---
layout: post
title: "T4 template - CultureNames.tt"
date: 2016-03-08 05:31:00
comments: true
tags: [T4]
keywords: "T4, Culture"
description: "T4 template - CultureNames.tt"
---

.NET 在操作 Culture 時，免不了要帶入 CultureInfo 的 Name，多半是用 Hard code 的形式帶入，像是下面這樣：  

<!-- More -->  

{% codeblock lang:c# %}
...
var currentThread = Thread.CurrentThread;
currentThread.CurrentCulture = CultureInfo.GetCultureInfo("zh-tw");
...
{% endcodeblock %}

<br/>

{% img /images/posts/T4CultureNames/1.png %}

<br/>


這邊筆者做了個 T4 Template，期望能解決這樣的問題。  

{% codeblock lang:c# %}
<#@ template debug="false" hostspecific="false" language="C#" #>
<#@ assembly name="System.Core" #>
<#@ import namespace="System.Globalization" #>
<#@ import namespace="System.Linq" #>
<#@ import namespace="System.Text" #>
<#@ import namespace="System.Collections.Generic" #>
<#@ output extension=".cs" #>
namespace System.Globalization
{
    public static class CultureNames
    {
<#
        var cultures = CultureInfo.GetCultures(CultureTypes.SpecificCultures);
		var length = cultures.Count();
        foreach(var culture in cultures)
        {
			var cultureName = culture.Name;
#>
		/// <summary>
        /// <#=cultureName#>
        /// </summary>
		public const string <#=cultureName.Replace("-","_").ToUpper()#> = "<#=cultureName#>";

<#
		}
#>
    }
}
{% endcodeblock %}

<br/>


該  T4 Template 運行後會將所有可用的 Culture Name 彙整成一個靜態類別。  

{% codeblock lang:c# %}
namespace System.Globalization
{
    public static class CultureNames
    {
		/// <summary>
        /// ar-SA
        /// </summary>
		public const string AR_SA = "ar-SA";

		/// <summary>
        /// bg-BG
        /// </summary>
		public const string BG_BG = "bg-BG";

		/// <summary>
        /// ca-ES
        /// </summary>
		public const string CA_ES = "ca-ES";

		/// <summary>
        /// zh-TW
        /// </summary>
		public const string ZH_TW = "zh-TW";

		/// <summary>
        /// cs-CZ
        /// </summary>
		public const string CS_CZ = "cs-CZ";

		/// <summary>
        /// da-DK
        /// </summary>
		public const string DA_DK = "da-DK";

		/// <summary>
        /// de-DE
        /// </summary>
		public const string DE_DE = "de-DE";

		/// <summary>
        /// el-GR
        /// </summary>
		public const string EL_GR = "el-GR";

		/// <summary>
        /// en-US
        /// </summary>
		public const string EN_US = "en-US";

		/// <summary>
        /// fi-FI
        /// </summary>
		public const string FI_FI = "fi-FI";

		/// <summary>
        /// fr-FR
        /// </summary>
		public const string FR_FR = "fr-FR";

		/// <summary>
        /// he-IL
        /// </summary>
		public const string HE_IL = "he-IL";

		/// <summary>
        /// hu-HU
        /// </summary>
		public const string HU_HU = "hu-HU";

		/// <summary>
        /// is-IS
        /// </summary>
		public const string IS_IS = "is-IS";

		/// <summary>
        /// it-IT
        /// </summary>
		public const string IT_IT = "it-IT";

		/// <summary>
        /// ja-JP
        /// </summary>
		public const string JA_JP = "ja-JP";

		/// <summary>
        /// ko-KR
        /// </summary>
		public const string KO_KR = "ko-KR";

		/// <summary>
        /// nl-NL
        /// </summary>
		public const string NL_NL = "nl-NL";

		/// <summary>
        /// nb-NO
        /// </summary>
		public const string NB_NO = "nb-NO";

		/// <summary>
        /// pl-PL
        /// </summary>
		public const string PL_PL = "pl-PL";

		/// <summary>
        /// pt-BR
        /// </summary>
		public const string PT_BR = "pt-BR";

		/// <summary>
        /// rm-CH
        /// </summary>
		public const string RM_CH = "rm-CH";

		/// <summary>
        /// ro-RO
        /// </summary>
		public const string RO_RO = "ro-RO";

		/// <summary>
        /// ru-RU
        /// </summary>
		public const string RU_RU = "ru-RU";

		/// <summary>
        /// hr-HR
        /// </summary>
		public const string HR_HR = "hr-HR";

		/// <summary>
        /// sk-SK
        /// </summary>
		public const string SK_SK = "sk-SK";

		/// <summary>
        /// sq-AL
        /// </summary>
		public const string SQ_AL = "sq-AL";

		/// <summary>
        /// sv-SE
        /// </summary>
		public const string SV_SE = "sv-SE";

		/// <summary>
        /// th-TH
        /// </summary>
		public const string TH_TH = "th-TH";

		/// <summary>
        /// tr-TR
        /// </summary>
		public const string TR_TR = "tr-TR";

		/// <summary>
        /// ur-PK
        /// </summary>
		public const string UR_PK = "ur-PK";

		/// <summary>
        /// id-ID
        /// </summary>
		public const string ID_ID = "id-ID";

		/// <summary>
        /// uk-UA
        /// </summary>
		public const string UK_UA = "uk-UA";

		/// <summary>
        /// be-BY
        /// </summary>
		public const string BE_BY = "be-BY";

		/// <summary>
        /// sl-SI
        /// </summary>
		public const string SL_SI = "sl-SI";

		/// <summary>
        /// et-EE
        /// </summary>
		public const string ET_EE = "et-EE";

		/// <summary>
        /// lv-LV
        /// </summary>
		public const string LV_LV = "lv-LV";

		/// <summary>
        /// lt-LT
        /// </summary>
		public const string LT_LT = "lt-LT";

		/// <summary>
        /// tg-Cyrl-TJ
        /// </summary>
		public const string TG_CYRL_TJ = "tg-Cyrl-TJ";

		/// <summary>
        /// fa-IR
        /// </summary>
		public const string FA_IR = "fa-IR";

		/// <summary>
        /// vi-VN
        /// </summary>
		public const string VI_VN = "vi-VN";

		/// <summary>
        /// hy-AM
        /// </summary>
		public const string HY_AM = "hy-AM";

		/// <summary>
        /// az-Latn-AZ
        /// </summary>
		public const string AZ_LATN_AZ = "az-Latn-AZ";

		/// <summary>
        /// eu-ES
        /// </summary>
		public const string EU_ES = "eu-ES";

		/// <summary>
        /// hsb-DE
        /// </summary>
		public const string HSB_DE = "hsb-DE";

		/// <summary>
        /// mk-MK
        /// </summary>
		public const string MK_MK = "mk-MK";

		/// <summary>
        /// tn-ZA
        /// </summary>
		public const string TN_ZA = "tn-ZA";

		/// <summary>
        /// xh-ZA
        /// </summary>
		public const string XH_ZA = "xh-ZA";

		/// <summary>
        /// zu-ZA
        /// </summary>
		public const string ZU_ZA = "zu-ZA";

		/// <summary>
        /// af-ZA
        /// </summary>
		public const string AF_ZA = "af-ZA";

		/// <summary>
        /// ka-GE
        /// </summary>
		public const string KA_GE = "ka-GE";

		/// <summary>
        /// fo-FO
        /// </summary>
		public const string FO_FO = "fo-FO";

		/// <summary>
        /// hi-IN
        /// </summary>
		public const string HI_IN = "hi-IN";

		/// <summary>
        /// mt-MT
        /// </summary>
		public const string MT_MT = "mt-MT";

		/// <summary>
        /// se-NO
        /// </summary>
		public const string SE_NO = "se-NO";

		/// <summary>
        /// ms-MY
        /// </summary>
		public const string MS_MY = "ms-MY";

		/// <summary>
        /// kk-KZ
        /// </summary>
		public const string KK_KZ = "kk-KZ";

		/// <summary>
        /// ky-KG
        /// </summary>
		public const string KY_KG = "ky-KG";

		/// <summary>
        /// sw-KE
        /// </summary>
		public const string SW_KE = "sw-KE";

		/// <summary>
        /// tk-TM
        /// </summary>
		public const string TK_TM = "tk-TM";

		/// <summary>
        /// uz-Latn-UZ
        /// </summary>
		public const string UZ_LATN_UZ = "uz-Latn-UZ";

		/// <summary>
        /// tt-RU
        /// </summary>
		public const string TT_RU = "tt-RU";

		/// <summary>
        /// bn-IN
        /// </summary>
		public const string BN_IN = "bn-IN";

		/// <summary>
        /// pa-IN
        /// </summary>
		public const string PA_IN = "pa-IN";

		/// <summary>
        /// gu-IN
        /// </summary>
		public const string GU_IN = "gu-IN";

		/// <summary>
        /// or-IN
        /// </summary>
		public const string OR_IN = "or-IN";

		/// <summary>
        /// ta-IN
        /// </summary>
		public const string TA_IN = "ta-IN";

		/// <summary>
        /// te-IN
        /// </summary>
		public const string TE_IN = "te-IN";

		/// <summary>
        /// kn-IN
        /// </summary>
		public const string KN_IN = "kn-IN";

		/// <summary>
        /// ml-IN
        /// </summary>
		public const string ML_IN = "ml-IN";

		/// <summary>
        /// as-IN
        /// </summary>
		public const string AS_IN = "as-IN";

		/// <summary>
        /// mr-IN
        /// </summary>
		public const string MR_IN = "mr-IN";

		/// <summary>
        /// sa-IN
        /// </summary>
		public const string SA_IN = "sa-IN";

		/// <summary>
        /// mn-MN
        /// </summary>
		public const string MN_MN = "mn-MN";

		/// <summary>
        /// bo-CN
        /// </summary>
		public const string BO_CN = "bo-CN";

		/// <summary>
        /// cy-GB
        /// </summary>
		public const string CY_GB = "cy-GB";

		/// <summary>
        /// km-KH
        /// </summary>
		public const string KM_KH = "km-KH";

		/// <summary>
        /// lo-LA
        /// </summary>
		public const string LO_LA = "lo-LA";

		/// <summary>
        /// gl-ES
        /// </summary>
		public const string GL_ES = "gl-ES";

		/// <summary>
        /// kok-IN
        /// </summary>
		public const string KOK_IN = "kok-IN";

		/// <summary>
        /// syr-SY
        /// </summary>
		public const string SYR_SY = "syr-SY";

		/// <summary>
        /// si-LK
        /// </summary>
		public const string SI_LK = "si-LK";

		/// <summary>
        /// iu-Cans-CA
        /// </summary>
		public const string IU_CANS_CA = "iu-Cans-CA";

		/// <summary>
        /// am-ET
        /// </summary>
		public const string AM_ET = "am-ET";

		/// <summary>
        /// ne-NP
        /// </summary>
		public const string NE_NP = "ne-NP";

		/// <summary>
        /// fy-NL
        /// </summary>
		public const string FY_NL = "fy-NL";

		/// <summary>
        /// ps-AF
        /// </summary>
		public const string PS_AF = "ps-AF";

		/// <summary>
        /// fil-PH
        /// </summary>
		public const string FIL_PH = "fil-PH";

		/// <summary>
        /// dv-MV
        /// </summary>
		public const string DV_MV = "dv-MV";

		/// <summary>
        /// ha-Latn-NG
        /// </summary>
		public const string HA_LATN_NG = "ha-Latn-NG";

		/// <summary>
        /// yo-NG
        /// </summary>
		public const string YO_NG = "yo-NG";

		/// <summary>
        /// quz-BO
        /// </summary>
		public const string QUZ_BO = "quz-BO";

		/// <summary>
        /// nso-ZA
        /// </summary>
		public const string NSO_ZA = "nso-ZA";

		/// <summary>
        /// ba-RU
        /// </summary>
		public const string BA_RU = "ba-RU";

		/// <summary>
        /// lb-LU
        /// </summary>
		public const string LB_LU = "lb-LU";

		/// <summary>
        /// kl-GL
        /// </summary>
		public const string KL_GL = "kl-GL";

		/// <summary>
        /// ig-NG
        /// </summary>
		public const string IG_NG = "ig-NG";

		/// <summary>
        /// ii-CN
        /// </summary>
		public const string II_CN = "ii-CN";

		/// <summary>
        /// arn-CL
        /// </summary>
		public const string ARN_CL = "arn-CL";

		/// <summary>
        /// moh-CA
        /// </summary>
		public const string MOH_CA = "moh-CA";

		/// <summary>
        /// br-FR
        /// </summary>
		public const string BR_FR = "br-FR";

		/// <summary>
        /// ug-CN
        /// </summary>
		public const string UG_CN = "ug-CN";

		/// <summary>
        /// mi-NZ
        /// </summary>
		public const string MI_NZ = "mi-NZ";

		/// <summary>
        /// oc-FR
        /// </summary>
		public const string OC_FR = "oc-FR";

		/// <summary>
        /// co-FR
        /// </summary>
		public const string CO_FR = "co-FR";

		/// <summary>
        /// gsw-FR
        /// </summary>
		public const string GSW_FR = "gsw-FR";

		/// <summary>
        /// sah-RU
        /// </summary>
		public const string SAH_RU = "sah-RU";

		/// <summary>
        /// qut-GT
        /// </summary>
		public const string QUT_GT = "qut-GT";

		/// <summary>
        /// rw-RW
        /// </summary>
		public const string RW_RW = "rw-RW";

		/// <summary>
        /// wo-SN
        /// </summary>
		public const string WO_SN = "wo-SN";

		/// <summary>
        /// prs-AF
        /// </summary>
		public const string PRS_AF = "prs-AF";

		/// <summary>
        /// gd-GB
        /// </summary>
		public const string GD_GB = "gd-GB";

		/// <summary>
        /// ar-IQ
        /// </summary>
		public const string AR_IQ = "ar-IQ";

		/// <summary>
        /// zh-CN
        /// </summary>
		public const string ZH_CN = "zh-CN";

		/// <summary>
        /// de-CH
        /// </summary>
		public const string DE_CH = "de-CH";

		/// <summary>
        /// en-GB
        /// </summary>
		public const string EN_GB = "en-GB";

		/// <summary>
        /// es-MX
        /// </summary>
		public const string ES_MX = "es-MX";

		/// <summary>
        /// fr-BE
        /// </summary>
		public const string FR_BE = "fr-BE";

		/// <summary>
        /// it-CH
        /// </summary>
		public const string IT_CH = "it-CH";

		/// <summary>
        /// nl-BE
        /// </summary>
		public const string NL_BE = "nl-BE";

		/// <summary>
        /// nn-NO
        /// </summary>
		public const string NN_NO = "nn-NO";

		/// <summary>
        /// pt-PT
        /// </summary>
		public const string PT_PT = "pt-PT";

		/// <summary>
        /// sr-Latn-CS
        /// </summary>
		public const string SR_LATN_CS = "sr-Latn-CS";

		/// <summary>
        /// sv-FI
        /// </summary>
		public const string SV_FI = "sv-FI";

		/// <summary>
        /// az-Cyrl-AZ
        /// </summary>
		public const string AZ_CYRL_AZ = "az-Cyrl-AZ";

		/// <summary>
        /// dsb-DE
        /// </summary>
		public const string DSB_DE = "dsb-DE";

		/// <summary>
        /// se-SE
        /// </summary>
		public const string SE_SE = "se-SE";

		/// <summary>
        /// ga-IE
        /// </summary>
		public const string GA_IE = "ga-IE";

		/// <summary>
        /// ms-BN
        /// </summary>
		public const string MS_BN = "ms-BN";

		/// <summary>
        /// uz-Cyrl-UZ
        /// </summary>
		public const string UZ_CYRL_UZ = "uz-Cyrl-UZ";

		/// <summary>
        /// bn-BD
        /// </summary>
		public const string BN_BD = "bn-BD";

		/// <summary>
        /// mn-Mong-CN
        /// </summary>
		public const string MN_MONG_CN = "mn-Mong-CN";

		/// <summary>
        /// iu-Latn-CA
        /// </summary>
		public const string IU_LATN_CA = "iu-Latn-CA";

		/// <summary>
        /// tzm-Latn-DZ
        /// </summary>
		public const string TZM_LATN_DZ = "tzm-Latn-DZ";

		/// <summary>
        /// quz-EC
        /// </summary>
		public const string QUZ_EC = "quz-EC";

		/// <summary>
        /// ar-EG
        /// </summary>
		public const string AR_EG = "ar-EG";

		/// <summary>
        /// zh-HK
        /// </summary>
		public const string ZH_HK = "zh-HK";

		/// <summary>
        /// de-AT
        /// </summary>
		public const string DE_AT = "de-AT";

		/// <summary>
        /// en-AU
        /// </summary>
		public const string EN_AU = "en-AU";

		/// <summary>
        /// es-ES
        /// </summary>
		public const string ES_ES = "es-ES";

		/// <summary>
        /// fr-CA
        /// </summary>
		public const string FR_CA = "fr-CA";

		/// <summary>
        /// sr-Cyrl-CS
        /// </summary>
		public const string SR_CYRL_CS = "sr-Cyrl-CS";

		/// <summary>
        /// se-FI
        /// </summary>
		public const string SE_FI = "se-FI";

		/// <summary>
        /// quz-PE
        /// </summary>
		public const string QUZ_PE = "quz-PE";

		/// <summary>
        /// ar-LY
        /// </summary>
		public const string AR_LY = "ar-LY";

		/// <summary>
        /// zh-SG
        /// </summary>
		public const string ZH_SG = "zh-SG";

		/// <summary>
        /// de-LU
        /// </summary>
		public const string DE_LU = "de-LU";

		/// <summary>
        /// en-CA
        /// </summary>
		public const string EN_CA = "en-CA";

		/// <summary>
        /// es-GT
        /// </summary>
		public const string ES_GT = "es-GT";

		/// <summary>
        /// fr-CH
        /// </summary>
		public const string FR_CH = "fr-CH";

		/// <summary>
        /// hr-BA
        /// </summary>
		public const string HR_BA = "hr-BA";

		/// <summary>
        /// smj-NO
        /// </summary>
		public const string SMJ_NO = "smj-NO";

		/// <summary>
        /// ar-DZ
        /// </summary>
		public const string AR_DZ = "ar-DZ";

		/// <summary>
        /// zh-MO
        /// </summary>
		public const string ZH_MO = "zh-MO";

		/// <summary>
        /// de-LI
        /// </summary>
		public const string DE_LI = "de-LI";

		/// <summary>
        /// en-NZ
        /// </summary>
		public const string EN_NZ = "en-NZ";

		/// <summary>
        /// es-CR
        /// </summary>
		public const string ES_CR = "es-CR";

		/// <summary>
        /// fr-LU
        /// </summary>
		public const string FR_LU = "fr-LU";

		/// <summary>
        /// bs-Latn-BA
        /// </summary>
		public const string BS_LATN_BA = "bs-Latn-BA";

		/// <summary>
        /// smj-SE
        /// </summary>
		public const string SMJ_SE = "smj-SE";

		/// <summary>
        /// ar-MA
        /// </summary>
		public const string AR_MA = "ar-MA";

		/// <summary>
        /// en-IE
        /// </summary>
		public const string EN_IE = "en-IE";

		/// <summary>
        /// es-PA
        /// </summary>
		public const string ES_PA = "es-PA";

		/// <summary>
        /// fr-MC
        /// </summary>
		public const string FR_MC = "fr-MC";

		/// <summary>
        /// sr-Latn-BA
        /// </summary>
		public const string SR_LATN_BA = "sr-Latn-BA";

		/// <summary>
        /// sma-NO
        /// </summary>
		public const string SMA_NO = "sma-NO";

		/// <summary>
        /// ar-TN
        /// </summary>
		public const string AR_TN = "ar-TN";

		/// <summary>
        /// en-ZA
        /// </summary>
		public const string EN_ZA = "en-ZA";

		/// <summary>
        /// es-DO
        /// </summary>
		public const string ES_DO = "es-DO";

		/// <summary>
        /// sr-Cyrl-BA
        /// </summary>
		public const string SR_CYRL_BA = "sr-Cyrl-BA";

		/// <summary>
        /// sma-SE
        /// </summary>
		public const string SMA_SE = "sma-SE";

		/// <summary>
        /// ar-OM
        /// </summary>
		public const string AR_OM = "ar-OM";

		/// <summary>
        /// en-JM
        /// </summary>
		public const string EN_JM = "en-JM";

		/// <summary>
        /// es-VE
        /// </summary>
		public const string ES_VE = "es-VE";

		/// <summary>
        /// bs-Cyrl-BA
        /// </summary>
		public const string BS_CYRL_BA = "bs-Cyrl-BA";

		/// <summary>
        /// sms-FI
        /// </summary>
		public const string SMS_FI = "sms-FI";

		/// <summary>
        /// ar-YE
        /// </summary>
		public const string AR_YE = "ar-YE";

		/// <summary>
        /// en-029
        /// </summary>
		public const string EN_029 = "en-029";

		/// <summary>
        /// es-CO
        /// </summary>
		public const string ES_CO = "es-CO";

		/// <summary>
        /// sr-Latn-RS
        /// </summary>
		public const string SR_LATN_RS = "sr-Latn-RS";

		/// <summary>
        /// smn-FI
        /// </summary>
		public const string SMN_FI = "smn-FI";

		/// <summary>
        /// ar-SY
        /// </summary>
		public const string AR_SY = "ar-SY";

		/// <summary>
        /// en-BZ
        /// </summary>
		public const string EN_BZ = "en-BZ";

		/// <summary>
        /// es-PE
        /// </summary>
		public const string ES_PE = "es-PE";

		/// <summary>
        /// sr-Cyrl-RS
        /// </summary>
		public const string SR_CYRL_RS = "sr-Cyrl-RS";

		/// <summary>
        /// ar-JO
        /// </summary>
		public const string AR_JO = "ar-JO";

		/// <summary>
        /// en-TT
        /// </summary>
		public const string EN_TT = "en-TT";

		/// <summary>
        /// es-AR
        /// </summary>
		public const string ES_AR = "es-AR";

		/// <summary>
        /// sr-Latn-ME
        /// </summary>
		public const string SR_LATN_ME = "sr-Latn-ME";

		/// <summary>
        /// ar-LB
        /// </summary>
		public const string AR_LB = "ar-LB";

		/// <summary>
        /// en-ZW
        /// </summary>
		public const string EN_ZW = "en-ZW";

		/// <summary>
        /// es-EC
        /// </summary>
		public const string ES_EC = "es-EC";

		/// <summary>
        /// sr-Cyrl-ME
        /// </summary>
		public const string SR_CYRL_ME = "sr-Cyrl-ME";

		/// <summary>
        /// ar-KW
        /// </summary>
		public const string AR_KW = "ar-KW";

		/// <summary>
        /// en-PH
        /// </summary>
		public const string EN_PH = "en-PH";

		/// <summary>
        /// es-CL
        /// </summary>
		public const string ES_CL = "es-CL";

		/// <summary>
        /// ar-AE
        /// </summary>
		public const string AR_AE = "ar-AE";

		/// <summary>
        /// es-UY
        /// </summary>
		public const string ES_UY = "es-UY";

		/// <summary>
        /// ar-BH
        /// </summary>
		public const string AR_BH = "ar-BH";

		/// <summary>
        /// es-PY
        /// </summary>
		public const string ES_PY = "es-PY";

		/// <summary>
        /// ar-QA
        /// </summary>
		public const string AR_QA = "ar-QA";

		/// <summary>
        /// en-IN
        /// </summary>
		public const string EN_IN = "en-IN";

		/// <summary>
        /// es-BO
        /// </summary>
		public const string ES_BO = "es-BO";

		/// <summary>
        /// en-MY
        /// </summary>
		public const string EN_MY = "en-MY";

		/// <summary>
        /// es-SV
        /// </summary>
		public const string ES_SV = "es-SV";

		/// <summary>
        /// en-SG
        /// </summary>
		public const string EN_SG = "en-SG";

		/// <summary>
        /// es-HN
        /// </summary>
		public const string ES_HN = "es-HN";

		/// <summary>
        /// es-NI
        /// </summary>
		public const string ES_NI = "es-NI";

		/// <summary>
        /// es-PR
        /// </summary>
		public const string ES_PR = "es-PR";

		/// <summary>
        /// es-US
        /// </summary>
		public const string ES_US = "es-US";

    }
}
{% endcodeblock %}

<br/>


有了該靜態類別我們就可以將這部份的 Hard code 拿掉了。  

{% codeblock lang:c# %}
...
var currentThread = Thread.CurrentThread;
currentThread.CurrentCulture = CultureInfo.GetCultureInfo(CultureNames.ZH_TW);

Console.WriteLine(currentThread.CurrentCulture.Name);
...
{% endcodeblock %}

<br/>


{% img /images/posts/T4CultureNames/2.png %}
