---
title: "[C#][WPF]DependencyProperty"
slug: "[CSharp][WPF]DependencyProperty"
date: "2011-12-08 12:45:18"
description: "[C#][WPF]DependencyProperty"
tags: [WPF,CSharp]
---

前好一陣子有用到WPF的相依屬性，這邊隨手簡單紀錄一下怎樣新增WPF元件的相依屬性。

	新增相依屬性時首先必須加入個靜態的攔位，欄位型態為DependencyProperty。

#region Var
public static readonly DependencyProperty _status;
#endregion

	接著建立對應的屬性，屬性內部的get區塊用GetValue函式實作，帶入剛建立的靜態攔位，並將回傳值轉為我們預期的型態就可以了。而set區塊則用SetValue函式實作，帶入剛建立的靜態攔位與新的屬性值。

        #region Property
        public int Status
        {
            get
            {
                return (int)GetValue(_status);
            }
            set
            {
                SetValue(_status, value);
                ChangeStatus(value);
            }
        }
        #endregion

	再來必須在靜態建構子中跟系統註冊相依屬性，註冊時帶入相依屬性的名稱、相依屬性的型態、相依屬性擁有者的型態、相依屬性的預設值，若有需要也可以帶入回呼函式,當相依屬性變動時觸發。

        #region Constructor
        static UserControl1()
        {
            _status = DependencyProperty.Register("Status", typeof(int), typeof(UserControl1), new UIPropertyMetadata(default(int), new PropertyChangedCallback(OnStatusChanged)));
        }
        #endregion

	若在註冊相依屬性時有帶入相依屬性的回呼函式，回呼函式可以像下面這樣撰寫，將傳入的相依物件轉型為相依屬性擁有者的型態後設定其對應的屬性值，新的屬性值可自e.NewValue取得。

        #region Event Process
        private static void OnStatusChanged(DependencyObject o, DependencyPropertyChangedEventArgs e)
        { 
            if (o == null)
                return;
            var statusIcon = o as UserControl1;
            statusIcon.Status = (int)e.NewValue;
        }
        #endregion

	用Blend使用時我們就可以看到屬性中多了我們新增的相依屬性。