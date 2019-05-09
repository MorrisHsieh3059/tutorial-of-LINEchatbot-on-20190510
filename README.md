**金融科技-文字探勘與機器學習 (Fintech-Text Mining and Machine Learning)**

**W12 LINEBOT 教學**

**講員：龔泓愷、何承諭、謝君模**

檔案介紹
1. Folder: LINESimulator
           <ul>
           <li>reference: https://github.com/kenakamu/LINESimulator</li>
           <li>這是本機模擬用的套件，裝在哪裡都行，但建議放在專案資料夾，避免找不到</li>
           </ul>
2. Files:
      <ul>
       <li>I.  運行用的主程式
         <ul>
         <li> a. basic.py:　 介紹基本的架構(PS: 不用跑這個檔案，只是說明用)</li>
         <li> b. echo.py:    簡易的複誦機器人</li>
         <li> c. example.py: 用到兩種event(message & postback)的簡易示範</li>
         </ul>
        </li>
       <li>II. 裝一些零件用的(記得import到主程式)
          <ul>
          <li>d. carousel.py</li>
          </ul>
       </li>   
     </ul>
3. Operation:
      開兩個cmd，先後順序無關，但都要開XD
      <ul>
      <li>i) 專門跑flask ── 軍隊的後勤</li>
          <ul>
          <li>Commands:</li>
            <li>  cd <Foldername></li>
            <li>  pipenv shell</li>
            <li>  set FLASK_APP=<filename>   # 如果之後都沒有換主程式，不用重複打</li>
            <li>  set FLASK_ENV=development  # 第一次使用前輸入即可</li>
            <li>  flask run</li>
         </ul>
      <li>ii) 跑LINESimulator用的 ── 軍隊的前鋒</li>
         <ul>   
          <li>Commands:</li>
               <li>  cd LINESimulator</li>
               <li>  npm start</li>
         </ul>
      </ul>

4. Others:
     <ul>  
     <li>  更多內容請見LINE Messaging API官方文件，裡面有詳細的說明，還有各種類別的使用方法及限制</li>
       <li>  Doc: https://developers.line.biz/en/reference/messaging-api/</li>
</ul>
