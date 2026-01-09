.. role:: red
.. role:: blue
.. role:: black
.. _Google Sheet Sample: https://docs.google.com/spreadsheets/d/1QfIX_cQ8UFNPeKUtLeTG_sPMpsk_8B4g/edit?gid=2053356627#gid=2053356627
.. _Google Spreadsheet Sample: https://docs.google.com/spreadsheets/d/153mE5kvo7PzYukcsVt_IsjvDFq4JxnPzSnSqfuEnY_4/edit?gid=0#gid=0

Support System
==============

Google Sheet
-------------

Định nghĩa
*************

Trang quản lý số lần thăm khám của 1 clinic. Khách hàng cung cấp.

Trang thông tin này được cập nhật thông tin liên tục. Ngày 1-10 hàng tháng sẽ update toàn bộ thông tin của tháng trước đó.

Example: `Google Sheet Sample`_


.. list-table:: **Main Flow**
   :header-rows: 1
   :widths: 30 80 50 30

   * - Đề mục
     - Dịch
     - Ý nghĩa
     - Giá trị
   * - ``居宅・施設名``
     - Tên cơ sở/nhà ở
     - Chứa thông tin nhà ở, cơ sở
     - Text
   * - ``患者番号``
     - Mã bệnh nhân
     - Mỗi bệnh nhân có mã riêng biệt
     - ID bệnh nhân được sinh tự động trên hệ thống
   * - ``カナ氏名``
     - Tên bệnh nhân
     - Tên người bệnh đến cơ sở thăm khám
     - Text
   * - ``カルテ記載完了``
     - Hoàn thành viết hồ sơ điện tử
     - Trạng thái bệnh nhân đã được hoàn thành viết hồ sơ điện tử
     - X: hoàn thành

       O: chưa hoàn thành
   * - ``病名チェック完了``
     - Hoàn thành kiểm tra tên bệnh
     - Trạng thái bác sĩ đã hoàn thành kiểm tra tên bệnh
     - X: hoàn thành

       O: chưa hoàn thành
   * - ``モバカル会計完了``
     - Hoàn thành kế toán Movocal
     - Trạng thái bệnh nhân đã hoàn thành qua kế toán Movocal
     - X: hoàn thành

       O: chưa hoàn thành
   * - ``ORCA会計完了``
     - Hoàn thành kế toán ORCA
     - Trạng thái bệnh nhân đã hoàn thành qua kế toán OCRA
     - X: hoàn thành

       O: chưa hoàn thành
   * - ``在･施医総管ｶｳﾝﾄ``
     - Count quản lý tại nhà/quản lý tại cơ sở chăm sóc
     - Số lượng người khám chung
     - Number
   * - ``医保レセ完了``
     - Hoàn thành bảng kê bảo hiểm y tế
     - Trạng thái
     - X: hoàn thành

       O: chưa hoàn thành
   * - ``プロアスコメント``
       黒字➡プロアスでの算定内容➡返信不要

       :blue:`青字➡算定に関するお知らせ事項➡返信不要・ご一読ください`. (回答があった場合も青字のまま残す)

       :red:`赤字➡算定に関する質問事項➡ご確認の上、回答をお願いいたします`.(回答後の対応が済み次第、黒字へ変更)
     - **Bình luận Proas**

       Chữ đen ➡ Nội dung tính toán tại Proas ➡ Không cần phản hồi

       :blue:`Chữ xanh ➡ Thông báo liên quan đến tính toán ➡ Không cần phản hồi, vui lòng đọc qua`. (Ngay cả khi có phản hồi, vẫn giữ nguyên chữ xanh)
       
       :red:`Chữ đỏ ➡ Câu hỏi liên quan đến tính toán ➡ Vui lòng xác nhận và phản hồi`. (Sau khi xử lý phản hồi, đổi sang chữ đen)
     - Mô tả
     - Mô tả
   * - ``医療機関様コメント``

       :blue:`青字はご一読いただくのみ、返信不要です`

       :red:`赤字はご回答をお願いいたします`
     - "**Bình luận từ cơ sở y tế**  

       :blue:`Chữ xanh: Chỉ cần đọc, không cần phản hồi.`

       :red:`Chữ đỏ: Vui lòng phản hồi.`
     - Mô tả
     - Mô tả
   * - ``病名記載欄``
     - Tên bệnh
     - Danh sách bệnh của bệnh nhân môi lần thăm khám
     - Danh sách các bệnh (text)
   * - ``次月引継ぎメモ``
     - Ghi chú bàn giao tháng tới
     - Mô tả
     - Mô tả
   * - ``7月診療分在宅精神療法算定患者``
     - Bệnh nhân tính toán cho liệu pháp tâm thần tại nhà (tháng 7)
     - Mô tả
     - Mô tả
   * - ``在宅精神療法``
     - Trị liệu tâm lý tại nhà (khám tâm thần)
     - Mô tả
     - X: hoàn thành

       O: chưa hoàn thành
   * - ``他医依頼``
     - Yêu cầu từ một bác sĩ khác (Nhờ bác sĩ khác)
     - Mô tả
     - Mô tả
   * - ``訪問回数``
     - Số lần thăm khám
     - Khách hàng đăng kí số lượng thăm khám tại tháng này
     - Number
   * - ``処理対象患者``
     - Bệnh nhân cần được điều trị
     - Mô tả
     - X: hoàn thành

       O: chưa hoàn thành
   * - ``DX情報活用加算``
     - 
     - Mô tả
     - Mô tả
   * - ``情報連携加算``
     - Cộng tác thông tin cao cấp
     - Mô tả
     - Mô tả
   * - ``包括的支援加算``
     - Hỗ trợ toàn diện cao cấp
     - Mức hỗ trợ toàn diện cao cấp
     - Giá trị từ 1 đến 4


Google SpreadSheet
----------------------

Định nghĩa
************
Trang Google Sheet chứa danh sách tên bệnh được coi là bệnh hiểm nghèo. Nhập liệu thủ công. Khách hàng quy định Critical Illness List Sample.
Khách hàng update file thường xuyên và không có khung thời gian cố định, thông báo.

Example: `Google Spreadsheet Sample`_

.. list-table:: Google Speadsheet
   :header-rows: 1
   :widths: 30 50

   * - **Đề mục**
     - **Ý nghĩa**
   * - **Bệnh**
     - Danh sách các bệnh được coi là bệnh hiểm nghèo. Tên bệnh sẽ được dùng để so sánh với ``bệnh của bệnh nhân``. Các 4 trường hợp so sánh khác nhau.
   * - **Khớp hoàn toàn**
     - Nếu ô này của bệnh được đánh dấu, thì ``tên bệnh hiểm nghèo`` phải giống hoàn toàn với ``bệnh của bệnh nhân`` mới được coi là bệnh hiểm nghèo.
   * - **Khớp đầu**
     - Nếu ô này của bệnh được đánh dấu, thì ``tên bệnh hiểm nghèo`` chỉ cần giống chuỗi kí tự đứng đầu của ``bệnh của bệnh nhân`` mới được coi là bệnh hiểm nghèo.
   * - **Khớp cuối**
     - Nếu ô này của bệnh được đánh dấu, thì ``tên bệnh hiểm nghèo`` chỉ cần giống chuỗi kí tự cuối của ``bệnh của bệnh nhân`` mới được coi là bệnh hiểm nghèo.
   * - **Khớp bất kì**
     - Nếu ô này của bệnh được đánh dấu, thì ``tên bệnh hiểm nghèo`` chỉ cần giống chuỗi kí tự bất kì của ``bệnh của bệnh nhân`` mới được coi là bệnh hiểm nghèo.
