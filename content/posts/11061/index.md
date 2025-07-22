---
title: "[C#]Effective C# 條款七： 將值類型盡可能實現為具有常量性與原子性的類型"
slug: "[CSharp]Effective C# 條款七： 將值類型盡可能實現為具有常量性與原子性的類型"
date: "2009-10-15 09:00:47"
description: "[C#]Effective C# 條款七： 將值類型盡可能實現為具有常量性與原子性的類型"
tags: [CSharp]
---

## 
	Introduction

	當程式決定使用值類型來開發時，請優先考慮將值類型實現為具備常量性與原子性的類型。因為具有常量性的類型可讓程式較為容易編寫與維護，也較容易構建更複雜的結構。

## 
	Advantage

	常量性值類型具備以下優點：

		常量性類型由於建構後值就固定不變，因此只需在建構子做參數的檢查，可省略許多必要的錯誤檢查。
	
		常量性類型其值不能變動，不同執行緒看到的值都一樣，是執行緒安全的。
	
		常量性類型可安全的曝露給外界，因其調用者無法變更值。
	
		常量性類型能確保GetHashCode()方法返回一個常量，在雜湊集合中表現良好。

## 
	實現具有常量性與原子性的值類型

	假設今天我們有段程式：

	public struct Address
    {
        private String _line;
        private String _city;
        private String _state;
        private int _zipCode;

        public string Line
        {
            get { return _line; }
            set { _line = value; }
        }
        public string City
        {
            get { return _city; }
            set { _city = value; }
        }
        public string State
        {
            get { return _state; }
            set {
                ValidateState(value);
                _state = value; 
            }
        }
        public int ZipCode
        {
            get { return _zipCode; }
            set {
                ValidateZip(value);
                _zipCode = value; 
            }
        }
        ...
    }

	並有如下的使用代碼：

	Address address = new Address();
    ...
    address.City = "Anytown";
    address.State = "IL";
    address.ZipCode = 61111;
    ...
    //Modify
    address.City = "Ann Arbor";
    address.ZipCode = 48103;
    address.State = "MI";

	我們應該可以發現address物件在做修改內容時，會有一段時間其值是不完整且無意義的暫態。這樣的程式在多執行緒的情況下，會造成程式運行結果不正確。而在單一執行緒的情況下，我們在做錯誤檢查上也會增加許多的困難度。若把程式改為具有常量性與原子性的類型，則可以避免這樣的問題。因此我們可以修改成：

	public struct Address
    {
        private readonly String _line;
        private readonly String _city;
        private readonly String _state;
        private readonly int _zipCode;

        public string Line
        {
            get { return _line; }
        }
        public string City
        {
            get { return _city; }
        }
        public string State
        {
            get { return _state; }
        }
        public int ZipCode
        {
            get { return _zipCode; }
        }

        public Address(string line,string city,string state,int zipCode)
        {
            _line = line;
            _city = city;
            _state = state;
            _zipCode = zipCode;
            ValidateState(state);
            ValidateZip(zipCode);
        }
    }

	透過readonly關鍵字的使用，可讓成員變量具有常量性。而建構子的填值動作，則能為類型帶來原子性。這樣的程式不會有像上面所述的問題。修改後程式的使用將會變成如下這般：

	Address address = new Address("111 S. Main","Anytown","IL",61111);
    ...
    //Modify
    address = new Address(address.Line,"Ann Arbor","MI",48103);

## 
	防禦常量性類型隱藏性漏洞

	當實現了具有常量性與原子性類型後，我們還必須特別留意是否有隱藏性漏洞存在。這邊的隱藏性漏洞指的是該值類型曝露在外的參考型別。若值類型內含參考類型的公有成員，或是具有可帶入參考類型參數的方法，則此值類型就有可能存有隱藏性的漏洞。透過這個隱藏性的漏洞，外界可利用曝露在外或是帶入的參考類型來改變其內部成員的值。

	舉個例子來說，像下面這段程式就內含隱藏性的漏洞：

	public struct PhoneList
    {
        private readonly Phone[] _phones;

        public PhoneList(Phone[] ph)
        {
            _phones = ph;
        }
        ...
    }

	這段程式在使用時，我們需在PhoneList建構子傳入Phone的陣列，PhoneList建構子會把帶入的值當為內部的資料。使用上就像下面這樣：

	Phone[] phones = new Phone[10];
    PhoneList ps = new PhoneList(phones);
    ...
    //Modify
    phones[5] = Phone.GeneratePhoneNumber();

	由於陣列是屬於參考類型，因此像上面這樣把phones帶入建構後，再對phones的元素做修改。則會連帶的影響到PhoneList內部的資料。若要解決這樣的問題，我們可以做如下修改(這邊的Phone為值類型)：

	public struct PhoneList
    {
        private readonly Phone[] _phones;

        public PhoneList(Phone[] ph)
        {
            _phones = new Phone[ph.Length];
            ph.CopyTo(_phones,0);
        }
        ...
    }

## 
	初始化常量性類型

	初始化常量性類型通常有三種方法：

		定義合適的建構子
	
		使用工廠方法
	
		創建可變的輔助類

	選擇哪一種方法主要是依據類型的複雜度。

	定義合適的建構子

	使用建構子來創建常量性類型是最簡單的一種方法，只需在建構子中設定適當的參數，透過這些建構子參數把為內部變數填值即可。

	使用工廠方法

	使用工廠方法來創建常量性類型，對於一些常用的值較為方便。像是Color.FromKnowColor()與Color.FromName()就是ㄧ例。

	創建可變的輔助類

	這是最麻煩且操作步驟最多的方法。我們可以透過對輔助類多次的叫用，來建立我們所需要的物件。像.NET中的StringBuilder就是String的輔助類。