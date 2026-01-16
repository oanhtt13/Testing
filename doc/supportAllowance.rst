Support Allowance
=============================

Mục đích
---------

Đối với ``包括的支援加算``, ngoài các yêu cầu hiện có, bổ sung thêm các điều kiện mới nhằm **tăng số lượng bệnh nhân đủ điều kiện tính phí**.
Đồng thời, **mở rộng chức năng nhập comment dạng lựa chọn** dựa trên các điều kiện mới này.

Định nghĩa Phí Hỗ trợ Toàn diện (CSF)
-----------------------------------------------

Hệ thống hỗ trợ
-----------------------

Google-Sheet: Trang quản lý  1 clinic. Khách hàng cung cấp. Tham khảo tại: :doc:`supportSystem`.


Logic tinh CSF
-----------------------

Phí Hỗ trợ Toàn diện (CSF) được tính dựa trên các yếu tố sau:

Điều kiện chính (độ ưu tiên cao nhất):
* Mức độ hỗ trợ cần thiết cho bệnh nhân: ``要介護 3`` trở lên
* Mức độ tự lập trong sinh hoạt hằng ngày của người cao tuổi mắc sa sút trí tuệ: ``Rank III`` trở lên

Điều kiện phụ (chỉ được sử dụng khi điều kiện chính không đủ): thông tin được cung cấp tại :doc:`supportSystem`, mục ``包括的支援加算``.

Functional Requirementd
------------------------

FR-Support_Fee-1: Checking with priority conditions (Implementing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Đây là phần tính năng đã có, các điều kiện này được ưu tiên hơn các điều kiện phía sau.

===============  =============================================================================================================================
Content          Explain
===============  =============================================================================================================================
Description      Hệ thống sẽ kiểm tra các điều kiện ưu tiên để xác định xem bệnh nhân có đủ điều kiện nhận Phí Hỗ trợ Toàn diện hay không.
Input            Dữ liệu bệnh nhân bao gồm mức độ hỗ trợ cần thiết và mức độ tự lập trong sinh hoạt hằng ngày.
Output           Kết quả kiểm tra Phí Hỗ trợ Toàn diện (CSF) - Đủ điều kiện hoặc Không đủ điều kiện (f24).
Trigger          Sau khi bệnh nhân được lọc qua Alert 3
Preconditions    Danh sách bệnh nhân không thuộc Alert 3 không rỗng.
Postconditions   Hệ thống xác định được bệnh nhân có đủ điều kiện nhận Phí Hỗ trợ Toàn diện hay không.
===============  =============================================================================================================================


.. list-table:: **Main Flow**
   :header-rows: 1
   :widths: 15 80 20

   * - Step
     - Action
     - Business Acceptance Criteria
   * - 1. Lấy danh sách bệnh nhân
     - Hệ thống nhận danh sách bệnh nhân sau khi được lọc qua các điều kiện Alert 3
     - Lấy thành công danh sách bệnh nhân
   * - 2. Kiểm tra điều kiện
     - Sử dụng model AI (``model 2``) giúp kiểm tra bệnh nhân có đủ điều kiện tính phí hỗ trợ toàn diện hay không
     - Kiểm tra thành công bệnh nhân
   * - 3. Xuất kết quả
     - Hệ thống xuất kết quả kiểm tra Phí Hỗ trợ Toàn diện (CSF) cho từng bệnh nhân
     - Lưu thông tin bệnh nhân có phí hỗ trợ vào database (``f24 = 1``)

FR-Support_Fee-2: Updating Comprehensive Support Fee Conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: **Description**
   :header-rows: 1
   :widths: 15 100

   * - Content
     - Explain
   * - Description
     - Điều kiện chỉ được xét tới nếu sau FR-Support-Fee-1 trả về người bệnh không được tính phụ phí hỗ trợ hoàn diện. (``f24 = 0``)

       Xét thêm điều kiện để tăng số lượng đối tượng được tính phí hỗ trợ.
   * - Input
     - Danh sách bệnh nhân không đủ điều kiện tính Phí Hỗ trợ Toàn diện từ FR-Support_Fee-1.
   * - Output
     - Danh sách các bệnh nhân đạt điều kiện tính phụ phí hỗ trợ toàn diện theo điều kiện bổ sung.
   * - Trigger
     - Sau khi chạy xong model 2.
   * - Preconditions
     - Thông tin cột ``包括的支援加算`` của trang Google Sheet được cập nhật.
   * - Postconditions
     - Các bệnh nhân đủ điều kiện 2 được update trạng thái mới (``tbl_record``)

       Update selective comment cho các trường hợp bệnh nhân đó.

.. list-tabel:: **Business Logic**
   :header-row: 1
   :widths: 15 50 20

   * - Step
     - Action
     - Business Acceptance Criteria
   * - 1. Lấy danh sách bệnh nhân
     - Lấy danh sách bệnh nhân được trả về sau model 2
     - Lấy thành công danh sách
   * - 2. Lọc danh sách bệnh nhân
     - Loại bỏ các bệnh nhân có ``f24 = 1`` (đã được tính phải bệnh hiểm nghèo)
     - Chỉ lấy những bệnh nhân chưa đạt điều kiện chính của phí hỗ trợ.
   * - 3. Đánh giá bệnh nhân
     - Đọc trang Google Sheet.

       **Nếu:**

       Cột ``包括的支援加算`` không rỗng (khác NULL)

       **Thì:**
       
       Bệnh nhân được tính phí hỗ trợ
     - Lưu thông tin phí được update vào database


FR-Selective_Comment-1: Implementing Selective Comment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Thông tin chi tiết tại :doc:`selectiveComment`.

.. list-table:: **Description**
   :header-rows: 1
   :widths: 15 100

   * - Content
     - Explain
   * - Description
     - Hỗ trợ chức năng nhập comment dạng lựa chọn cho người dùng dành cho các loại phí.
   * - Input
     - Thông tin trong bảng ``tbl_item``
   * - Output
     - Giao diện nhập comment dạng lựa chọn cho người dùng.
   * - Trigger
     - Khi người dùng truy cập vào phần nhập liệu liên quan đến Phí Hỗ trợ Toàn diện.
   * - Preconditions
     - Tạo các điều kiện liên quan đến Phí Hỗ trợ Toàn diện trong hệ thống.
   * - Postconditions
     - Tạo thành công comment và lưu thông tin vào ``tbl_record``.

