---
title: "FlickrNet開發系列- 使用FlickrNet上傳照片至Flickr"
date: "2013-11-06 12:00:00"
description: "FlickrNet開發系列- 使用FlickrNet上傳照片至Flickr"
---

透過FlickrNet上傳照片至Flickr十分簡單，我們可以透過FlickrNet.UploadPicture與FlickrNet.UploadPictureAsync這兩個方法來達成需求，支援同步與非同步上傳。圖片上傳時也可以透過OnUploadProgress事件取得上傳的進度。

上傳事件的參數可以取得像是傳送了多少Byte、傳送了幾趴、總共傳了多少Byte、與是否上傳完成...等

這邊是個簡單的實作範例：
              var dialog = new OpenFileDialog() 
            {
                Filter = "JPEG File|*.jpg"
            };

            if (dialog.ShowDialog() != System.Windows.Forms.DialogResult.OK)
                return;

            var form = new Form();
            var progress = new ProgressBar() 
            {
                Maximum = 100,
                Dock = DockStyle.Fill
            };

            form.Controls.Add(progress);
            form.Size = new System.Drawing.Size(200, 100);

            m_Flickr.OnUploadProgress += (s, ex) =>
                {
                    progress.Value = ex.ProcessPercentage;
                };

            form.Show();
            m_Flickr.UploadPicture(dialog.FileName,
                "Photo1", "Just test upload");

運行起來後會跳出開啟對話框，選取要上傳的圖片檔案後按下確定按鈕，上傳進度對話框就會出現，進度更新會即時顯示，就像下圖一樣。

 上傳完畢圖片就會在Flickr上，下圖中的無尾熊與鬱金香就是筆者測試實上傳的圖片。