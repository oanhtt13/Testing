.. role:: red

Selective Comment
====================

Mục đích
------------

Tính năng tạo comment cho từng loại phí được áp dụng cho người khám bệnh.

Tiền điều kiện
-----------------

Danh sách các comment cụ thể cho từng loại phí phải được tạo trước đó tại bảng ``mst_fee_comment`` trên database

Function Requirement
----------------------

FR-Comment_Handel-1: Generate_comment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: **Generate Comment**
   :header-rows: 1
   :widths: 30 80

   * - Content
     - Detail
   * - Description
     - Tạo comment tương ứng với từng loại phí mà khách hàng cần phải chi trả.

       Lưu comment vào database.
   * - Input
     - Database: ``mst_fee_comment``

       Danh sách bệnh nhân và các loại phí bệnh nhân cần phải chi trả

   * - Output
     - None
   * - Trigger
     - Khi lấy được thông tin tính phí của bệnh nhân
   * - Preconditions
     - Thông tin tại bảng ``mst_fee_comment`` phải được cập nhật

       Thông tin tại bảng trên được đọc thành công và lưu lại vào file ``/tmp/data/master_data/mst_fee_comments.csv``

       Bệnh nhân không có ``lert 3 flag``
   * - Postconditions
     - Comment tương ứng phải được cập nhật trên database, tại bảng ``tbl_record``


.. list-table:: **Business Flow**
   :header-rows: 1
   :widths: 20 30 50

   * - Step
     - Description
     - Acception
   * - 1. Cung cấp danh sách bệnh nhân kèm các loại phí
     - Nhập vào dataframe chứa thông tin danh sách record của từng bệnh nhân kèm thông tin các phí mà bệnh nhân cần phải chi trả.
     - Danh sách chứa thông tin:

       ``patient_id``, ``record_id``, ``subunit_name``, ``private_home_flag``, ``number_patient_samedayaddress``, ``gh_flag``, ``exam_method``, ``anesthetic_flag``
   * - 2. Đọc danh sách các loại phí
     - Đọc file csv (``MST_FEE_COMMENTS``) để lấy danh sách comment các loại phí
     - Lấy thông tin thành công
   * - 3. Kiểm tra các loại phí bệnh nhân cần chi trả
     - Kiểm tra các loại phí bệnh nhân cần chi trả, mapping phí sang mã code tương ứng
     - None
   * - 4. Kiểm tra phí có cần kiểm tra mục ``condition`` hay không
     - Kiểm tra cột ``need_condition`` của file ``csv`` để lấy thông tin

       **Nếu:**

       need_condition = ``no``

       **Thì:**

       Lấy comment tương ứng với phí tại cột ``comment``

       **Nếu:**

       need_condition = ``yes``
     
       **Thì:**

       Kiểm tra cột ``condition`` rồi sang bước 4.1

       **Nếu:**

       need_condition = ``notyet``

       **Thì:**

       Bỏ qua (Null)
     - Lấy thành công thông tin
   * - 4.1 Kiểm tra điều kiện generate comment
     - Kiểm tra cột ``condition`` trong file ``csv``

       **Nếu:**

       Kiểm tra điều kiện trả về ``True``

       **Thì:**

       Gen comment theo cột ``comment`` tương ứng
     - Lưu thông tin comment (nếu comment khác None)
   * - 5. Gen comment
     - Tạo comment theo cấu trúc sau:

       ``patient_id``, ``record_id``, ``comment_id``, ``parent_code``, ``comment``, ``reliability``, ``feedback``, ``numerical_value``, ``category_id``, ``priority``

       Lưu comment
     - Lưu thông tin vào dataframe
   * - 6. Nhóm dữ liệu dựa trên ``patient_id``, ``record_id``, ``parent_code``
     - Nhóm những dataframe mới tạo vào nhóm có chung ``patient_id``, ``record_id``, ``parent_code``

       **Nếu:**

       Giữ lại dataframe có ``priority`` nhỏ nhất. 
     - Giữ lại tất cả các comment trong dataframe có priority giống nhau.