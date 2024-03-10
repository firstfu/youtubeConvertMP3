# YouTube轉MP3下載器

這是一個簡單的Web應用，讓用戶能夠將YouTube視頻轉換成MP3格式並下載到本地。

## 目錄

- [關於](#about)
- [開始使用](#getting_started)
- [使用說明](#usage)
- [貢獻](../CONTRIBUTING.md)

## 關於 <a name="about"></a>

本項目的目的是提供一個簡便的工具，讓用戶能夠從YouTube視頻中提取音頻，並將其保存為MP3文件。這對於希望在不同設備上聆聽YouTube音樂、播客或任何其他音頻內容的用戶來說非常有用。

## 開始使用 <a name="getting_started"></a>

以下指南將幫助您在本地機器上設置和運行項目，用於開發和測試目的。

### 先決條件

在開始之前，您需要安裝以下軟件：

- Python 3.6或更高版本
- pip (Python包管理器)

### 安裝

執行以下命令安裝所需的庫：

```bash
pip install streamlit pytube moviepy
```

運行應用
克隆此倉庫，然後運行Streamlit應用：

這將在默認瀏覽器中打開應用界面。

```bash
git clone https://yourproject.github.com
cd yourproject
streamlit run your_app.py
```

## 使用說明 <a name="usage"></a>

在應用界面，點擊“新增”按鈕以添加文本區域。
將YouTube視頻的URL粘貼到文本區域中。
點擊相應的“轉換”按鈕開始轉換過程。轉換完成後，系統將顯示一個“下載MP3”按鈕。
點擊“下載MP3”按鈕，即可將轉換後的MP3文件保存到您的設備。
