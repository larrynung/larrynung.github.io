---
title: "T4 template - CultureNames.tt"
date: "2016-03-08 05:31:00"
description: "T4 template - CultureNames.tt"
tags: [T4, CSharp]
---

.NET 在操作 Culture 時，免不了要帶入 CultureInfo 的 Name，多半是用 Hard code 的形式帶入，像是下面這樣：  

```c#
...
var currentThread = Thread.CurrentThread;
currentThread.CurrentCulture = CultureInfo.GetCultureInfo("zh-tw");
...
```

![1.png](/images/posts/T4CultureNames/1.png)

這邊筆者做了個 T4 Template，期望能解決這樣的問題。  

```c#

namespace System.Globalization
{
    public static class CultureNames
    {

		/// 
        /// 
        /// 
		public const string  = "";

    }
}
```

該  T4 Template 運行後會將所有可用的 Culture Name 彙整成一個靜態類別。  

```c#
namespace System.Globalization
{
    public static class CultureNames
    {
		/// 
        /// ar-SA
        /// 
		public const string AR_SA = "ar-SA";

		/// 
        /// bg-BG
        /// 
		public const string BG_BG = "bg-BG";

		/// 
        /// ca-ES
        /// 
		public const string CA_ES = "ca-ES";

		/// 
        /// zh-TW
        /// 
		public const string ZH_TW = "zh-TW";

		/// 
        /// cs-CZ
        /// 
		public const string CS_CZ = "cs-CZ";

		/// 
        /// da-DK
        /// 
		public const string DA_DK = "da-DK";

		/// 
        /// de-DE
        /// 
		public const string DE_DE = "de-DE";

		/// 
        /// el-GR
        /// 
		public const string EL_GR = "el-GR";

		/// 
        /// en-US
        /// 
		public const string EN_US = "en-US";

		/// 
        /// fi-FI
        /// 
		public const string FI_FI = "fi-FI";

		/// 
        /// fr-FR
        /// 
		public const string FR_FR = "fr-FR";

		/// 
        /// he-IL
        /// 
		public const string HE_IL = "he-IL";

		/// 
        /// hu-HU
        /// 
		public const string HU_HU = "hu-HU";

		/// 
        /// is-IS
        /// 
		public const string IS_IS = "is-IS";

		/// 
        /// it-IT
        /// 
		public const string IT_IT = "it-IT";

		/// 
        /// ja-JP
        /// 
		public const string JA_JP = "ja-JP";

		/// 
        /// ko-KR
        /// 
		public const string KO_KR = "ko-KR";

		/// 
        /// nl-NL
        /// 
		public const string NL_NL = "nl-NL";

		/// 
        /// nb-NO
        /// 
		public const string NB_NO = "nb-NO";

		/// 
        /// pl-PL
        /// 
		public const string PL_PL = "pl-PL";

		/// 
        /// pt-BR
        /// 
		public const string PT_BR = "pt-BR";

		/// 
        /// rm-CH
        /// 
		public const string RM_CH = "rm-CH";

		/// 
        /// ro-RO
        /// 
		public const string RO_RO = "ro-RO";

		/// 
        /// ru-RU
        /// 
		public const string RU_RU = "ru-RU";

		/// 
        /// hr-HR
        /// 
		public const string HR_HR = "hr-HR";

		/// 
        /// sk-SK
        /// 
		public const string SK_SK = "sk-SK";

		/// 
        /// sq-AL
        /// 
		public const string SQ_AL = "sq-AL";

		/// 
        /// sv-SE
        /// 
		public const string SV_SE = "sv-SE";

		/// 
        /// th-TH
        /// 
		public const string TH_TH = "th-TH";

		/// 
        /// tr-TR
        /// 
		public const string TR_TR = "tr-TR";

		/// 
        /// ur-PK
        /// 
		public const string UR_PK = "ur-PK";

		/// 
        /// id-ID
        /// 
		public const string ID_ID = "id-ID";

		/// 
        /// uk-UA
        /// 
		public const string UK_UA = "uk-UA";

		/// 
        /// be-BY
        /// 
		public const string BE_BY = "be-BY";

		/// 
        /// sl-SI
        /// 
		public const string SL_SI = "sl-SI";

		/// 
        /// et-EE
        /// 
		public const string ET_EE = "et-EE";

		/// 
        /// lv-LV
        /// 
		public const string LV_LV = "lv-LV";

		/// 
        /// lt-LT
        /// 
		public const string LT_LT = "lt-LT";

		/// 
        /// tg-Cyrl-TJ
        /// 
		public const string TG_CYRL_TJ = "tg-Cyrl-TJ";

		/// 
        /// fa-IR
        /// 
		public const string FA_IR = "fa-IR";

		/// 
        /// vi-VN
        /// 
		public const string VI_VN = "vi-VN";

		/// 
        /// hy-AM
        /// 
		public const string HY_AM = "hy-AM";

		/// 
        /// az-Latn-AZ
        /// 
		public const string AZ_LATN_AZ = "az-Latn-AZ";

		/// 
        /// eu-ES
        /// 
		public const string EU_ES = "eu-ES";

		/// 
        /// hsb-DE
        /// 
		public const string HSB_DE = "hsb-DE";

		/// 
        /// mk-MK
        /// 
		public const string MK_MK = "mk-MK";

		/// 
        /// tn-ZA
        /// 
		public const string TN_ZA = "tn-ZA";

		/// 
        /// xh-ZA
        /// 
		public const string XH_ZA = "xh-ZA";

		/// 
        /// zu-ZA
        /// 
		public const string ZU_ZA = "zu-ZA";

		/// 
        /// af-ZA
        /// 
		public const string AF_ZA = "af-ZA";

		/// 
        /// ka-GE
        /// 
		public const string KA_GE = "ka-GE";

		/// 
        /// fo-FO
        /// 
		public const string FO_FO = "fo-FO";

		/// 
        /// hi-IN
        /// 
		public const string HI_IN = "hi-IN";

		/// 
        /// mt-MT
        /// 
		public const string MT_MT = "mt-MT";

		/// 
        /// se-NO
        /// 
		public const string SE_NO = "se-NO";

		/// 
        /// ms-MY
        /// 
		public const string MS_MY = "ms-MY";

		/// 
        /// kk-KZ
        /// 
		public const string KK_KZ = "kk-KZ";

		/// 
        /// ky-KG
        /// 
		public const string KY_KG = "ky-KG";

		/// 
        /// sw-KE
        /// 
		public const string SW_KE = "sw-KE";

		/// 
        /// tk-TM
        /// 
		public const string TK_TM = "tk-TM";

		/// 
        /// uz-Latn-UZ
        /// 
		public const string UZ_LATN_UZ = "uz-Latn-UZ";

		/// 
        /// tt-RU
        /// 
		public const string TT_RU = "tt-RU";

		/// 
        /// bn-IN
        /// 
		public const string BN_IN = "bn-IN";

		/// 
        /// pa-IN
        /// 
		public const string PA_IN = "pa-IN";

		/// 
        /// gu-IN
        /// 
		public const string GU_IN = "gu-IN";

		/// 
        /// or-IN
        /// 
		public const string OR_IN = "or-IN";

		/// 
        /// ta-IN
        /// 
		public const string TA_IN = "ta-IN";

		/// 
        /// te-IN
        /// 
		public const string TE_IN = "te-IN";

		/// 
        /// kn-IN
        /// 
		public const string KN_IN = "kn-IN";

		/// 
        /// ml-IN
        /// 
		public const string ML_IN = "ml-IN";

		/// 
        /// as-IN
        /// 
		public const string AS_IN = "as-IN";

		/// 
        /// mr-IN
        /// 
		public const string MR_IN = "mr-IN";

		/// 
        /// sa-IN
        /// 
		public const string SA_IN = "sa-IN";

		/// 
        /// mn-MN
        /// 
		public const string MN_MN = "mn-MN";

		/// 
        /// bo-CN
        /// 
		public const string BO_CN = "bo-CN";

		/// 
        /// cy-GB
        /// 
		public const string CY_GB = "cy-GB";

		/// 
        /// km-KH
        /// 
		public const string KM_KH = "km-KH";

		/// 
        /// lo-LA
        /// 
		public const string LO_LA = "lo-LA";

		/// 
        /// gl-ES
        /// 
		public const string GL_ES = "gl-ES";

		/// 
        /// kok-IN
        /// 
		public const string KOK_IN = "kok-IN";

		/// 
        /// syr-SY
        /// 
		public const string SYR_SY = "syr-SY";

		/// 
        /// si-LK
        /// 
		public const string SI_LK = "si-LK";

		/// 
        /// iu-Cans-CA
        /// 
		public const string IU_CANS_CA = "iu-Cans-CA";

		/// 
        /// am-ET
        /// 
		public const string AM_ET = "am-ET";

		/// 
        /// ne-NP
        /// 
		public const string NE_NP = "ne-NP";

		/// 
        /// fy-NL
        /// 
		public const string FY_NL = "fy-NL";

		/// 
        /// ps-AF
        /// 
		public const string PS_AF = "ps-AF";

		/// 
        /// fil-PH
        /// 
		public const string FIL_PH = "fil-PH";

		/// 
        /// dv-MV
        /// 
		public const string DV_MV = "dv-MV";

		/// 
        /// ha-Latn-NG
        /// 
		public const string HA_LATN_NG = "ha-Latn-NG";

		/// 
        /// yo-NG
        /// 
		public const string YO_NG = "yo-NG";

		/// 
        /// quz-BO
        /// 
		public const string QUZ_BO = "quz-BO";

		/// 
        /// nso-ZA
        /// 
		public const string NSO_ZA = "nso-ZA";

		/// 
        /// ba-RU
        /// 
		public const string BA_RU = "ba-RU";

		/// 
        /// lb-LU
        /// 
		public const string LB_LU = "lb-LU";

		/// 
        /// kl-GL
        /// 
		public const string KL_GL = "kl-GL";

		/// 
        /// ig-NG
        /// 
		public const string IG_NG = "ig-NG";

		/// 
        /// ii-CN
        /// 
		public const string II_CN = "ii-CN";

		/// 
        /// arn-CL
        /// 
		public const string ARN_CL = "arn-CL";

		/// 
        /// moh-CA
        /// 
		public const string MOH_CA = "moh-CA";

		/// 
        /// br-FR
        /// 
		public const string BR_FR = "br-FR";

		/// 
        /// ug-CN
        /// 
		public const string UG_CN = "ug-CN";

		/// 
        /// mi-NZ
        /// 
		public const string MI_NZ = "mi-NZ";

		/// 
        /// oc-FR
        /// 
		public const string OC_FR = "oc-FR";

		/// 
        /// co-FR
        /// 
		public const string CO_FR = "co-FR";

		/// 
        /// gsw-FR
        /// 
		public const string GSW_FR = "gsw-FR";

		/// 
        /// sah-RU
        /// 
		public const string SAH_RU = "sah-RU";

		/// 
        /// qut-GT
        /// 
		public const string QUT_GT = "qut-GT";

		/// 
        /// rw-RW
        /// 
		public const string RW_RW = "rw-RW";

		/// 
        /// wo-SN
        /// 
		public const string WO_SN = "wo-SN";

		/// 
        /// prs-AF
        /// 
		public const string PRS_AF = "prs-AF";

		/// 
        /// gd-GB
        /// 
		public const string GD_GB = "gd-GB";

		/// 
        /// ar-IQ
        /// 
		public const string AR_IQ = "ar-IQ";

		/// 
        /// zh-CN
        /// 
		public const string ZH_CN = "zh-CN";

		/// 
        /// de-CH
        /// 
		public const string DE_CH = "de-CH";

		/// 
        /// en-GB
        /// 
		public const string EN_GB = "en-GB";

		/// 
        /// es-MX
        /// 
		public const string ES_MX = "es-MX";

		/// 
        /// fr-BE
        /// 
		public const string FR_BE = "fr-BE";

		/// 
        /// it-CH
        /// 
		public const string IT_CH = "it-CH";

		/// 
        /// nl-BE
        /// 
		public const string NL_BE = "nl-BE";

		/// 
        /// nn-NO
        /// 
		public const string NN_NO = "nn-NO";

		/// 
        /// pt-PT
        /// 
		public const string PT_PT = "pt-PT";

		/// 
        /// sr-Latn-CS
        /// 
		public const string SR_LATN_CS = "sr-Latn-CS";

		/// 
        /// sv-FI
        /// 
		public const string SV_FI = "sv-FI";

		/// 
        /// az-Cyrl-AZ
        /// 
		public const string AZ_CYRL_AZ = "az-Cyrl-AZ";

		/// 
        /// dsb-DE
        /// 
		public const string DSB_DE = "dsb-DE";

		/// 
        /// se-SE
        /// 
		public const string SE_SE = "se-SE";

		/// 
        /// ga-IE
        /// 
		public const string GA_IE = "ga-IE";

		/// 
        /// ms-BN
        /// 
		public const string MS_BN = "ms-BN";

		/// 
        /// uz-Cyrl-UZ
        /// 
		public const string UZ_CYRL_UZ = "uz-Cyrl-UZ";

		/// 
        /// bn-BD
        /// 
		public const string BN_BD = "bn-BD";

		/// 
        /// mn-Mong-CN
        /// 
		public const string MN_MONG_CN = "mn-Mong-CN";

		/// 
        /// iu-Latn-CA
        /// 
		public const string IU_LATN_CA = "iu-Latn-CA";

		/// 
        /// tzm-Latn-DZ
        /// 
		public const string TZM_LATN_DZ = "tzm-Latn-DZ";

		/// 
        /// quz-EC
        /// 
		public const string QUZ_EC = "quz-EC";

		/// 
        /// ar-EG
        /// 
		public const string AR_EG = "ar-EG";

		/// 
        /// zh-HK
        /// 
		public const string ZH_HK = "zh-HK";

		/// 
        /// de-AT
        /// 
		public const string DE_AT = "de-AT";

		/// 
        /// en-AU
        /// 
		public const string EN_AU = "en-AU";

		/// 
        /// es-ES
        /// 
		public const string ES_ES = "es-ES";

		/// 
        /// fr-CA
        /// 
		public const string FR_CA = "fr-CA";

		/// 
        /// sr-Cyrl-CS
        /// 
		public const string SR_CYRL_CS = "sr-Cyrl-CS";

		/// 
        /// se-FI
        /// 
		public const string SE_FI = "se-FI";

		/// 
        /// quz-PE
        /// 
		public const string QUZ_PE = "quz-PE";

		/// 
        /// ar-LY
        /// 
		public const string AR_LY = "ar-LY";

		/// 
        /// zh-SG
        /// 
		public const string ZH_SG = "zh-SG";

		/// 
        /// de-LU
        /// 
		public const string DE_LU = "de-LU";

		/// 
        /// en-CA
        /// 
		public const string EN_CA = "en-CA";

		/// 
        /// es-GT
        /// 
		public const string ES_GT = "es-GT";

		/// 
        /// fr-CH
        /// 
		public const string FR_CH = "fr-CH";

		/// 
        /// hr-BA
        /// 
		public const string HR_BA = "hr-BA";

		/// 
        /// smj-NO
        /// 
		public const string SMJ_NO = "smj-NO";

		/// 
        /// ar-DZ
        /// 
		public const string AR_DZ = "ar-DZ";

		/// 
        /// zh-MO
        /// 
		public const string ZH_MO = "zh-MO";

		/// 
        /// de-LI
        /// 
		public const string DE_LI = "de-LI";

		/// 
        /// en-NZ
        /// 
		public const string EN_NZ = "en-NZ";

		/// 
        /// es-CR
        /// 
		public const string ES_CR = "es-CR";

		/// 
        /// fr-LU
        /// 
		public const string FR_LU = "fr-LU";

		/// 
        /// bs-Latn-BA
        /// 
		public const string BS_LATN_BA = "bs-Latn-BA";

		/// 
        /// smj-SE
        /// 
		public const string SMJ_SE = "smj-SE";

		/// 
        /// ar-MA
        /// 
		public const string AR_MA = "ar-MA";

		/// 
        /// en-IE
        /// 
		public const string EN_IE = "en-IE";

		/// 
        /// es-PA
        /// 
		public const string ES_PA = "es-PA";

		/// 
        /// fr-MC
        /// 
		public const string FR_MC = "fr-MC";

		/// 
        /// sr-Latn-BA
        /// 
		public const string SR_LATN_BA = "sr-Latn-BA";

		/// 
        /// sma-NO
        /// 
		public const string SMA_NO = "sma-NO";

		/// 
        /// ar-TN
        /// 
		public const string AR_TN = "ar-TN";

		/// 
        /// en-ZA
        /// 
		public const string EN_ZA = "en-ZA";

		/// 
        /// es-DO
        /// 
		public const string ES_DO = "es-DO";

		/// 
        /// sr-Cyrl-BA
        /// 
		public const string SR_CYRL_BA = "sr-Cyrl-BA";

		/// 
        /// sma-SE
        /// 
		public const string SMA_SE = "sma-SE";

		/// 
        /// ar-OM
        /// 
		public const string AR_OM = "ar-OM";

		/// 
        /// en-JM
        /// 
		public const string EN_JM = "en-JM";

		/// 
        /// es-VE
        /// 
		public const string ES_VE = "es-VE";

		/// 
        /// bs-Cyrl-BA
        /// 
		public const string BS_CYRL_BA = "bs-Cyrl-BA";

		/// 
        /// sms-FI
        /// 
		public const string SMS_FI = "sms-FI";

		/// 
        /// ar-YE
        /// 
		public const string AR_YE = "ar-YE";

		/// 
        /// en-029
        /// 
		public const string EN_029 = "en-029";

		/// 
        /// es-CO
        /// 
		public const string ES_CO = "es-CO";

		/// 
        /// sr-Latn-RS
        /// 
		public const string SR_LATN_RS = "sr-Latn-RS";

		/// 
        /// smn-FI
        /// 
		public const string SMN_FI = "smn-FI";

		/// 
        /// ar-SY
        /// 
		public const string AR_SY = "ar-SY";

		/// 
        /// en-BZ
        /// 
		public const string EN_BZ = "en-BZ";

		/// 
        /// es-PE
        /// 
		public const string ES_PE = "es-PE";

		/// 
        /// sr-Cyrl-RS
        /// 
		public const string SR_CYRL_RS = "sr-Cyrl-RS";

		/// 
        /// ar-JO
        /// 
		public const string AR_JO = "ar-JO";

		/// 
        /// en-TT
        /// 
		public const string EN_TT = "en-TT";

		/// 
        /// es-AR
        /// 
		public const string ES_AR = "es-AR";

		/// 
        /// sr-Latn-ME
        /// 
		public const string SR_LATN_ME = "sr-Latn-ME";

		/// 
        /// ar-LB
        /// 
		public const string AR_LB = "ar-LB";

		/// 
        /// en-ZW
        /// 
		public const string EN_ZW = "en-ZW";

		/// 
        /// es-EC
        /// 
		public const string ES_EC = "es-EC";

		/// 
        /// sr-Cyrl-ME
        /// 
		public const string SR_CYRL_ME = "sr-Cyrl-ME";

		/// 
        /// ar-KW
        /// 
		public const string AR_KW = "ar-KW";

		/// 
        /// en-PH
        /// 
		public const string EN_PH = "en-PH";

		/// 
        /// es-CL
        /// 
		public const string ES_CL = "es-CL";

		/// 
        /// ar-AE
        /// 
		public const string AR_AE = "ar-AE";

		/// 
        /// es-UY
        /// 
		public const string ES_UY = "es-UY";

		/// 
        /// ar-BH
        /// 
		public const string AR_BH = "ar-BH";

		/// 
        /// es-PY
        /// 
		public const string ES_PY = "es-PY";

		/// 
        /// ar-QA
        /// 
		public const string AR_QA = "ar-QA";

		/// 
        /// en-IN
        /// 
		public const string EN_IN = "en-IN";

		/// 
        /// es-BO
        /// 
		public const string ES_BO = "es-BO";

		/// 
        /// en-MY
        /// 
		public const string EN_MY = "en-MY";

		/// 
        /// es-SV
        /// 
		public const string ES_SV = "es-SV";

		/// 
        /// en-SG
        /// 
		public const string EN_SG = "en-SG";

		/// 
        /// es-HN
        /// 
		public const string ES_HN = "es-HN";

		/// 
        /// es-NI
        /// 
		public const string ES_NI = "es-NI";

		/// 
        /// es-PR
        /// 
		public const string ES_PR = "es-PR";

		/// 
        /// es-US
        /// 
		public const string ES_US = "es-US";

    }
}
```

有了該靜態類別我們就可以將這部份的 Hard code 拿掉了。  

```c#
...
var currentThread = Thread.CurrentThread;
currentThread.CurrentCulture = CultureInfo.GetCultureInfo(CultureNames.ZH_TW);

Console.WriteLine(currentThread.CurrentCulture.Name);
...
```

![2.png](/images/posts/T4CultureNames/2.png)