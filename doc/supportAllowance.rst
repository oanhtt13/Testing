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

``Google Sheet:`` Trang quản lý  1 clinic. Khách hàng cung cấp.


Logic tinh CSF
-----------------------

Phí Hỗ trợ Toàn diện (CSF) được tính dựa trên các yếu tố sau:

* Mức độ hỗ trợ cần thiết cho bệnh nhân: ``要介護 3`` trở lên
* Mức độ tự lập trong sinh hoạt hằng ngày của người cao tuổi mắc sa sút trí tuệ: ``Rank III`` trở lên


Functional Requirementd
------------------------

FR-Support_Fee-1: Checking with priority conditions (Implementing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


FR-Selective_Comment-1: Implementing Selective Comment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: **Description**
   :header-rows: 1
   :widths: 15 100

   * - Content
     - Explain
   * - Description
     - Ho tro chuc nang nhap comment dang lua chon cho nguoi dung duoi cac dieu kien lien quan den Phí Hỗ trợ Toàn diện.
   * - Input
     - Thong tin trong bang ``tbl_item``
   * - Output
     - Giao diện nhập comment dạng lựa chọn cho người dùng.
   * - Trigger
     - Khi người dùng truy cập vào phần nhập liệu liên quan đến Phí Hỗ trợ Toàn diện.
   * - Preconditions
     - Tạo các điều kiện liên quan đến Phí Hỗ trợ Toàn diện trong hệ thống.
   * - Postconditions
     - Can tpc

