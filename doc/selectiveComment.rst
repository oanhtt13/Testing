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

       Lưu thông tin vào database
   * - Input
     - Database

       Danh sách bệnh nhân và các loại phí bệnh nhân cần phải chi trả
   * - Output
     - None
   * - Trigger
     - Khi lấy được thông tin tính phí của bệnh nhân
   * - Preconditions
     - Thông tin tại bảng ``mst_fee_comment`` phải được cập nhật

       Thông tin tại bảng được đọc thành công và lưu lại vào file ``/tmp/data/master_data/mst_fee_comments.csv``
   * - Postconditions
     - Comment tương ứng phải được cập nhật trên database, tại bảng ``tbl_record``


.. list-table:: **Main Flow**
   :header-rows: 1
   :widths: 20 30 50

   * - Step
     - Description
     - Acception
   * - 1. Cung cấp danh sách bệnh nhân kèm các loại phí
     - Nhập vào dataframe chứa thông tin danh sách bệnh nhân
     - Danh sách chứa thông tin ``patient_id``, ``record_id``, ``subunit_name``, ``private_home_flag``, ``number_patient_samedayaddress``, ``gh_flag``, ``exam_method``, ``anesthetic_flag``
   * - 2. Đọc danh sách các loại phí
     - Đọc file csv để lấy danh sách comment các loại phí
     - Lấy thông tin thành công
   * - 3. Kiểm tra các loại phí bệnh nhân cần chi trả
     - Kiểm tra các loại phí bệnh nhân cần chi trả, encoder phí sang code tương ứng
     -
   * - 4. Kiểm tra phí có nhiều loại comment hay không
     - Kiểm tra cột ``need_condition`` của file ``csv`` để lấy thông tin

       **Nếu:**

       need_condition = :red:`no`

       **Thì:**

       Lấy comment tương ứng với phí tại cột ``comment``

       **Nếu:**

       need_condition = :red:`yes`
     
       **Thì:**

       Kiểm tra cột ``condition`` rồi sang bước 4.1
     - Lấy thành công thông tin
   * - 4.1 Kiểm tra điều kiện generate comment
     - Kiểm tra cột ``condition``

       **Nếu:**

       Bệnh nhân có thông tin liên quan giống với thông tin trong ``condition`` thì sẽ gen comment theo cột ``comment`` tương ứng
     - Gen comment
   * - 5. Hoàn thiện comment
     - hgh
     - Tạo comment dạng text theo form


