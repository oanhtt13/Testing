Support Allowance
=============================

Muc đích
---------

Đối với ``包括的支援加算``,
ngoài các yêu cầu hiện có, bổ sung thêm các điều kiện mới nhằm **tăng số lượng bệnh nhân đủ điều kiện tính phí**.
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
Preconditions    Danh sách bệnh nhân không thuộc Alert 3 không rong.
Postconditions   Hệ thống xác định được bệnh nhân có đủ điều kiện nhận Phí Hỗ trợ Toàn diện hay không.
===============  =============================================================================================================================


.. list-table:: **Main Flow**
   :header-rows: 1
   :widths: 15 100 20

   * - Step
     - Action
     - Business Acceptance Criteria
   * - 1. Lay danh sach benh nhan
     - Hệ thống nhận danh sách bệnh nhân sau khi được lọc qua các điều kiện Alert 3
     - Lay thanh cong dang sach benh nhan
   * - 2. Kiem tra dieu kien
     - Sử dụng model AI giúp kiểm tra bệnh nhân có đủ điều kiện tính phí hỗ trợ toàn diện hay không
     - Kiem tra thanh cong dieu kien tinh phi ho tro toan dien
   * - 3. Xuat ket qua
     - Hệ thống xuất kết quả kiểm tra Phí Hỗ trợ Toàn diện (CSF) cho từng bệnh nhân
     - Xuat ket qua thanh cong

FR-Support_Fee-2: Updating Comprehensive Support Fee Conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: **Description**
   :header-rows: 1
   :widths: 15 100

   * - Content
     - Explain
   * - Description
     - Điều kiện chỉ được xét tới nếu sau FR-Support-Fee-1 trả về người bệnh không được tính phụ phí hỗ trợ hoàn diện.
   * - Input
     - Danh sách bệnh nhân không đủ điều kiện tính Phí Hỗ trợ Toàn diện từ FR-Support_Fee-1.
   * - Output
     - Danh sách các bệnh nhân đạt điều kiện tính phụ phí hỗ trợ toàn diện theo điều kiện bổ sung
   * - Trigger
     - Khi co yeu cau cap nhat dieu kien tinh phi ho tro toan dien moi.
   * - Preconditions
     - Danh sach
   * - Postconditions
     - He thong duoc cap nhat voi dieu kien tinh phi ho tro toan dien moi.


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

